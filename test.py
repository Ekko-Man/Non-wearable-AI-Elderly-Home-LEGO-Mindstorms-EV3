import time
from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient
from logs.logger import create_logger
from control import move_ev3


def test_connection_with_AWS():
    myMQTTClient = AWSIoTMQTTClient("ev3")
    myMQTTClient.configureEndpoint("a3vp0n4b48aqlf-ats.iot.us-east-1.amazonaws.com", 8883)
    myMQTTClient.configureCredentials(u"/home/robot/cert/AmazonRootCA1.pem",
                                        u"/home/robot/cert/391ba739a7-private.pem.key",
                                        u"/home/robot/cert/391ba739a7-certificate.pem.crt")
    myMQTTClient.configureOfflinePublishQueueing(-1)
    myMQTTClient.configureDrainingFrequency(2)
    myMQTTClient.configureConnectDisconnectTimeout(10)
    myMQTTClient.configureMQTTOperationTimeout(5)

    def customCallback():
        pass

    myMQTTClient.connect()
    apple = str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) )
    myMQTTClient.publish("myTopic", apple+"myPayload", 0)
    myMQTTClient.subscribe("myTopic", 1, customCallback)
    myMQTTClient.unsubscribe("myTopic")
    myMQTTClient.disconnect()

def test_logger():
    logger = create_logger('test')  # 在 logs 目錄下建立 tutorial 目錄
    logger.info('Start \n')

def test_lego_control():
    move_ev3('move_forword')
    move_ev3('move_backward')
    move_ev3('turn_left')
    move_ev3('turn_right')


if __name__ == "__main__":
    test_connection_with_AWS()
    test_logger()
    test_lego_control()