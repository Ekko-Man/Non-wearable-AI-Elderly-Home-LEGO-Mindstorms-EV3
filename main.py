#!/usr/bin/env python3

from iot.toAWS import toAWSIoT
from config import TOPIC

def main():
    toAWSIoT(TOPIC) #iot/ev3

if __name__ == "__main__":
    main()