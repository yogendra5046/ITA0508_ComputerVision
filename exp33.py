import numpy as np
import cv2
def create_rectangle_image(image_size):
 height, width = image_size 
 image = np.ones((height, width, 3), dtype=np.uint8) * 255
 top_left = (width // 4, height // 4)
 bottom_right = (3 * width // 4, 3 * height // 4)
 cv2.rectangle(image, top_left, bottom_right, (255, 0, 0), 2)
 cv2.imshow("Rectangle Image", image)
 cv2.waitKey(0)
 cv2.destroyAllWindows()
user_width = int(input("Enter image width: "))
user_height = int(input("Enter image height: "))
create_rectangle_image((user_height, user_width))