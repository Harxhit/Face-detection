import cv2

# Use the full path to the Haar Cascade XML file
file = cv2.CascadeClassifier(r"C:\Users\Welcome\OneDrive\Desktop\Python\Projects\Face Detection\haarcascade_frontalface_default.xml")

# Check if the file was loaded properly
if file.empty():
    print("Error: Failed to load cascade file")
    exit()

# Initialize the webcam
video = cv2.VideoCapture(0)

# Check if the webcam was opened successfully
if not video.isOpened():
    print("Error: Failed to open video source")
    exit()

while True:
    # Read a frame from the webcam
    ret, image = video.read()

    # Check if the frame was captured successfully
    if not ret:
        print("Error: Failed to capture image")
        break

    # Convert to grayscale for face detection
    color = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Detect faces in the image (experiment with parameters here)
    fo = file.detectMultiScale(color, scaleFactor=1.1, minNeighbors=4, minSize=(30, 30))

    # Draw rectangles around detected faces
    for (x, y, w, h) in fo:
        cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2)

    # Show the video with face detection
    cv2.imshow("Video", image)

    # Break the loop when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and close windows
video.release()
cv2.destroyAllWindows()
