import logging
import json
import time
import sys
import AWSIoTPythonSDK
from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient
from control import move_ev3
from __init__ import debug_print
from config import ELDERLY_ID, IOT_ENDPOINT
from logs.logger import create_logger

logging.basicConfig()

MQTTClient = AWSIoTMQTTClient("ev3dev")

def Callback(client, userdata, message):
    payload = message.payload.decode('utf8').replace("'", '"')
    debug_print("#Received a new message: ", payload)
    debug_print("#From topic: ", message.topic, "\n--------------\n\n")

    js = json.loads(payload)
    status = js['status']
    check_elderly = js['elderly']

    if ELDERLY_ID != check_elderly:
        return

    now_time = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())  #'2009-01-05 22:14:39'
    debug_print('status:  ', status)

    topic = 'iot/ev3/action'

    logger = create_logger('ev3_activity')
    logger.info('Recive Meesage: '+str(payload))

    # action = move_forword, move_backward, turn_left, turn_right
    if status == 'fall down':
        logger.info('Elderly fall down')
        return
    elif status == 'move forward':
        move_ev3('move_forword')
        logger.info('Ev3 move forward')
        return
    elif status == 'move backward':
        move_ev3('move_backward')
        logger.info('Ev3 move backward')
        return
    elif status == 'turn left':
        move_ev3('turn_left')
        logger.info('Ev3 turn left')
        return
    elif status == 'turn right':
        move_ev3('turn_right')
        logger.info('Ev3 turn right')
        return
    else:
        return

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

def publish_to_iot(topic, message):
    MQTTClient.publish(topic, message, 0)

def toAWSIoT(topic):
    aws_iot_config(MQTTClient)
    while True:
        times_to_connect = 0
        try:
            if times_to_connect == 10:
                sys.exit()
            MQTTClient.connect()
            break
        except Exception as e:
            connect_logger = create_logger('Connection')
            connect_logger.info('Start \n')
            connect_logger.error(e)
            debug_print('fail')
            debug_print(e)
            # Stop the internal worker
            MQTTClient._mqtt_core._event_consumer.stop()
            time.sleep(10)
            times_to_connect += 1
            continue

    while True:
        MQTTClient.subscribe(topic, 1, Callback)    #iot/ev3
        debug_print('sleep')
        time.sleep(60)
        alive_time = str(int(time.time()))
        publish_to_iot("iot/ev3/alive", '{"elderly_id":"%s","alive_time":"%s"}'%(str(ELDERLY_ID), alive_time))



if __name__ == "__main__":
    pass
