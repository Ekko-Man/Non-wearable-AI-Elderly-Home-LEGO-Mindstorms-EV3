import logging
import json
import time
import AWSIoTPythonSDK
from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient
from iot.config import aws_iot_config
from control import move_ev3
from __init__ import debug_print
from config import ELDERLY_ID

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

    # action = move_forword, move_backward, turn_left, turn_right
    if status == 'pk':
        topic = 'iot/ev3'
        pub_message = '{"time": %s ,"elderly": %s ,"status": "recive elderly pk"}' % (now_time, ELDERLY_ID)
        publish_to_iot(topic, pub_message)
        return
    elif status == 'move forward':
        move_ev3('move_forword')
        pub_message = '{"time": %s ,"elderly": %s ,"status": "move forward"}' % (now_time, ELDERLY_ID)
        publish_to_iot(topic, pub_message)
        return
    elif status == 'move backward':
        move_ev3('move_backward')
        pub_message = '{"time": %s ,"elderly": %s ,"status": "move backward"}' % (now_time, ELDERLY_ID)
        publish_to_iot(topic, pub_message)
        return
    elif status == 'turn left':
        move_ev3('turn_left')
        pub_message = '{"time": %s ,"elderly": %s ,"status": "turn left"}' % (now_time, ELDERLY_ID)
        publish_to_iot(topic, pub_message)
        return
    elif status == 'turn right':
        move_ev3('turn_right')
        pub_message = '{"time": %s ,"elderly": %s ,"status": "turn right"}' % (now_time, ELDERLY_ID)
        publish_to_iot(topic, pub_message)
        return

def toAWSIoT(topic):
    aws_iot_config(MQTTClient)
    # while True:
    #     try:
    #         MQTTClient.connect()
    #         break
    #     except Exception as e:
    #         debug_print('fail')
    #         debug_print(e)
    #         # Stop the internal worker
    #         MQTTClient._mqtt_core._event_consumer.stop()
    #         time.sleep(10)
    #         continue

    while True:
        MQTTClient.subscribe(topic, 1, Callback)
        debug_print('sleep')
        time.sleep(2)
        publish_to_iot(topic, '{"elderly": 12345,"status": "pk"}')

    MQTTClient.unsubscribe(topic)
    MQTTClient.disconnect()

def publish_to_iot(topic, message):
    MQTTClient.publish(topic, message, 0)

if __name__ == "__main__":
    pass
