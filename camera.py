import cv2 

class Camera: 
    def __init__(self, camera_index = 0):
        # Initialize the webcam 
        self.cap = cv2.VideoCapture(camera_index)

    def get_frame(self):
        # Captures a frame, then mirrors it for intuitive use.
        success, frame = self.cap.read()
        if not success:
            return False, None
    
        # Flip the camera horizontally so that you left hand shows on the left side of the screen 
        frame = cv2.flip(frame, 1)
        return True, frame

    def release(self):
        # Releases the resoureces after app is closed 
        self.cap.release() 


