import RPi.GPIO as GPIO
import time


class IO:
	buzzer = 23

	def __init__(self):
		GPIO.setwarnings(False)
		GPIO.setmode(GPIO.BCM)
		GPIO.setup(self.buzzer, GPIO.OUT)

	def beep(self):
		GPIO.output(self.buzzer, GPIO.HIGH)
		time.sleep(0.1)
		GPIO.output(self.buzzer, GPIO.LOW)

	def double_beep(self):
		for loop in range(2):
			self.beep()
			time.sleep(0.1)


io = IO()
io.double_beep()
