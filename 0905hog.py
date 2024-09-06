import sys
import numpy as np
import cv2
import random

from pytube import YouTube

# 유튜브 동영상 URL
url = 'https://www.youtube.com/watch?v=zSQ48zyWZrY'

# YouTube 객체 생성
yt = YouTube(url)

# 영상 스트림 선택 (예: 720p)
stream = yt.streams.filter(file_extension='avi').get_highest_resolution()

# 동영상 다운로드
stream.download(filename='svt.avi')


cap = cv2.VideoCapture('svt.avi')

if not cap.isOpened():
    print('Video open failed!')
    sys.exit()

hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

while True:
    ret, frame = cap.read()

    if not ret:
        break

    detected, _ = hog.detectMultiScale(frame)

    for (x, y, w, h) in detected:
        c = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        cv2.rectangle(frame, (x, y), (x + w, y + h), c, 3)

    cv2.imshow('frame', frame)
    if cv2.waitKey(10) == 27:
        break

cv2.destroyAllWindows()
