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
    success, img = cap.read()
     
    hands, img = detector.findHands(img)
