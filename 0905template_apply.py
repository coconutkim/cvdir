# 불량 부분을 템플릿 이미지로 지정하여 원본 이미지에서 비슷한 부분을 찾아주는 방식
# 원본 이미지(circuit.bmp)에서 **템플릿 이미지(crystal.bmp)**와 일치하거나 유사한 부분을
# cv2.matchTemplate() 함수로 찾아서 표시하는 것이 목표

# 일종의 숨은 그림 찾기

import sys
import numpy as np
import cv2


img = cv2.imread(r'C:\ex\cvdir\img\starwars.jpg', cv2.IMREAD_COLOR)
templ = cv2.imread(r'C:\ex\cvdir\img\starwars_template.jpg', cv2.IMREAD_COLOR)

if img is None or templ is None:
    print('Image load failed!')
    sys.exit()

img = img + (50, 50, 50)

noise = np.zeros(img.shape, np.int32)
cv2.randn(noise, 0, 10)
img = cv2.add(img, noise, dtype=cv2.CV_8UC3)

res = cv2.matchTemplate(img, templ, cv2.TM_CCOEFF_NORMED)
res_norm = cv2.normalize(res, None, 0, 255, cv2.NORM_MINMAX, cv2.CV_8U)
# 템플릿 매칭 결과를 0에서 255 사이로 정규화

_, maxv, _, maxloc = cv2.minMaxLoc(res)
print('maxv:', maxv)

(th, tw) = templ.shape[:2]
cv2.rectangle(img, maxloc, (maxloc[0] + tw, maxloc[1] + th), (0, 0, 255), 2)

# cv2.namedWindow('templ',cv2.WINDOW_NORMAL)
cv2.imshow('templ', templ)
cv2.imshow('res_norm', res_norm)
cv2.imshow('img', img)
cv2.waitKey()
cv2.destroyAllWindows()
