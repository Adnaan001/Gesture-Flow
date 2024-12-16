import cv2
import numpy as np
import Handtrackingmodule as htm
import time
import autopy
import pyautogui


##########################
wCam, hCam = 640, 480
# frameR = 50 # Frame Reduction
smoothening = 8
#########################

pTime = 0
plocX, plocY = 0, 0
clocX, clocY = 0, 0

cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)
detector = htm.handDetector(maxHands=1)
wScr, hScr = autopy.screen.size()
# print(wScr, hScr)

while True:  
    # 1. Find hand Landmarks
    success, img = cap.read()
    img = detector.findHands(img)
    lmList= detector.findPosition(img)
    # 2. Get the tip of the index and middle fingers
    if len(lmList) != 0:
        x1, y1 = lmList[8][1:]
        x2, y2 = lmList[12][1:]
        # print(x1, y1, x2, y2)

        # 3. Check which fingers are up
        fingers = detector.fingersUp()
        # print(fingers)
        cv2.rectangle(img, (50,50), (wCam -200,hCam - 200),(255, 0, 255), 2)
        # --------------------------------------------------------------------------------
        # 4. Only Index Finger : Moving Mode
        if fingers[1] == 1 and fingers[2] == 0:
            # 5. Convert Coordinates
            x3 = np.interp(x1, (50, wCam - 200), (0, wScr))
            y3 = np.interp(y1, (50, hCam - 200), (0, hScr))
            # 6. Smoothen Values
            clocX = plocX + (x3 - plocX) / smoothening
            clocY = plocY + (y3 - plocY) / smoothening

            # 7. Move Mouse
            autopy.mouse.move(wScr - clocX, clocY)
            cv2.circle(img, (x1, y1), 15, (255, 0, 255), cv2.FILLED)
            plocX, plocY = clocX, clocY
        # ----------------------------------------------------------------------------------
        # ----------------------------------------------------------------------------------
        # 8. Both Index and middle fingers are up : Clicking Mode
        if fingers[1] == 1 and fingers[2] == 1:
            # 9. Find distance between fingers
            length, img, lineInfo = detector.findDistance(8, 12, img)
            print(length)
            # 10. Click mouse if distance short
            if length < 40:
                cv2.circle(img, (lineInfo[4], lineInfo[5]),
                15, (0, 255, 0), cv2.FILLED)
                autopy.mouse.click()
        # -----------------------------------------------------------------------------------

        # ----------------------------------------------------------------------------------
        #if all the fingers are up and wrist is moving from rigth to left new window/tab will open
                # and if from left to right perv tab/window will open
                wristx= lmList[0][1]
                prevw=0
                movement_threshold=20
        if fingers[0]==1 and fingers[1]==1 and fingers[2]==1 and fingers[3]==1 and fingers[4]==1:
            time.sleep(0.5);
            pyautogui.hotkey('alt', 'tab')
        elif fingers[0]==0 and fingers[1]==1 and fingers[2]==1 and fingers[3]==1 and fingers[4]==1:
            time.sleep(0.5);
            pyautogui.hotkey('alt','shift','tab')
        elif fingers[0]==0 and fingers[1]==0 and fingers[2]==1 and fingers[3]==1 and fingers[4]==1:
            time.sleep(0.5);
            pyautogui.hotkey('winleft', 'tab')
        elif fingers[0]==1 and fingers[1]==0 and fingers[2]==0 and fingers[3]==0 and fingers[4]==1:
            time.sleep(0.5);
            pyautogui.hotkey('winleft', 'd')
        elif fingers[0]==0 and fingers[1]==0 and fingers[2]==0 and fingers[3]==0 and fingers[4]==1:
            time.sleep(0.5);
            pyautogui.rightClick();
        elif fingers[0]==1 and fingers[1]==0 and fingers[2]==0 and fingers[3]==0 and fingers[4]==0:
            time.sleep(0.5);
            pyautogui.leftClick();


            # prevw=10
            # prevw2=600
            # wristx=lmList[9][1]
            # if wristx==prevw:
            #     while (wristx>prevw):
            #         if wristx==500:
            #             pyautogui.hotkey('alt','tab')
            #             prevw=10
            #             break;
            #         prevw=wristx
            # elif wristx==prevw2:
            #     while wristx<prevw2:
            #         if wristx==100:
            #             pyautogui.hotkey('alt','shift','tab')
            #             prevw2=650
            #             break;
            #         prevw2=wristx







        # -----------------------------------------------------------------------------------
# # 11. Frame Rate
# cTime = time.time()
# fps = 1 / (cTime – pTime)
# pTime = cTime
# cv2.putText(img, str(int(fps)), (20, 50), cv2.FONT_HERSHEY_PLAIN, 3,
#             (255, 0, 0), 3)
    # 12. Display
    cv2.imshow("Image", img)
    cv2.waitKey(1)
