import wisepaasdatahubedgesdk.Common.Constants as constant
from wisepaasdatahubedgesdk.Model.Edge import EdgeData, EdgeTag, EdgeStatus, EdgeDeviceStatus, EdgeConfig, NodeConfig, \
    DeviceConfig, AnalogTagConfig, DiscreteTagConfig, TextTagConfig


def analogTagConfig():
    analog = AnalogTagConfig(name='ATag1',
                             description='ATag1',
                             readOnly=False,
                             arraySize=0,
                             spanHigh=1000,
                             spanLow=0,
                             engineerUnit='',
                             integerDisplayFormat=4,
                             fractionDisplayFormat=2)
    return analog


def discreateTagConfig():
    discrete = DiscreteTagConfig(name='DTag1',
                                 description='DTag1',
                                 readOnly=False,
                                 arraySize=0,
                                 state0='Stop',
                                 state1='Start')
    return discrete


def textTagConfig():
    text = TextTagConfig(name='TTag1',
                         description='TTag1',
                         readOnly=False,
                         arraySize=0)
    return text


def cameraConfig():
    cameraConfig = DeviceConfig(id='Device1',
                                name='CCTV',
                                description='Camera',
                                deviceType='Camera',
                                retentionPolicyName='')

    analog = analogTagConfig()
    discrete = discreateTagConfig()
    text = textTagConfig()

    cameraConfig.analogTagList.append(analog)
    cameraConfig.discreteTagList.append(discrete)
    cameraConfig.textTagList.append(text)
    return cameraConfig


def soundConfig():
    soundConfig = DeviceConfig(id='Device2',
                               name='Sound Sensor',
                               description='Sound Sensor',
                               deviceType='Sound Sensor',
                               retentionPolicyName='')

    analog = analogTagConfig()
    discrete = discreateTagConfig()
    text = textTagConfig()

    soundConfig.analogTagList.append(analog)
    soundConfig.discreteTagList.append(discrete)
    soundConfig.textTagList.append(text)
    return soundConfig


def nodeConfig():
    nodeConfig = NodeConfig(nodeType=constant.EdgeType['Gateway'])
    return nodeConfig


def generateConfig():
    config = EdgeConfig()
    node = nodeConfig()
    config.node = node

    camera = cameraConfig()
    sound = soundConfig()
    config.node.deviceList.append(camera)
    config.node.deviceList.append(sound)

    return config