import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setup(23,GPIO.OUT)
GPIO.setup(15,GPIO.OUT)
while True:
	n = input("enter a password")
	if n == 'simon':
		GPIO.output(23,0)
		print("password correct")
		GPIO.output(15,0)
		time.sleep(5)
		GPIO.output(23,1)
	else:
		GPIO.output(23,1)
		time.sleep(.5)
		print("incorrect password")
		GPIO.output(15,1)
		time.sleep(.5)
		GPIO.output(15,0)
		time.sleep(.5)
		GPIO.output(15,1)
		time.sleep(.5)
		GPIO.output(15,0)
		time.sleep(.5)
		GPIO.output(15,1)
		time.sleep(.5)
		GPIO.output(15,0)
		time.sleep(.5)
		GPIO.output(15,1)
		time.sleep(.5)
		GPIO.output(15,0)
		time.sleep(.5)
		GPIO.output(15,1)
		time.sleep(.5)
		GPIO.output(15,0)
		time.sleep(.5)
		GPIO.output(15,1)
		time.sleep(.5)
		GPIO.output(15,0)
		time.sleep(.5)
