import cv2
import numpy as np

img = cv2.imread('./img/missing_hole.jpg')

# 구조화 요소 커널, 사각형 (5x5) 생성 ---①
k = cv2.getStructuringElement(cv2.MORPH_RECT, (2,2))

# (2,2)
# 정수로 넣어야 한다
# 숫자가 작아질수록 어두워진다. 이게 불량 검출에 적합한 듯
# 숫자가 커질수록 색의 변형이 일어난다

# 탑햇 연산 적용 ---②
tophat = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, k)
# 블랫햇 연산 적용 ---③
blackhat = cv2.morphologyEx(img, cv2.MORPH_BLACKHAT, k)

# 결과 출력
merged = np.vstack((img, tophat, blackhat)) # 세로
# merged = np.hstack((img, tophat, blackhat)) # 가로
cv2.imshow('tophat blackhat', merged)
cv2.waitKey(0)
cv2.destroyAllWindows()