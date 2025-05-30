import cv2
watch_cascade = cv2.CascadeClassifier("watch_cascade.xml")
if watch_cascade.empty():
    print("Error loading cascade file")
    exit()
image = cv2.imread("watchdet.jpg")
if image is None:
    print("Error loading image")
    exit()
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gray = cv2.equalizeHist(gray)
watches = watch_cascade.detectMultiScale(
    gray,
    scaleFactor=1.1,  
    minNeighbors=5,   
    minSize=(50, 50)  
)
print(f"Number of watches detected: {len(watches)}")
for (x, y, w, h) in watches:
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
cv2.imshow("Detected Watch", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
