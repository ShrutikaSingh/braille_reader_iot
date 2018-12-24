from espeak import espeak
import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
s1=11
s2=12
s3=13
s4=15
s5=16
s6=18
GPIO.setup(s1,GPIO.OUT)
GPIO.setup(s2,GPIO.OUT)
GPIO.setup(s3,GPIO.OUT)
GPIO.setup(s4,GPIO.OUT)
GPIO.setup(s5,GPIO.OUT)
GPIO.setup(s6,GPIO.OUT)
espeak.synth('a')
GPIO.output(s1,GPIO.HIGH)
GPIO.output(s2,GPIO.LOW)
GPIO.output(s3,GPIO.LOW)
GPIO.output(s4,GPIO.LOW)
GPIO.output(s5,GPIO.LOW)
GPIO.output(s6,GPIO.LOW)
time.sleep(2)
GPIO.output(s1,GPIO.LOW)
GPIO.output(s2,GPIO.LOW)
GPIO.output(s3,GPIO.LOW)
GPIO.output(s4,GPIO.LOW)
GPIO.output(s5,GPIO.LOW)
GPIO.output(s6,GPIO.LOW)
time.sleep(2)
