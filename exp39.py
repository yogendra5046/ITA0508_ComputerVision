import cv2

def play_video_reverse_slow(video_path):
    cap = cv2.VideoCapture(video_path)
    frames = []

    # Read all frames and store them in a list
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        frames.append(frame)  # This must be inside the loop!

    cap.release()

    # Display frames in reverse with a delay for slow motion
    for frame in reversed(frames):
        cv2.imshow('Reverse Slow Motion Video', frame)
        if cv2.waitKey(100) & 0xFF == ord('q'):  # 100ms delay between frames
            break

    cv2.destroyAllWindows()

# Example usage
play_video_reverse_slow('sd.mp4')
