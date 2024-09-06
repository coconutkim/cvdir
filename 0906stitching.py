# python 0906stitching.py img1.jpg img2.jpg img3.jpg
# python 0906stitching.py dog_img1.jpg dog_img2.jpg dog_img3.jpg

import sys
import numpy as np
import cv2

# src=cv2.imread(r'C:\ex\cvdir\img\dog_park.jpg')

argc = len(sys.argv)
if argc < 3:
    print('Usage: stitching.exe <image_file1> <image_file2> [<image_file3> ...]')
    sys.exit()

imgs = []
for i in range(1, argc):
    img = cv2.imread(sys.argv[i])

    if img is None:
        print('Image load failed!')
        sys.exit()

    imgs.append(img)

stitcher = cv2.Stitcher_create()
status, dst = stitcher.stitch(imgs)

# if status != cv2.Stitcher_OK:
#     print('Error on stitching!')
#     sys.exit()
if status == cv2.Stitcher_ERR_NEED_MORE_IMGS:
        print("Error: Need more images.")
        sys.exit()
# elif status == cv2.Stitcher_ERR_OUTOFMEMORY:
#     print("Error: Out of memory.")
#     sys.exit()
# elif status == cv2.Stitcher_ERR_NOT_ENOUGH_FEATURES:
#     print("Error: Not enough features.")
#     sys.exit()
# elif status == cv2.Stitcher_ERR_HOMOGRAPHY_EST_FAIL:
#     print("Error: Homography estimation failed.")
#     sys.exit()
# elif status == cv2.Stitcher_ERR_CAMERA_PARAMS_ADJUST_FAIL:
#     print("Error: Camera parameters adjustment failed.")
#     sys.exit()

img1=cv2.imread('dog_img1.jpg')
img2=cv2.imread('dog_img2.jpg')
img3=cv2.imread('dog_img3.jpg')

cv2.imwrite('dogs.jpg', dst)
# cv2.imshow('orig',src)
cv2.imshow('img1',img1)
cv2.imshow('img2',img2)
cv2.imshow('img3',img3)
cv2.imshow('dst', dst)

cv2.waitKey()
cv2.destroyAllWindows()

# first error
# 자른 이미지가 서로 충분히 겹치지 않았다
# solution
# 에러가 날 경우 이것을 경우에 따라 상태를 프린트해서 상황 파악을 한다
# 에러 종류에 따라 문제를 해결
# this type
# 이미지를 어느정도 겹친다