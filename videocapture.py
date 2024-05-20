import cv2

# Capture video from webcam
vid_capture = cv2.VideoCapture(0)  # Use device index 0 for the default webcam

# Define the codec and create a VideoWriter object
vid_cod = cv2.VideoWriter_fourcc(*'XVID')  # Codec for saving as .mp4
output = cv2.VideoWriter(r"C:\invictus6\images\cam_video1.mp4", vid_cod, 20.0, (640, 480))

while True:
    # Capture each frame of webcam video
    ret, frame = vid_capture.read()

    # Display the video in a window (optional)
    cv2.imshow("My cam video", frame)

    # Write the frame to the output video file
    output.write(frame)

    # Close and break the loop after pressing "x" key
    if cv2.waitKey(1) & 0xFF == ord('x'):
        break

# Release resources
vid_capture.release()  # Close the camera
# output.release()  # Close the output file
cv2.destroyAllWindows()  # Close the window and free memory
