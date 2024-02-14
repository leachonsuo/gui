import cv2
import mediapipe as mp

mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_hands = mp.solutions.hands

cap = cv2.VideoCapture(0)

with mp_hands.Hands(model_complexity=0, min_detection_confidence=0.5, min_tracking_confidence=0.5) as hands:
    while cap.isOpened():
        success, image = cap.read()
        if not success: # 카메라 불러오기 실패일때
            print("Ignoring empty camera frame.") # 메세지 출력
            continue                              # 다시 실행 (12~)

        image.flags.writeable = False
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB) # RGB 색 바꾸기
        results = hands.process(image)

        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        if results.multi_hand_landmarks:
            for hand in results.multi_hand_landmarks:
                mp_drawing.draw_landmarks(
                image,
                hand,
                mp_hands.HAND_CONNECTIONS,
                mp_drawing_styles.get_default_hand_landmarks_style(),
                mp_drawing_styles.get_default_hand_connections_style())

                x1,x2,y1,y2 = 0,0,0,0

                for id, lm in enumerate(hand.landmark):
                    h, w, c = image.shape
                    cx, cy = int(lm.x*w), int(lm.y*h)
                    print(id, " : ", cx , cy)

                    if id == 8:
                        cv2.circle(image, (cx, cy), 20 ,(255,0,0), cv2.FILLED)
                        x1, y1 = cx, cy
                    if id == 12:
                        cv2.circle(image, (cx, cy), 20 ,(255,0,0), cv2.FILLED)
                        x2, y2 = cx, cy

                cv2.rectangle(image, (x1, y1), (x2, y2), (255,0,0), cv2.FILLED)

        cv2.imshow('MediaPipe Hands', cv2.flip(image, 1))

        if cv2.waitKey(5) & 0xFF == 27:
            break
cap.release()