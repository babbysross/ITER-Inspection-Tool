#A program that will hopefully control a motor via a Raspberry Pi Zero W

from tkinter import Frame, Scale, HORIZONTAL, Tk 
import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)
pwm = GPIO.PWM(18,100)
pwm.start(5)

class App:
    #main application
    def _init_(self,master):
        frame = Frame(master)
        frame.pack()
        scale = Scale(frame, from_=0, to=180,
            orient=HORIZONTAL, command=self.update)
        scale.grid(row=0)

    def update(self, angle):
        duty = float(angle) / 10.0 + 2.5
        pwm.ChangeDutyCycle(duty)

root = Tk()
root.wm_title('Doosan Motor Control')
app = App(root, width=200, height=600)
root.geometry("200x50+0+0")
root.mainloop()