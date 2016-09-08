#!/usr/bin/env python3

import RPi.GPIO as GPIO
import RPimax7219.led as led
from time import sleep
from random import randrange

mx = led.matrix()

button = 17
buzzer = 18

GPIO.setmode(GPIO.BCM)
GPIO.setup(button, GPIO.IN,  pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(buzzer, GPIO.OUT, initial=GPIO.LOW)

def beep():
    GPIO.output(buzzer, GPIO.HIGH)
    sleep(0.1)
    GPIO.output(buzzer, GPIO.LOW)

def rollTheBones(*args):
    rolls = randrange(18, 36)
    number = 0
    for x in range(0, rolls):
        number += 1
        beep()
        mx.letter(0, ord(str(number)))
        sleep(0.01 * x)
        if(number == 9):
            number = 0


GPIO.add_event_detect(button, GPIO.RISING, bouncetime=500)

def main():
    while True:
        if GPIO.event_detected(button):
            rollTheBones()

try:
    main()
except KeyboardInterrupt:
    GPIO.cleanup()
    mx.clear()
