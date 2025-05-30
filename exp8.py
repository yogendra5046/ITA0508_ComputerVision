import cv2
import numpy as np
im =cv2.imread('samp.jpg')
cv2.imshow("original Image",im)
gray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
kernel =np.ones((5,5),np.uint8)
dilated_image=cv2.dilate(gray, kernel,iterations=1)
cv2.imshow("Dilated image",dilated_image)
cv2.imshow('dilated Image',dilated_image)
cv2.waitKey(0)
cv2.destroyAllWindows()