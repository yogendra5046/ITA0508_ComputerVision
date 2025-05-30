import cv2
image =cv2.imread('samp.jpg')
bigger_img=cv2.resize(image,None,fx=2,fy=2,interpolation=cv2.INTER_LINEAR)
smaller_img=cv2.resize(image,None,fx=0.5,fy=0.5,interpolation=cv2.INTER_AREA)
cv2.imshow("org img",image)
cv2.imshow("biger image ",bigger_img)
cv2.imshow("small image ",smaller_img)
cv2.waitKey(0)
cv2.destroyAllWindows()