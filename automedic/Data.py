from wisepaasdatahubedgesdk.Model.Edge import EdgeData, EdgeTag

def create_edge_data_from_plag(plag, device_id, tag_name):
    edge_data = EdgeData()
    edge_tag = EdgeTag(deviceId=device_id, tagName=tag_name, value=str(plag))
    edge_data.tagList.append(edge_tag)
    return edge_data

def receive_plag_data(plag):
    device_id = "Device1"  # Device1이 데이터허브 내 CCTV 디바이스
    tag_name = "TTag1"  # 태그는 Text타입의 TTag1
    edge_data = create_edge_data_from_plag(plag, device_id, tag_name)
    return edge_data
