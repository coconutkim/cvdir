import cv2
img_quo=cv2.imread('C:/ex/img/ai-generated-8244720_1280.webp')

x,y=100,100
title='quokka'

while True:
    cv2.imshow('quokka', img_quo)
    cv2.moveWindow(title, x, y) # 이 좌표로 이동해라
    key=cv2.waitKey () & 0xFF
    print(key,chr(key))
    # if key ==ord('q') or key == 27:
    #     break
    #     cv2.destroyAllWindows()
    if key ==ord('h'): 
        x -=10
    elif key ==ord('j'):
        y +=10
    elif key ==ord('k'):
        y -=10
    elif key ==ord('l'):
        x +=10
    # q나 esc를 누르면 끝내라
    elif key ==ord('q') or key == 27:
        break
        cv2.destroyAllWindows()
    cv2.moveWindow(title, x, y) # 이 좌표로 이동해라