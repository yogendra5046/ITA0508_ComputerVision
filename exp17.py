import cv2
image = cv2.imread('samp.jpg')  
watermark_text = 'yogendra '
font = cv2.FONT_HERSHEY_SIMPLEX
font_scale = 1
color = (255, 255, 255)  
thickness = 2

height, width = image.shape[:2]

text_size, _ = cv2.getTextSize(watermark_text, font, font_scale, thickness)
text_x = width - text_size[0] - 10
text_y = height - 10

cv2.putText(image, watermark_text, (text_x, text_y), font, font_scale, color, thickness)

cv2.imwrite('watermarked_output.jpg', image)
cv2.imshow('Watermarked Image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
