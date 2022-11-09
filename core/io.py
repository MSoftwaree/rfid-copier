import RPi.GPIO as GPIO
import time


class IO:
	buzzer = 23
	read_button = 17
	write_button = 27

	def __init__(self):
		GPIO.setwarnings(False)
		GPIO.setmode(GPIO.BCM)
		GPIO.setup(self.buzzer, GPIO.OUT)
		GPIO.setup(self.read_button, GPIO.IN)
		GPIO.setup(self.write_button, GPIO.IN)

	def beep(self, count=1):
		for loop in range(count):
			GPIO.output(self.buzzer, GPIO.HIGH)
			time.sleep(0.1)
			GPIO.output(self.buzzer, GPIO.LOW)
			time.sleep(0.1)

	def read_buttons(self):
		command = None
		while command is None:
			read_state = self._read_button_state()
			write_state = self._write_button_state()

			if read_state is True:
				command = "read"
			elif write_state is True:
				command = "write"

		return command

	def _read_button_state(self):
		if GPIO.input(self.read_button) == GPIO.HIGH:
			return True

	def _write_button_state(self):
		if GPIO.input(self.write_button) == GPIO.HIGH:
			return True
