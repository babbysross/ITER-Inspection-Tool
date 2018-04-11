#A program that will hopefully control a motor via a Raspberry Pi Zero W

from tkinter import Frame, Scale, HORIZONTAL, Tk 
import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)
GPIO.setwarnings(False)
pwm = GPIO.PWM(18,100)
pwm.start(5)


master = Tk()
w = Scale(frame, from_=0, to=180, orient=HORIZONTAL, command=self.update)
w.pack()
duty = float(angle) / 10.0 + 2.5
pwm.ChangeDutyCycle(duty)
master.wm_title('Doosan Motor Control')
app = app(master)
master.mainloop()