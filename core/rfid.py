from mfrc522 import SimpleMFRC522
import RPi.GPIO as GPIO
import time


class RFID:
	def __init__(self, lcd):
		self.reader = SimpleMFRC522()
		self.lcd = lcd
		self.data = None

	def read_card(self):
		try:
			self.lcd.text("Reading...", 1)
			_, self.data = self.reader.read()
			self.lcd.text("Read", 1)
		finally:
			time.sleep(2)
			GPIO.cleanup()
			self.lcd.clear()

	def write_card(self):
		if self.data is None:
			self.lcd.text("No data read!", 1)
			time.sleep(2)
			return False
		try:
			self.lcd.text("Hold the card", 1)
			self.lcd.text("Writing...", 2)
			self.reader.write(self.data)
			self.lcd.clear()
			self.lcd.text("Written", 1)
		finally:
			time.sleep(2)
			GPIO.cleanup()
			self.lcd.clear()
