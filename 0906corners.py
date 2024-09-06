import numpy as np
import cv2


def corner_harris():
    src = cv2.imread('building.jpg', cv2.IMREAD_GRAYSCALE)

    if src is None:
        print('Image load failed!')
        return

    harris = cv2.cornerHarris(src, 3, 3, 0.04)
    harris_norm = cv2.normalize(harris, None, 0, 255, cv2.NORM_MINMAX, cv2.CV_8U)

    dst = cv2.cvtColor(src, cv2.COLOR_GRAY2BGR)

    for y in range(harris_norm.shape[0]):
        for x in range(harris_norm.shape[1]):
            if harris_norm[y, x] > 120:
                if (harris[y, x] > harris[y-1, x] and
                        harris[y, x] > harris[y-1, x] and
                        harris[y, x] > harris[y-1, x] and
                        harris[y, x] > harris[y-1, x]):
                    cv2.circle(dst, (x, y), 5, (0, 0, 255), 2)

    cv2.imshow('src', src)
    cv2.imshow('harris_norm', harris_norm)
    cv2.imshow('dst', dst)
    cv2.waitKey()
    cv2.destroyAllWindows()

# FAST(Features from Accelerated Segment Test)
# FAST 코너 검출기의 가장 큰 장점은 연산 효율성
# 또한 머신러닝 기술이 적용되면, 연산 시간과 자원 측면에서 우수한 성능을 실현
# 이러한 빠른 처리 속도 때문에 실시간 영상 처리 어플리케이션에 가장 적합

def corner_fast():
    src = cv2.imread('building.jpg', cv2.IMREAD_GRAYSCALE)

    if src is None:
        print('Image load failed!')
        return

    fast = cv2.FastFeatureDetector_create(60)
    keypoints = fast.detect(src)

    dst = cv2.cvtColor(src, cv2.COLOR_GRAY2BGR)

    for kp in keypoints:
        pt = (int(kp.pt[0]), int(kp.pt[1]))
        cv2.circle(dst, pt, 5, (0, 0, 255), 2)

    cv2.imshow('src', src)
    cv2.imshow('dst', dst)
    cv2.waitKey()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    corner_harris()
    corner_fast()
