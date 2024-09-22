
# Face Detection using OpenCV

This project implements a face detection system using OpenCV's `cv2` library in Python. The application detects human faces in real-time using a webcam or from static images via the Haar Cascade Classifier.

## Features

- **Real-time face detection:** Detects faces from webcam input.
- **Image-based detection:** Detects faces in static images.
- **Haar Cascade Classifier:** Uses pre-trained Haar Cascade for frontal face detection.

## Requirements

- Python 3.x
- OpenCV (`cv2`) library

## Installation

1. Clone the repository:

   ```bash
   git clone <repository-url>
   ```

2. Install the required dependencies:

   ```bash
   pip install opencv-python
   ```

## Usage

1. Download the Haar Cascade Classifier XML file from [here](https://github.com/opencv/opencv/blob/master/data/haarcascades/haarcascade_frontalface_default.xml) and save it in your project directory.

2. Run the Python script:

   ```bash
   python face_detection.py
   ```

3. For real-time detection using your webcam:

   ```bash
   python face_detection.py --webcam
   ```

4. To perform detection on a static image:

   ```bash
   python face_detection.py --image <path-to-image>
   ```

## Project Structure

```plaintext
├── face_detection.py    # Main script for face detection
├── haarcascade_frontalface_default.xml    # Haar Cascade Classifier
└── README.md            # Project documentation
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
