import requests
from IPython.display import HTML
#%matplotlib inline
import matplotlib.pyplot as plt
from PIL import Image
from matplotlib import patches
from io import BytesIO
import http.client, urllib.request, urllib.parse, urllib.error, base64, sys, httplib2
import simplejson as json
import numpy as np
import cv2
import time

def annotate_pic(nam):
    name = nam + '.jpg'
    image_data = open(name, "rb")
    response = requests.post(face_api_url, params=params, headers=headers, data=image_data)
    response.raise_for_status()
    faces = response.json()
    image = Image.open(name)
    plt.figure(figsize=(8,8))
    ax = plt.imshow(image, alpha=0.6)
    for face in faces:
        fr = face["faceRectangle"]
        fa = face["faceAttributes"]
        h = fa['emotion']
        emotval = 0
        for emot in h.keys():
            if h[emot]>emotval:
                chosenemot = emot
                emotval = h[emot]
        origin = (fr["left"], fr["top"])
        p = patches.Rectangle(origin, fr["width"], fr["height"], fill=False, linewidth=2, color='r')
        ax.axes.add_patch(p)
        plt.text(origin[0], origin[1], "%s, %d, %s"%(fa["gender"].capitalize(), fa["age"], chosenemot.capitalize()), fontsize=10, weight="bold", va="bottom")
    plt.axis("off")
    name2 = nam + 'annotated'+'.jpg'
    plt.savefig(name2)



subscription_key = 'insert key here'
assert subscription_key
face_api_url = 'https://westcentralus.api.cognitive.microsoft.com/face/v1.0/detect'
image_url = 'https://scontent-lht6-1.xx.fbcdn.net/v/t1.0-9/22519134_1875995839096291_5085130781646904423_n.jpg?_nc_cat=109&_nc_ht=scontent-lht6-1.xx&oh=8f436a6ab66fea0e9b43a17f9874b1da&oe=5D27A0F4'

headers = {
            'Ocp-Apim-Subscription-Key': subscription_key ,
            'Content-Type': 'application/octet-stream',}

params = {
    'returnFaceId': 'true',
    'returnFaceLandmarks': 'false',
    'returnFaceAttributes': 'age,gender,headPose,smile,facialHair,glasses,emotion,hair,makeup,occlusion,accessories,blur,exposure,noise',}

cap = cv2.VideoCapture(0) # video capture source camera (Here webcam of laptop)

while(True):
    ret,frame = cap.read() # return a single frame in variable `frame`
    cv2.namedWindow("Emotions", cv2.WND_PROP_FULLSCREEN)
    cv2.setWindowProperty("Emotions",cv2.WND_PROP_FULLSCREEN,cv2.WINDOW_FULLSCREEN)
    vertical_img = frame.copy()
    vertical_img = cv2.flip( frame, 1 )
    cv2.imshow('Emotions',vertical_img) #display the captured image
    if cv2.waitKey(1) & 0xFF == ord('y'): #save on pressing 'y'
        nam = 'test' + str(int(time.time()))
        name = nam + '.jpg'
        cv2.imwrite(name,vertical_img)
        annotate_pic(nam)
        cv2.destroyAllWindows()
        img2 = nam + 'annotated'+'.jpg'
        imger = cv2.imread(img2,1)
        cv2.namedWindow("Emotions Result", cv2.WND_PROP_FULLSCREEN)
        cv2.setWindowProperty("Emotions Result",cv2.WND_PROP_FULLSCREEN,cv2.WINDOW_FULLSCREEN)
        cv2.imshow('Emotions Result',imger)
        if cv2.waitKey(0) & 0xFF == ord('n'): #quit on pressing q
            cv2.destroyWindow('Emotions Result')
        #break
    elif cv2.waitKey(1) & 0xFF == ord('q'): #quit on pressing q
        cv2.destroyAllWindows()
        break
cap.release()

img2 = nam + 'annotated'+'.jpg'

imger = cv2.imread(img2,1)
cv2.namedWindow("Emotions Result", cv2.WND_PROP_FULLSCREEN)
cv2.setWindowProperty("Emotions Result",cv2.WND_PROP_FULLSCREEN,cv2.WINDOW_FULLSCREEN)
cv2.imshow('Emotions Result',imger)
if cv2.waitKey(0) & 0xFF == ord('q'): #quit on pressing q
    cv2.destroyAllWindows()
