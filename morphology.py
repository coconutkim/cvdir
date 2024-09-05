import numpy as np
import cv2
from matplotlib import pyplot as plt


def erode_dilate():
    src = cv2.imread('milkdrop.bmp', cv2.IMREAD_GRAYSCALE)
    # src 입력 영상
    # 파일을 그레이스케일 영상 형식으로 불러와 src에 저장

    if src is None:
        print('Image load failed!')
        return

    _, src_bin = cv2.threshold(src, 0, 255,
                               cv2.THRESH_BINARY | cv2.THRESH_OTSU)
    
    # _, src_bin = ... 구문
    # 파이썬에서 값을 무시하거나 필요 없는 값을 처리할 때 자주 사용됩니다
    
    # **_** 반환된 값 중에서 사용하지 않을 값을 나타냅니다

    dst1 = cv2.erode(src_bin, None)
    # dst 출력 영상, src와 같은 크기, 같은 타입
    dst2 = cv2.dilate(src_bin, None)

    plt.subplot(221), plt.axis('off'), plt.imshow(src, 'gray'), plt.title('src')
    plt.subplot(222), plt.axis('off'), plt.imshow(src_bin, 'gray'), plt.title('src_bin')
    plt.subplot(223), plt.axis('off'), plt.imshow(dst1, 'gray'), plt.title('erode')
    plt.subplot(224), plt.axis('off'), plt.imshow(dst2, 'gray'), plt.title('dilate')
    plt.show()


def open_close():
    src = cv2.imread('milkdrop.bmp', cv2.IMREAD_GRAYSCALE)

    if src is None:
        print('Image load failed!')
        return

    _, src_bin = cv2.threshold(src, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

    dst1 = cv2.morphologyEx(src_bin, cv2.MORPH_OPEN, None)
    dst2 = cv2.morphologyEx(src_bin, cv2.MORPH_CLOSE, None)

    plt.subplot(221), plt.axis('off'), plt.imshow(src, 'gray'), plt.title('src')
    plt.subplot(222), plt.axis('off'), plt.imshow(src_bin, 'gray'), plt.title('src_bin')
    plt.subplot(223), plt.axis('off'), plt.imshow(dst1, 'gray'), plt.title('open')
    plt.subplot(224), plt.axis('off'), plt.imshow(dst2, 'gray'), plt.title('close')
    plt.show()


if __name__ == '__main__':
    erode_dilate()
    open_close()
