# Gesture Media Controller

Control YouTube playback using hand gestures detected through your webcam. No browser extension required.

---

## Gestures

| Gesture | Action |
|---|---|
| Fist | Play / Pause |
| Index finger pointing up | Forward 10s |
| Index finger pointing left | Backward 10s |

---

## Download

Download the latest `main.exe` from the [Releases](https://github.com/Azhan-Ali55/gesture-media-controller/releases) page.

---

## How to Use

1. Download and run `main.exe`
2. Open YouTube in your browser and click the video to focus it
3. Show your hand in front of the webcam
4. Use the gestures above to control playback
5. Press Q or close the webcam window to quit

---

## Requirements

- Windows 10 or 11
- A webcam
- An internet connection on first launch (downloads the hand detection model automatically)

---

## Troubleshooting

**Gestures not working**
Make sure the YouTube tab is focused by clicking the video before gesturing.

**Webcam not opening**
Make sure no other application is using your webcam.

**Windows security warning on launch**
Click "More info" then "Run anyway". This appears because the exe is unsigned.

**App crashes on launch**
Make sure you have an active internet connection — the hand detection model downloads automatically on first run.

---

## Built With

- Python 3.11
- OpenCV
- MediaPipe
- PyAutoGUI
