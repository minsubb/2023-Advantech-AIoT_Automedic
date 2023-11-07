import time
from Data import create_edge_data_from_plag
from Config import generateConfig
import wisepaasdatahubedgesdk.Common.Constants as constant
from wisepaasdatahubedgesdk.EdgeAgent import EdgeAgent as SDKEdgeAgent
from wisepaasdatahubedgesdk.Model.Edge import EdgeAgentOptions, DCCSOptions

class EdgeAgent:
    def __init__(self, options):
        self.sdk_edge_agent = SDKEdgeAgent(options)
        self.sdk_edge_agent.on_connected = self.on_connected
        self.sdk_edge_agent.on_disconnected = self.on_disconnected
        self.sdk_edge_agent.on_message = self.on_message
        self.sdk_edge_agent.connect()

    def on_connected(self, agent, isConnected):
        print("Connected to DataHub.")

    def on_disconnected(self, agent, isDisconnected):
        print("Disconnected from DataHub.")

    def on_message(self, agent, messageReceivedEventArgs):
        print("Message received from DataHub.")

    def sendData(self, plag, device_id, tag_name):
        edgeData = create_edge_data_from_plag(plag, device_id, tag_name)
        self.sdk_edge_agent.sendData(edgeData)
        print(f"Data sent to DataHub: {plag}")

def generate_edgeAgent():
    # DCCS 및 EdgeAgent 설정
    dccsOptions = DCCSOptions(apiUrl='https://api-dccs-ensaas.sa.wise-paas.com/',
                              credentialKey='25648b9f14af17f9b598209a3074d451')
    edgeAgentOptions = EdgeAgentOptions(nodeId='36d582d7-e85a-4131-aaab-012e5512f035',
                                        connectType=constant.ConnectType['DCCS'],
                                        DCCS=dccsOptions)
    edge_agent = EdgeAgent(edgeAgentOptions)
    config = generateConfig()

    # EdgeAgent 설정 업로드
    edge_agent.sdk_edge_agent.uploadConfig(action=constant.ActionType['Create'], edgeConfig=config)

    return edge_agent

# 이 함수는 main.py에서 호출될 것입니다.
def sendDataToDataHub(edge_agent, edge_data):
    # EdgeData 객체를 데이터 허브로 전송합니다.
    edge_agent.sdk_edge_agent.sendData(edge_data)
    print(f"Data sent to DataHub: {edge_data}")