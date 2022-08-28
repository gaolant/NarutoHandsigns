import cv2
import os
import time
from ffpyplayer.player import MediaPlayer
from cvzone.HandTrackingModule import HandDetector


folderPath = "handsigns"

cap = cv2.VideoCapture(0)

imgPath = os.listdir(folderPath)

# Variables
width, height = 1280, 720
hs, ws = 120, 213
signDelay = 15
signDoing = False
signCount = 0

# Hand detector
detector = HandDetector(detectionCon=0.8, maxHands=2)

# Sign pattern
pattern = []
raikiri = ['ox', 'hare', 'monkey']
earthwal = ['tiger', 'dog', 'ox', 'horse', 'hare', 'tiger', 'boar', 'serpent']


# start video
while True:
    
    #import images
    success, img = cap.read()
     
    hands, img = detector.findHands(img)
    
    if len(hands) == 2 and signDoing == False:
        hand1 = hands[0]
        hand2 = hands[1]
        lmListh1 = hand1['lmList']
        lmListh2 = hand2['lmList']

        # print(lmListh1[0][0])
        # print(lmListh2[0][0])

        fingersh1 = detector.fingersUp(hand1)
        fingersh2 = detector.fingersUp(hand2)
