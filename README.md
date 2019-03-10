# HealthHack19

We built HAPI. 

The code is in the following files:
final.py - This file uses the webcam to take images using opencv and uses the microsoft azure api to detect key indicators from each image such as age, gender, headPose, smile, facialHair, glasses, emotion, hair, makeup, occlusion and accessories.The taken image will then be presented with an overlay showing the detected face with the detected gender, age and emotion shown.

textsent.py - This utilises the VaderSentiment library to carry out sentiment analysis on a diary entry to look for negative, neutral and positive terms and returns a compounded score

gui.py - An attempt at a basic GUI using the pySimpleGUI library. 
