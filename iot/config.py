import logging
import AWSIoTPythonSDK
from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient
from __init__ import debug_print
from config import IOT_ENDPOINT

def aws_iot_config(MQTTClient):
    logging.basicConfig()

    # Configurations
    # For TLS mutual authentication
    debug_print(IOT_ENDPOINT)
    MQTTClient.configureEndpoint(IOT_ENDPOINT, 8883)

    # For TLS mutual authentication with TLS ALPN extension
    MQTTClient.configureCredentials(u"/home/robot/cert/AmazonRootCA1.pem",
                                    u"/home/robot/cert/391ba739a7-private.pem.key",
                                    u"/home/robot/cert/391ba739a7-certificate.pem.crt")

    # Infinite offline Publish queueing
    MQTTClient.configureOfflinePublishQueueing(-1)
    MQTTClient.configureDrainingFrequency(2)  # Draining: 2 Hz
    MQTTClient.configureConnectDisconnectTimeout(10)  # 10 sec
    MQTTClient.configureMQTTOperationTimeout(5)  # 5 sec


    debug_print('#Config and Connected to AWS IoT')

    MQTTClient.connect()
