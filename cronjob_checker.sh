#!/bin/bash
pid_file='/home/robot/ev3dev/test.pid'
if [ ! -s "$pid_file" ] || ! kill -0 $(cat $pid_file) > /dev/null 2>&1; then
  echo $$ > "$pid_file"
  exec /usr/bin/python3.5 /home/robot/ev3dev/test.py
fi