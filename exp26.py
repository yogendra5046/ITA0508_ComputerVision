import cv2
def reverse_video(input_video_path, output_video_path):
    cap = cv2.VideoCapture('sd.mp4')

    frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = int(cap.get(cv2.CAP_PROP_FPS))

    fourcc = cv2.VideoWriter_fourcc(*"mp4v")  
    out = cv2.VideoWriter(output_video_path, fourcc, fps, (frame_width, frame_height))

    frames = []

    while True:
        ret, frame = cap.read()
        if not ret:
            break
        frames.append(frame)

    cap.release()

    frames.reverse()

    for frame in frames:
        out.write(frame)

    out.release()
    print(f"Reversed video saved as: {output_video_path}")

reverse_video("sd.mp4", "output_reversed.mp4")
