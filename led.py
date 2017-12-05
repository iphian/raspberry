import RPi.GPIO as GPIO
import time

led = 16
GPIO.setmode(GPIO.BCM)
GPIO.setup(led,GPIO.OUT)
try:
    while 1:
        GPIO.output(led,1)
        time.sleep(1)
        GPIO.output(led,0)
        time.sleep(1)
except KeyboardInterrupt:
    GPIO.cleanup()
