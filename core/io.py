
import RPi.GPIO as GPIO
import time


class IO:

	def button_test(self):
		GPIO.setwarnings(False)
		GPIO.setmode(GPIO.BCM)
		buzzer = 23
		GPIO.setup(buzzer, GPIO.OUT)
		
		while True:
			GPIO.output(buzzer, GPIO.HIGH)
			print("HIGH")
			time.sleep(0.5)
			GPIO.output(buzzer, GPIO.LOW)
			print("LOW")
			time.sleep(0.5)


io = IO()
io.button_test()
