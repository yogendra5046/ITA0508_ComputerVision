import cv2
def segment_image(image_path, threshold_value=127):
 image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE) 
 _, segmented_image = cv2.threshold(image, threshold_value, 255, cv2.THRESH_BINARY)
 cv2.imshow("Original Image", image)
 cv2.imshow("Segmented Image", segmented_image)
 cv2.waitKey(0)
 cv2.destroyAllWindows()
segment_image("samp.jpg", 127) 