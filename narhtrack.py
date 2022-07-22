import cv2
import os
import time
from ffpyplayer.player import MediaPlayer
from cvzone.HandTrackingModule import HandDetector


folderPath = "handsigns"

cap = cv2.VideoCapture(0)

imgPath = os.listdir(folderPath)

width, height = 1280, 720
hs, ws = 120, 213
signDelay = 15
signDoing = False
signCount = 0
