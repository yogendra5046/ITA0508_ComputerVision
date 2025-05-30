import cv2
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
smile_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_smile.xml')
if face_cascade.empty() or smile_cascade.empty():
    print("Error loading cascade classifiers")
    exit()
image = cv2.imread('face.jpg') 
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray, 1.3, 5)
for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2)
    roi_gray = gray[y:y + h, x:x + w]
    roi_color = image[y:y + h, x:x + w]
    height = roi_gray.shape[0]
    roi_gray_lower = roi_gray[height//2:]
    roi_color_lower = roi_color[height//2:]
    smiles = smile_cascade.detectMultiScale(
        roi_gray_lower,
        scaleFactor=1.3,
        minNeighbors=10,
        minSize=(25, 25)
    )
    for (sx, sy, sw, sh) in smiles:
        cv2.rectangle(roi_color_lower, (sx, sy), (sx + sw, sy + sh), (0, 255, 0), 2)
cv2.imshow('Smile Detection', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
