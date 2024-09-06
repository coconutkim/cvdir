import sys
import numpy as np
import cv2

src_orig=cv2.imread('./img/maze.png')
src = cv2.imread('./img/maze.png', cv2.IMREAD_GRAYSCALE)

if src is None:
    print('Image load failed!')
    sys.exit()

orb = cv2.ORB_create()

keypoints = orb.detect(src)
keypoints, desc = orb.compute(src, keypoints)

print('len(keypoints):', len(keypoints))
print('desc.shape:', desc.shape)

# 예를 들어 keypoints의 크기가 일정 값 이하만 그리기
min_size = 50  # 이 값은 원하는 키포인트 크기에 따라 조정 가능
# 50 이상은 되어야 키포인트가 나온다. 값이 아주 작으면 아무것도 검출하지 못한다
keypoints = [kp for kp in keypoints if kp.size < min_size]

dst = cv2.drawKeypoints(src, keypoints, None, (-1, -1, -1),
                       cv2.DrawMatchesFlags_DRAW_RICH_KEYPOINTS)

cv2.imshow('src', src_orig)
cv2.imshow('dst', dst)
cv2.waitKey()
cv2.imwrite(r'C:\ex\cvdir\img\maze_keypoints.jpg',dst)
cv2.destroyAllWindows()