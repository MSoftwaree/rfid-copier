
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522


class RFID:
	def __init__(self):
		self.reader = SimpleMFRC522()

	def read_card(self):
		try:
			print("Odczytuje!")
			id, text = self.reader.read()
			print(id)
			print(text)
		finally:
			GPIO.cleanup()

	def write_card(self):
		try:
			text = input("New data: ")
			self.reader.write(text)
			print("Written")
		finally:
			GPIO.cleanup()
rfid = RFID()

rfid.write_card()
#rfid.read_card()

print("Po wszystkim")
