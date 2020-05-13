#!/usr/bin/env python3
from time import sleep, time
from __init__ import debug_print

from ev3dev2.motor import LargeMotor, OUTPUT_A, OUTPUT_D, SpeedPercent, MoveTank
from ev3dev2.sensor.lego import TouchSensor, GyroSensor, UltrasonicSensor
from ev3dev2.sensor import INPUT_1, INPUT_2, INPUT_3


gyro_sensor = GyroSensor(INPUT_1) # 2
sonic_sensor = UltrasonicSensor(INPUT_2) 
touch_sensor = TouchSensor(INPUT_3) # 3

gyro_sensor.mode='GYRO-ANG'
sonic_sensor.mode='US-DIST-CM'

# Attach large motors to ports B and C
mA = LargeMotor('outA')
mD = LargeMotor('outD')

def touchsensor_hit():
    if touch_sensor.is_pressed:
        return True
    else:
        return False

def move_ev3(action):   # action = move_forword, move_backward, turn_left, turn_right
    try:
        if action == 'move_forword':
            speed = 360
        elif action == 'move_backward':
            speed = -360
        else:
            speed = 100

        t_end = time() + 1
        if action != 'turn_left':
            mA.run_forever(speed_sp=speed)
        if action != 'turn_right':
            mD.run_forever(speed_sp=speed)

        if action == 'move_forword' or 'move_backward':
            while sonic_sensor.value() > 200 and not touchsensor_hit() and time() < t_end:
                sleep(0.005)
            else:
                if sonic_sensor.value() < 200:
                    debug_print('Detected something in front of the robot during moving.')
                    return
                if touchsensor_hit():
                    debug_print("Robot hit something during moving")
                    return
        else:
            gyro_sensor.reset()
            while sonic_sensor.value() > 200 and not touchsensor_hit() and gyro_sensor.value() < 15:
                sleep(0.005)
            else:
                if sonic_sensor.value() < 200:
                    debug_print('Detected something in front of the robot during moving.')
                    return
                if touchsensor_hit():
                    debug_print("Robot hit something during moving")
                    return

        if action != 'turn_left':
            mA.stop(stop_action="brake")
        if action != 'turn_right':
            mD.stop(stop_action="brake")
    except:
        debug_print('fill wrong action')