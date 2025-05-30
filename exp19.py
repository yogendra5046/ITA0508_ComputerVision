import cv2
import numpy as np
image = cv2.imread('samp.jpg', cv2.IMREAD_GRAYSCALE)
if image is None:
    print("Error: Image not found.")
    exit()
_, binary_image = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)
kernel = np.ones((5, 5), np.uint8)
eroded_image = cv2.erode(binary_image, kernel, iterations=1)
cv2.imshow("Original", image)
cv2.imshow("Binary", binary_image)
cv2.imshow("Eroded", eroded_image)
cv2.imwrite("eroded_output.jpg", eroded_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
