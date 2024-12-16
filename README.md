# Gesture Flow 🌊  
A dynamic application for real-time gesture recognition and tracking, designed to bring a seamless user interaction experience. This project demonstrates the power of machine learning and computer vision in recognizing and interpreting human gestures for controlling the system's interface.

## 🌟 Features  
- **Real-time Gesture Recognition**: Detect and classify gestures using a webcam and computer vision in real-time.  
- **Mouse Control**: Use hand gestures to control the mouse pointer, simulate left/right clicks, and perform scrolling actions.  
- **System Shortcuts**: Trigger system-level shortcuts like opening a new window, switching tabs, or showing the desktop using predefined gestures.  
- **Gesture Mapping**: Includes a variety of gestures to perform common actions like clicking, switching between windows, and controlling the system’s view.  
- **Custom Gesture Training**: Add and train custom gestures for personalized applications (currently in development).  
- **User-Friendly Interface**: Simple and intuitive design for ease of use.  
- **Cross-Platform Support**: Works on major operating systems (Windows, Mac, Linux) with proper configuration.  
- **Expandable Framework**: Modular code structure to add more gestures or integrations effortlessly.  

## ⚙️ How It Works  
This project uses the **OpenCV** library to capture real-time webcam video, along with **MediaPipe** for hand tracking and gesture recognition. Hand landmarks are detected using the `handDetector` class, which processes hand gestures and maps them to actions. The `autopy` and `pyautogui` libraries are used for controlling the mouse cursor and simulating keypresses respectively. 

### Gesture Recognition Flow:
1. **Detecting Hand Landmarks**: The system uses `MediaPipe` to identify the key landmarks of the hand in each frame.
2. **Identifying Finger Positions**: Based on the positions of the fingertips and joints, the system determines the gesture being performed.
3. **Mapping Gestures to Actions**: The detected gestures are mapped to system actions such as moving the mouse, clicking, switching tabs, etc.

## 🤲 Supported Gestures and Actions

| **Gesture**                                      | **Description**                                                      | **Action**                                   |
|--------------------------------------------------|----------------------------------------------------------------------|---------------------------------------------|
| **Index Finger Up**                              | Only the index finger is raised.                                     | Move the mouse cursor.                      |
| **Index and Middle Fingers Up**                  | Both index and middle fingers are raised.                            | Left-click when fingers are brought close together (distance < 40). |
| **All Fingers Up**                               | All five fingers are raised.                                         | Switch to the next window/tab (`Alt + Tab`). |
| **All Fingers Up (Except Thumb)**                | Four fingers raised, thumb down.                                     | Switch to the previous window/tab (`Alt + Shift + Tab`). |
| **Middle, Ring, and Pinky Fingers Up**           | Middle, ring, and pinky fingers raised; index and thumb down.        | Open Task View (`Win + Tab`).               |
| **Thumb and Pinky Fingers Up**                   | Thumb and pinky fingers raised; all other fingers down.              | Show desktop (`Win + D`).                   |
| **Pinky Finger Up**                              | Only the pinky finger is raised.                                     | Perform a right-click.                      |
| **Thumb Up**                                     | Only the thumb is raised.                                            | Perform a left-click.                       |

## 🖥️ System Requirements  
- **Python 3.x**  
- **Required Libraries**:
  - `opencv-python`
  - `mediapipe`
  - `autopy`
  - `pyautogui`
  - `numpy`

## 📌 Contributing  
Feel free to fork the project, create pull requests, or open issues if you want to add new features or improvements.

---

## 📸 Screenshots  

---

