# age-gender-recognition-mobilenet-groups-64x64-flask-server
Age and gender recognition - Flask API
Usage: python age_gender_recognition_server.py
It opens port 5000
To recognize an image using curl, make a HTTP POST request:
curl "http://127.0.0.1:5000" -H "Content-Type: multipart/form-data" --form "image=@image.jpg"
The response is in JSON format.

Dependencies:
pip install tensorflow
pip install numpy
pip install opencv-python

If you use Windows, the OpenCV have to be installed from: https://www.lfd.uci.edu/~gohlke/pythonlibs/
To install Tensorflow on Windows, you might need also Microsoft Visual C++ Redistributable for Visual Studio 2015, 2017 and 2019: https://support.microsoft.com/en-us/help/2977003/the-latest-supported-visual-c-downloads

