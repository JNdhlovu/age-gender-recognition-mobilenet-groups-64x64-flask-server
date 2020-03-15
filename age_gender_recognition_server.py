# Copyright © 2019 by Spectrico

from flask import Flask, request
from flask_cors import CORS, cross_origin
import numpy as np
import classifier
import MTCNN
import base64
import traceback
import json
import io
import cv2

app = Flask(__name__)
CORS(app)

age_gender_classifier = classifier.Classifier()
mtcnn = MTCNN.MTCNN()

@app.route("/", methods = ['POST'])
@cross_origin()
def objectDetect():
    if request.headers['Content-Type'].startswith('multipart/form-data'):
        faces = []
        try:
            import numpy as np
            data = np.fromstring(request.files['image'].read(), dtype=np.uint8)
            img = cv2.imdecode(data, cv2.IMREAD_COLOR)
            if img is None:
                response = app.response_class(
                    response='415 Bad image',
                    status=415,
                    mimetype='text/plain'
                )
                return response
            boxes = mtcnn.detect(img[:,:,::-1])
            for box in boxes:
                # extract the bounding box coordinates
                score = box[4]
                box = box[:4] + 0.5
                box = box.astype(np.int32)
                x = box[0]
                y = box[1]
                w = box[2] - x
                h = box[3] - y
                l = max(w, h)
                x1 = int(x - (l - w) / 2)
                y1 = int(y - (l - h) / 2)
                x2 = x1 + l
                y2 = y1 + l
                x1 = max(0, x1)
                y1 = max(0, y1)
                x2 = min(img.shape[1], x2)
                y2 = min(img.shape[0], y2)
                result = age_gender_classifier.predict(img[y1:y2, x1:x2])
                rect = {"left": str(x), "top": str(y), "width": str(w), "height": str(h)}
                faces.append(
                    {"age": str(result[0]["age"]), "gender": result[0]["gender"], "prob": result[0]["prob"], "rect": rect})
        except:
            traceback.print_exc()
            response = app.response_class(
                response='415 Unsupported Media Type',
                status=415,
                mimetype='text/plain'
            )
            return response
        response = app.response_class(
            response=json.dumps({"faces": faces}),
            status=200,
            mimetype='application/json'
        )
        return response
    else:
        return "415 Unsupported Media Type"

@app.route("/", methods = ['GET'])
@cross_origin()
def version():
    response = app.response_class(
        response='{"version":"age and gender recognition 1.0"}',
        status=200,
        mimetype='application/json'
    )
    return response

@app.before_request
def option_autoreply():
    """ Always reply 200 on OPTIONS request """
    if request.method == 'OPTIONS':
        resp = app.make_default_options_response()

        headers = None
        if 'ACCESS_CONTROL_REQUEST_HEADERS' in request.headers:
            headers = request.headers['ACCESS_CONTROL_REQUEST_HEADERS']

        h = resp.headers

        # Allow the origin which made the XHR
        h['Access-Control-Allow-Origin'] = request.headers['Origin']
        # Allow the actual method
        h['Access-Control-Allow-Methods'] = request.headers['Access-Control-Request-Method']
        # Allow for 10 seconds
        h['Access-Control-Max-Age'] = "10"

        # We also keep current headers
        if headers is not None:
            h['Access-Control-Allow-Headers'] = headers

        return resp


@app.after_request
def set_allow_origin(resp):
    """ Set origin for GET, POST, PUT, DELETE requests """

    h = resp.headers

    # Allow crossdomain for other HTTP Verbs
    if request.method != 'OPTIONS' and 'Origin' in request.headers:
        h['Access-Control-Allow-Origin'] = request.headers['Origin']

    return resp

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=False, use_reloader=False, threaded=False)
