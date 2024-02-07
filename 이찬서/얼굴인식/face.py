import cv2
import tkinter as tk
import time
def 카메라():
    print("카메라")
    capture = cv2.VideoCapture(0)
    capture.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

    # 모델 가져오기 
    face_cascade = cv2.CascadeClassifier(".\opencv-master\data\haarcascades\haarcascade_frontalface_default.xml")

    while cv2.waitKey(33) != ord('q'):
        ret, frame = capture.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
        c = len(faces)
        frame = cv2.putText(frame, f"count : {c}", (0, 50), cv2.FONT_HERSHEY_COMPLEX, 2, (255, 255, 255), 3)
        for x,y,w,h in faces:
            frame = cv2.rectangle(frame, (x,y) , (x+w , y+h) , (255, 0, 0), 5, cv2.LINE_8)
        cv2.imshow("VideoFrame", frame)
        
    capture.release()
    cv2.destroyAllWindows()

import tkinter as tk
from tkinter import messagebox

def show_popup():
    popup = tk.Toplevel(window)
    popup.title("자동 닫히는 팝업")
    
    # 팝업 창 내용 추가
    label = tk.Label(popup, text="이 창은 3초 후에 자동으로 닫힙니다.")
    label.pack(padx=20, pady=20)

    # 3000 밀리초(3초) 후에 destroy_popup 함수 호출
    capture = cv2.VideoCapture(0)
    popup.after(3000, lambda: destroy_popup(popup))

def destroy_popup(popup):
    popup.destroy()
    카메라()

# 메인 창 생성
window = tk.Tk()
window.title("Tkinter 자동 닫히는 팝업 예제")

# 버튼 생성
popup_button = tk.Button(window, text="얼굴인식", command=show_popup)
popup_button.pack(pady=20)

# 메인 루프 시작
window.mainloop()