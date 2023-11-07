import cv2
from ultralytics import YOLO
from Crash import crash
from collections import deque

video = './dataset/test/cctv.gif'
cap = cv2.VideoCapture(video)

model = YOLO('./model/yolov8n.pt')

previous = []
sending = deque([])
accident_video = []
cnt = 0

def process_frame():
    global previous, sending, accident_video, cnt, cap
    if not cap.isOpened():  # cap 객체가 열려있지 않다면
        cap = cv2.VideoCapture(video)  # cap 객체를 다시 초기화
        if not cap.isOpened():  # 여전히 열리지 않는다면
            return None, None  # None을 반환하여 메인 루프 종료


    ret, frame = cap.read()
    if not ret:
        return None, None  # No more frames or error

    results = model.track(frame, persist=True, verbose=False)
    img = results[0].plot()
    white, previous, is_accident, plag = crash(results[0].boxes, img.shape, previous)

    img = cv2.addWeighted(img, 1, white, 1, 0)

    sending.append([img])

    if is_accident:
        cnt = 1
        accident_video.extend([*sending])
        return img, plag  # Return both img and plag data if accident detected

    FRAME_LEN = 35
    if cnt > 0:
        cnt += 1
        accident_video.append([img])

    if cnt >= FRAME_LEN:
        cnt = 0
        accident_video.clear()

    if len(sending) > FRAME_LEN:
        sending.popleft()

    return img, None  # Return image and None if no accident

if __name__ == "__main__":
    if cap.isOpened():
        while True:
            img, plag = process_frame()

            if plag is not None:
                # Accident detected, process plag data
                print(f"Detected accident, sending plag data: {plag}")
                # Here you would send the plag data to your data.py or wherever it needs to go

            if img is not None:
                cv2.imshow('img', img)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break  # Exit if 'q' is pressed
            else:
                break  # Exit if no more frames to process

    else:
        print("Unable to open camera")

cap.release()
cv2.destroyAllWindows()
