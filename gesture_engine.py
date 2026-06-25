class GestureEngine:
    def __init__(self):
        self.WRIST = 0

        # Finger Tip 
        self.INDEX_TIP = 8
        self.MIDDLE_TIP = 12
        self.RING_TIP = 16
        self.PINKY_TIP = 20

        # Knuckles
        self.INDEX_PIP = 6
        self.MIDDLE_PIP = 10
        self.RING_PIP = 14
        self.PINKY_PIP = 18

    def get_gesture(self, hand_landmarks):
        if not hand_landmarks:
            return "NO_HAND"
        
        index_open  = hand_landmarks[self.INDEX_TIP].y  < hand_landmarks[self.INDEX_PIP].y
        middle_open = hand_landmarks[self.MIDDLE_TIP].y < hand_landmarks[self.MIDDLE_PIP].y
        ring_open   = hand_landmarks[self.RING_TIP].y   < hand_landmarks[self.RING_PIP].y
        pinky_open  = hand_landmarks[self.PINKY_TIP].y  < hand_landmarks[self.PINKY_PIP].y

        # Fist 
        if not index_open and not middle_open and not ring_open and not pinky_open:
            return "PLAY_PAUSE"
            
        # Pointing 
        if index_open and not middle_open and not ring_open and not pinky_open:
            # Finger pointing straight up for forwarding video 
            if hand_landmarks[self.INDEX_TIP].y < hand_landmarks[self.WRIST].y - 0.2:
                return "FORWARD"
                
            # Finger pointing left to go backwards in video 
            if hand_landmarks[self.INDEX_TIP].x < hand_landmarks[self.WRIST].x - 0.1:
                return "BACKWARD"
        return "NO_HAND"


