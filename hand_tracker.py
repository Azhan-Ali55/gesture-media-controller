import cv2
import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision
import urllib.request
import os

class HandTracker:
    MODEL_PATH = "hand_landmarker.task"
    MODEL_URL = "https://storage.googleapis.com/mediapipe-models/hand_landmarker/hand_landmarker/float16/latest/hand_landmarker.task"

    def __init__(self, max_hands = 1, detection_confidence = 0.7):
        # Download model file if not present
        if not os.path.exists(self.MODEL_PATH):
            print("Downloading hand landmark model...")
            urllib.request.urlretrieve(self.MODEL_URL, self.MODEL_PATH)
            print("Download complete.")

        base_options = python.BaseOptions(model_asset_path = self.MODEL_PATH)
        options = vision.HandLandmarkerOptions(base_options = base_options, num_hands = max_hands, min_hand_detection_confidence = detection_confidence)
        self.detector = vision.HandLandmarker.create_from_options(options)

    def process_frame(self, frame):
        # Convert color from BGR to RGB 
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        mp_image = mp.Image(image_format = mp.ImageFormat.SRGB, data = rgb_frame)
        results = self.detector.detect(mp_image)

        # Check if hand is detected and return the landmarks of the first detected hand
        if results.hand_landmarks:
            return results.hand_landmarks[0]
        return None

    def draw_landmarks(self, frame, hand_landmarks):
        if hand_landmarks:
            h, w, _ = frame.shape

            # Define all connections between landmarks
            CONNECTIONS = [
                # Thumb
                (0,1), (1,2), (2,3), (3,4),
                # Index finger
                (0,5), (5,6), (6,7), (7,8),
                # Middle finger
                (0,9), (9,10), (10,11), (11,12),
                # Ring finger
                (0,13), (13,14), (14,15), (15,16),
                # Pinky
                (0,17), (17,18), (18,19), (19,20),
                # Palm
                (5,9), (9,13), (13,17)
            ]

            # Convert landmarks to pixel coordinates
            points = {}
            for i, landmark in enumerate(hand_landmarks):
                cx, cy = int(landmark.x * w), int(landmark.y * h)
                points[i] = (cx, cy)
                # Draw dots
                cv2.circle(frame, (cx, cy), 5, (0, 0, 255), 2)

            # Draw lines between connections
            for start, end in CONNECTIONS:
                cv2.line(frame, points[start], points[end], (0, 255, 0), 3)
        return frame
    
    def release(self):
        self.detector.close()