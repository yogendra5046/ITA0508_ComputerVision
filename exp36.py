import cv2
import numpy as np
def subtract_background(image_path, lower_color, upper_color):
 image = cv2.imread(image_path)
 hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
 lower_bound = np.array(lower_color, dtype=np.uint8)
 upper_bound = np.array(upper_color, dtype=np.uint8)
 mask = cv2.inRange(hsv, lower_bound, upper_bound)
 mask_inv = cv2.bitwise_not(mask)
 foreground = cv2.bitwise_and(image, image, mask=mask_inv)
 cv2.imshow("Original Image", image)
 cv2.imshow("Background Subtracted Image", foreground)
 cv2.waitKey(0)
 cv2.destroyAllWindows()
image_path = "samp.jpg" 
lower_color = [30, 30, 30] 
upper_color = [255, 255, 255] 
subtract_background(image_path, lower_color, upper_color)