import logging
import AWSIoTPythonSDK
from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient
from __init__ import debug_print

def aws_iot_config(MQTTClient):
    logging.basicConfig()

    # Configurations
    # For TLS mutual authentication
    MQTTClient.configureEndpoint(
        "a3vp0n4b48aqlf-ats.iot.us-east-1.amazonaws.com", 8883)

    # For TLS mutual authentication with TLS ALPN extension
    MQTTClient.configureCredentials("/home/robot/ev3dev/cert/AmazonRootCA1.pem",
                                    "/home/robot/ev3dev/cert/c0f8f9277f-private.pem.key", "/home/robot/ev3dev/cert/c0f8f9277f-certificate.pem.crt")

    # Infinite offline Publish queueing
    MQTTClient.configureOfflinePublishQueueing(-1)
    MQTTClient.configureDrainingFrequency(2)  # Draining: 2 Hz
    MQTTClient.configureConnectDisconnectTimeout(10)  # 10 sec
    MQTTClient.configureMQTTOperationTimeout(5)  # 5 sec
    debug_print('#Config Done')
