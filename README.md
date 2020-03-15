# age-gender-recognition-mobilenet-groups-64x64-flask-server
Age and gender recognition - Flask REST API
<br/>Usage: python age_gender_recognition_server.py
<br/>It opens port 5000
<br/>To recognize an image using curl, make a HTTP POST request:
```
curl "http://127.0.0.1:5000" -H "Content-Type: multipart/form-data" --form "image=@image.jpg"
```
The response is in JSON format:
```json
{"faces": [{"age": "3-5", "gender": "female", "prob": "0.6655734", "rect": {"left": "371", "top": "367", "width": "67", "height": "88"}}, {"age": "39-41", "gender": "female", "prob": "0.27251807", "rect": {"left": "557", "top": "208", "width": "76", "height": "111"}}, {"age": "33-35", "gender": "male", "prob": "0.20505214", "rect": {"left": "693", "top": "77", "width": "93", "height": "150"}}]}
```

Dependencies:
```
pip install tensorflow
pip install numpy
pip install opencv-python
pip install Pillow
```

If you use Windows, the OpenCV have to be installed from: https://www.lfd.uci.edu/~gohlke/pythonlibs/
<br/>To install Tensorflow on Windows, you might need also Microsoft Visual C++ Redistributable for Visual Studio 2015, 2017 and 2019: https://support.microsoft.com/en-us/help/2977003/the-latest-supported-visual-c-downloads

Python client example: python age_gender_recognition_api_client.py
