from Vision import process_frame
from Data import receive_plag_data
from EdgeAgent import generate_edgeAgent, sendDataToDataHub

def main():
    edge_agent = generate_edgeAgent()  # EdgeAgent 인스턴스 생성 및 설정

    while True:
        img, plag = process_frame()  # img와 plag 혹은 img와 None을 받음

        if img is None and plag is None: # img, plag 둘 다 None이면 영상이 끝난것이니 종료
            print("No more frames to process or unable to open video. Exiting.")
            break

        if plag is not None: # plag가 None이 아닌 것이 리턴된거면 is_accident이니 처리
            # 사고가 감지되었을 때 처리
            print(f"Accident detected, processing plag data: {plag}") # 요 출력문 나오면서 plag 처리함
            edge_data = receive_plag_data(plag)  # Data.py를 통해 EdgeData로 변환
            sendDataToDataHub(edge_agent, edge_data)  # 변환된 EdgeData를 EdgeAgent.py를 통해 데이터 허브로 전송

if __name__ == "__main__":
    main()
