import cv2
import numpy as np

img = cv2.imread('../img/blank_500.jpg')

cv2.rectangle(img, (450, 200), (200, 450), (0,0,255), -1 )
pts3 = np.array([[325,20], [200,200], [450,200]], dtype=np.int32)  
cv2.polylines(img, [pts3], True, (0,0,255), 10)  

cv2.imshow('house', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# error1
# (mldltest1) C:\ex\MLDL>python house.py
# python: can't open file 'house.py': [Errno 2] No such file or directory

# (mldltest1) C:\ex\MLDL>cd cvdir

