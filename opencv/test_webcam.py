import cv2

# Initialize the webcam (0 is usually the default camera)
cap = cv2.VideoCapture(0)

# Check if the webcam is opened correctly
if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()

# Define codec and create VideoWriter object to save video
# fourcc = cv2.VideoWriter_fourcc(*'XVID')
# out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    if not ret:
        print("Failed to grab frame.")
        break

    # Write the frame to the video file
    # out.write(frame)

    # Display the resulting frame
    cv2.imshow('Webcam', frame)

    # Capture photo when 'p' key is pressed
    key = cv2.waitkey(1)
    if key == ord('p'):
        cv2.imwrite('photo.jpg', frame)
        print("Photo taken and saved as photo.jpg")

    # Break the loop with 'q' key
    if key == ord('q'):
        break

# Release resources
cap.release()
out.release()
cv2.destroyAllWindows()
