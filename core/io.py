import RPi.GPIO as GPIO
import time


class IO:
	buzzer = 23
	read_button = 12
	write_button = 26
	read_count = 10

	def __init__(self):
		GPIO.setwarnings(False)
		GPIO.setmode(GPIO.BCM)
		GPIO.setup(self.buzzer, GPIO.OUT)
		GPIO.setup(self.read_button, GPIO.IN)
		GPIO.setup(self.write_button, GPIO.IN)

	def button_beep(self):
		""" One beep for clicking the buttons """
		self._beep()

	def confirm_beep(self):
		""" Two beeps for confirm rfid read/write """
		self._beep(count=2)

	def alarm_beep(self):
		""" Three beeps when rfid data is empty """
		self._beep(count=4)

	def read_buttons(self):
		"""
		Read button states and return specific command
		:return: Command for main script -> read or write
		"""
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
		""" Read state from read button """
		counter = 0
		for loop in range(self.read_count):
			if GPIO.input(self.read_button) == GPIO.HIGH:
				counter += 1
				time.sleep(0.1)
		if counter == self.read_count:			
			self.button_beep()
			return True

	def _write_button_state(self):
		""" Read state from write button """
		counter = 0
		for loop in range(self.read_count):		
			if GPIO.input(self.write_button) == GPIO.HIGH:
				counter += 1
				time.sleep(0.1)			
		if counter == self.read_count:
			self.button_beep()
			return True

	def _beep(self, count=1):
		""" Beep with a buzzer """
		for loop in range(count):
			GPIO.output(self.buzzer, GPIO.HIGH)
			time.sleep(0.1)
			GPIO.output(self.buzzer, GPIO.LOW)
			time.sleep(0.1)
