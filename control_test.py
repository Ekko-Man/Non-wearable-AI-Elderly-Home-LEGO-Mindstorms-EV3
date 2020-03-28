#!/usr/bin/env python3

import sys
import time
# import ev3dev.ev3 as ev3
import threading

from __init__ import debug_print
from ev3dev2.motor import LargeMotor, OUTPUT_A, OUTPUT_D, SpeedPercent, MoveTank
from ev3dev2.sensor import INPUT_1, INPUT_2, INPUT_3
from ev3dev2.sensor.lego import TouchSensor, GyroSensor
from ev3dev2.led import Leds
from ev3dev2.sound import Sound

sound = Sound()
touch_sensor = TouchSensor(INPUT_3) # 3
gyro_sensor = GyroSensor(INPUT_1) # 2
both_motor = MoveTank(OUTPUT_A, OUTPUT_D) # A = Left, D = Right

def turn_left(direction):
    debug_print(direction)
    t = threading.currentThread()
    while getattr(t, "do_run", True):
        both_motor.on_for_seconds(SpeedPercent(0), SpeedPercent(38), 5)

def test_gyro(): #left = negative, right = positive
    debug_print('#Start angle: ', gyro_sensor.angle)
    gyro_sensor.reset()
    debug_print('#After reset: ', gyro_sensor.angle)
    
    # th_turn_left = threading.Thread(target = turn_left, args=('left',))
    # th_turn_left.start()
    
    both_motor.on(0, 5)
    apple = True
    while apple == True:
        debug_print()
    if gyro_sensor.angle == -45:
        # th_turn_left.do_run = False
        # th_turn_left.join()
        both_motor.stop()
        

def change_angle(direction):
    if direction == 'turn':
        both_motor.on_for_seconds(SpeedPercent(0), SpeedPercent(5), 1)
    elif direction == 'left':
        both_motor.on_for_seconds(SpeedPercent(0), SpeedPercent(38), 1)
    elif direction == 'right':
        both_motor.on_for_seconds(SpeedPercent(38), SpeedPercent(0), 1)
    elif direction == 'turn_around':
        both_motor.on_for_seconds(SpeedPercent(38), SpeedPercent(0), 2)
    elif direction == 'move':
        both_motor.on_for_seconds(SpeedPercent(38), SpeedPercent(38), 1)
    else:
        debug_print('fill wrong direction')

def video_demo(re):
    if re == 're':
        change_angle('turn_around')
        both_motor.on_for_rotations(SpeedPercent(50), SpeedPercent(50), 4)
        change_angle('right')
        both_motor.on_for_rotations(SpeedPercent(50), SpeedPercent(50), 4)
        change_angle('turn_around')
        return
    both_motor.on_for_rotations(SpeedPercent(50), SpeedPercent(50), 4)
    change_angle('left')
    both_motor.on_for_rotations(SpeedPercent(50), SpeedPercent(50), 4)

def touchsensor_hit():
    if touch_sensor.is_pressed:
        return True
    else:
        return False

def test_hit_something():
    apple = True
    while apple:
        both_motor.on_for_rotations(SpeedPercent(50), SpeedPercent(50), 1)
        if touchsensor_hit():
            apple = False
    debug_print('Pub: Safe Continune')



# ---------------------------
# from ev3
# def lego_speak(text = str):
#     ev3.Sound.speak(text)

# def run_by_second():
#     motor_L = ev3.LargeMotor('outA')
#     motor_R = ev3.LargeMotor('outD')
#     motor_L.run_timed(time_sp=3000, speed_sp=500)




#---------------------------------------

# def sensor_function():
#     if sensor == ok:
#         return True
#     else:
#         return False


# def run():
#     apple = True
#     while sensor_function() and apple:
#         lego run 
#         apple = False
#     pub.(done)

# Pi
# def aa(json):
#     if json == done:
#         check cam
#         sub.run

