import cv2
import mediapipe as mp

class HandTracker:
    def __init__(self, max_hands = 1, detection_confidence = 0.7):
        # Initialize Mediapipe hands solution 
        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands(max_num_hands = max_hands, min_detection_confidence = detection_confidence)

        # For drawing the skeleton lines
        self.mp_draw = mp.solutions.drawing_utils

    # Processes the frame and returns raw landmarks if a hand is found
    def process_frame(self, frame):
        # Converts the colors from BGR to RGB 
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = self.hands.process(rgb_frame)

        # Check if hand is detected and return the landmarks of the first detected hand
        if results.multi_hand_landmarks:
            return results.multi_hand_landmarks[0]
        return None

    def draw_landmarks(self, frame, hand_landmarks):
        if hand_landmarks:
            self.mp_draw.draw_landmarks(frame, hand_landmarks, self.mp_hands.HAND_CONNECTIONS)
        return frame
