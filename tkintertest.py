from tkinter import *
import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)
GPIO.setwarnings(False)
pwm = GPIO.PWM(18,100)
pwm.start(5)

class App:
    def run(self, master):
        master = Tk()
        w1 = Scale(master, from_=0, to=180,
            orient=HORIZONTAL, command=App.update)
        w1.pack()
        angle = w1.get()
    def update(self, angle):
        duty = float(angle) / 10.0 + 2.5
        pwm.ChangeDutyCycle(duty)

root = Tk()
app = App()
App.mainloop()
