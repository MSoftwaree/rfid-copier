import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
from rpi_lcd import LCD
import time


class RFID:
	def __init__(self):
		self.reader = SimpleMFRC522()
		self.lcd = LCD()

	def read_card(self):
		try:
			self.lcd.text("Reading...", 1)
			id, text = self.reader.read()
			print(id)
			print(text)
		finally:
			time.sleep(2)
			GPIO.cleanup()
			self.lcd.clear()

	def write_card(self):
		try:
			text = input("New data: ")
			self.lcd.text("Please hold the card", 1)
			self.lcd.text("Writing...", 2)
			self.reader.write(text)
			self.lcd.text("Written", 2)
		finally:
			time.sleep(2)
			GPIO.cleanup()
			self.lcd.clear()


rfid = RFID()

#rfid.write_card()
rfid.read_card()

print("Done")
