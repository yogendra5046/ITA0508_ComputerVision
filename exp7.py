import cv2
cap = cv2.VideoCapture('sd.mp4')  
if not cap.isOpened():
    print("Error: Cannot open video file or stream.")
    exit()
speed_mode = input("Enter mode (normal/slow/fast): ").strip().lower()

if speed_mode == 'slow':
    delay = 60  
elif speed_mode == 'fast':
    delay = 10   
else:
    delay = 30   

while True:
    ret, frame = cap.read()
    if not ret:
        break  
    cv2.imshow('Video Playback', frame)

    if cv2.waitKey(delay) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
