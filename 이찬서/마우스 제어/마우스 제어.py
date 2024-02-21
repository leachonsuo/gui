import pyautogui # pip install pyautogui

"""pyautogui.moveTo(10,30,2) # x,y,time
pyautogui.click()
print(pyautogui.size())"""

import cv2
import mediapipe as mp

mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_hands = mp.solutions.hands

cap = cv2.VideoCapture(0)

with mp_hands.Hands(model_complexity=0,min_detection_confidence=0.5,min_tracking_confidence=0.5) as hands:
    while cap.isOpened():
        success, image = cap.read()
        if not success:  # 카메라를 성공적으로 가져 오지 못하면
            print("Ignoring empty camera frame.")  # 메세지 풀력
            continue                # 위 부터 다시 실행 (12번째 코드 부터)

        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB) # RGB 색 바꾸기
        results = hands.process(image)                 # 인식

        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

        reach = 0
        if results.multi_hand_landmarks:
            
            for hand in results.multi_hand_landmarks:

                x1,y1,x2,y2 = 0,0,0,0
                for id , lm in enumerate(hand.landmark):
                    h,w,c = image.shape
                    
                    cx ,cy = int(lm.x*w) , int(lm.y*h) # cv2 에서 사용할 좌표 정보
                    if id == 6:
                        cv2.circle(image , (cx , cy) , 10 ,(0,0,255) , cv2.FILLED)
                        x1 ,y1 = cx , cy
                    if id == 8:
                        cv2.circle(image , (cx , cy) , 10 ,(255,0,0) , cv2.FILLED)
                        x2 , y2 = cx , cy

                reach = int( ( (x1-x2)**2 + (y1-y2)**2 )**0.5 ) # 두 점 사이 거리

                x1 *= 1920/w
                y1 *= 1080/h

                pyautogui.moveTo(1920-x1, y1)
                if reach <= 27:
                    print(pyautogui.position())
                    pyautogui.click()

        image = cv2.flip(image,1)

        cv2.putText(image, f"dis : {reach} ", (10,45), cv2.FONT_HERSHEY_COMPLEX, 2, (0,0,255), 1)            
        cv2.imshow('MediaPipe Hands', image)

        if cv2.waitKey(5) & 0xFF == 27:
            break
cap.release()