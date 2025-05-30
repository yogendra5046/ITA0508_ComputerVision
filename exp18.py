import cv2
image = cv2.imread("samp.jpg")
if image is None:
    print("Error: Image not found.")
    exit()
img_height, img_width = image.shape[:2]
print(f"Image size: width={img_width}, height={img_height}")

x, y, w, h = 50, 50, 100, 100

if y + h > img_height or x + w > img_width:
    print("Error: ROI is out of bounds.")
    exit()
roi = image[y:y+h, x:x+w]

paste_x, paste_y = 100, 100  

if paste_y + h <= img_height and paste_x + w <= img_width:
    image[paste_y:paste_y+h, paste_x:paste_x+w] = roi
else:
    print("Error: ROI paste area is out of image bounds.")
    exit()

cv2.imshow("ROI Copied", image)
cv2.imwrite("output.jpg", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
