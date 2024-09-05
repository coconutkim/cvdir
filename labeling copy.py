import numpy as np
import cv2

# 라벨링이란 이미지 속 비슷한 무리의 픽셀까지 그룹화하여 구별이 가능하도록
def labeling_basic():
    src = np.array([[0, 0, 1, 1, 0, 0, 0, 0],
                    [1, 1, 1, 1, 0, 0, 1, 0],
                    [1, 1, 1, 1, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 1, 1, 0],
                    [0, 0, 0, 1, 1, 1, 1, 0],
                    [0, 0, 0, 1, 0, 0, 1, 0],
                    [0, 0, 1, 1, 1, 1, 1, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0]]).astype(np.uint8)
    
    # 이진화를 적용하기 위해 0과 255로 변환
    src = src * 255

    cnt, labels = cv2.connectedComponents(src, connectivity=4)

    print('src:'), 
    print(src)
    print('labels:')
    print(labels)
    print('number of labels:', cnt)


def labeling_stats():
    src = cv2.imread(r'C:\ex\cvdir\img\crosswalk.jpg', cv2.IMREAD_GRAYSCALE)

    if src is None:
        print('Image load failed!')
        return

    _, src_bin = cv2.threshold(src, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

    cnt, labels, stats, centroids = cv2.connectedComponentsWithStats(src_bin)

    dst = cv2.cvtColor(src, cv2.COLOR_GRAY2BGR)

    for i in range(1, cnt):
        (x, y, w, h, area) = stats[i]

        if area < 20:
            continue

        pt1 = (x, y)
        pt2 = (x + w, y + h)
        cv2.rectangle(dst, pt1, pt2, (0, 255, 255))

    cv2.imshow('src', src)
    cv2.imshow('dst', dst)

    cv2.waitKey()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    labeling_basic()
    labeling_stats()
