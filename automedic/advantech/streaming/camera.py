import cv2

# 영상을 저장된 파일로 송출
video = './dataset/test/cctv.gif'
video_path = "C:/Users/son-hyunho/Desktop/Advantech AIoT/code/2023_Advantech_AIoT/Computer_Vision/dataset/test/cctv.gif"

cap = cv2.VideoCapture(video_path)


# 영상을 컴퓨터 캠으로 송출
# cap = cv2.VideoCapture(0)

def get_stream_video():
    if cap.isOpened():
        while True:
            ret, frame = cap.read()

            if not ret:
                break
            else:
                ret, buffer = cv2.imencode('.jpg', frame)

                frame = buffer.tobytes()

                yield (b'--frame\r\n' b'content-Type: image/jpeg\r\n\r\n' +
                       bytearray(frame) + b'\r\n')
                if cv2.waitKey(100) & 0xFF == ord('q'):
                    break
    else:
        print("unable to use camera")