import cv2
img_quo=cv2.imread('C:/ex/img/ai-generated-8244720_1280.webp')

title='quokka'

def onMouse(event,x,y):
    print(event,x,y)
    # if event == cv2.EVENT_LBUTTONDOWN:
    #     cv2.circle(img_quo,(x,y))
    cv2.circle(img_quo,(x,y),30,(0,0,0),-1)
    img_quo.imshow(title,img_quo)
    
cv2.setMouseCallback(title,onMouse)

while True:
    if cv2.waitKey() == 27:
        break
    
cv2.destroyAllWindows()