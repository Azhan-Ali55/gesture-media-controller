import pyautogui
import time 

# Prevent pyautogui from throwing an error if mouse hits screen corner
pyautogui.FAILSAFE = False

class YoutubeController:
    def __init__(self, cooldown_sec = 1.5):
        self.cooldown = cooldown_sec
        self.last_trigger_time = 0
        self.last_gesture = None # To avoid repetition 

        # Mapping action buttons 
        self.action_map = {
            # This is for youtube only as these are the buttons that work for youtube 
            "PLAY_PAUSE": "k", 
            "FORWARD": "l",
            "BACKWARD": "j",
        }

    def trigger_action(self, gesture):
        if gesture not in self.action_map:
            return False
        
        current_time = time.time()
        if current_time - self.last_trigger_time >= self.cooldown:
            key_to_press = self.action_map[gesture]
            print(f"[ACTION] Gesture '{gesture}' → key '{key_to_press}'")

            if "+" in key_to_press:
                keys = key_to_press.split("+")
                pyautogui.hotkey(*keys)
            else:
                pyautogui.press(key_to_press)

            self.last_trigger_time = current_time
            self.last_gesture = gesture
            return True
        return False

