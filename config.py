# Copyright © 2020 by Spectrico

model_file = "model-weights-spectrico-age-gender-recognition-groups-mobilenet-64x64-9CFFCA00.pb"  # path to the age and gender classifier
label_file = "labels.txt"   # path to the text file, containing list with the supported classes
input_layer = "input_1"
output_layer = "softmax/Softmax"
classifier_input_size = (64, 64) # input size of the classifier
