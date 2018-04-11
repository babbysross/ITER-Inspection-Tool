#A program that will hopefully control a motor via a Raspberry Pi Zero W

import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)

Motor1A = 18

GPIO.setup(Motor1A,GPIO.OUT)

print("Turning motor on.")
GPIO.output(Motor1A,GPIO.HIGH)
sleep(2)
GPIO.output(Motor1A,GPIO.LOW)
sleep(2)
GPIO.output(Motor1A,GPIO.HIGH)

sleep(2)

print("Stopping motor")
GPIO.output(Motor1A,GPIO.LOW)

GPIO.cleanup()