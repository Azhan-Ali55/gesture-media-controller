import cv2 
from camera import Camera
from hand_tracker import HandTracker
from yt_controller import YoutubeController
from gesture_engine import GestureEngine

class App:
    def __init__(self):
        self.camera = Camera()
        self.tracker = HandTracker()
        self.controller = YoutubeController()
        self.engine = GestureEngine()

    def run(self):
        # Main loop 
        try:
            while True:
                success, frame = self.camera.get_frame()
                if not success:
                    print("Error! Couldn't read webcam feed")
                    break 

                # Variable to store hand landmarks thorugh frame 
                landmarks = self.tracker.process_frame(frame)

                # Initialize gesture to no hands 
                gesture = "NO_HANDS"
                if landmarks:
                    frame = self.tracker.draw_landmarks(frame, landmarks)
                    gesture = self.engine.get_gesture(landmarks)

                # This sends detetcted gesture to controller that preforms the action 
                self.controller.trigger_action(gesture)

                # Overlay status text on the video frame
                cv2.putText(frame, f"Gesture: {gesture}", (10, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 255), 2)
                
                # Show display window
                cv2.imshow("Hand Gesture Controller Feed", frame)

                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
            
                # Cheks if window is open or not and breaks the loop if not 
                if cv2.getWindowProperty("Hand Gesture Controller Feed", cv2.WND_PROP_VISIBLE) < 1:
                    break
        
        finally:        
            # Clean up resources safely
            self.camera.release()
            self.tracker.release()
            cv2.destroyAllWindows()