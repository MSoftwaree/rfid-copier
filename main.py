from rpi_lcd import LCD
from core.io import IO
from core.rfid import RFID
import time


lcd = LCD()
io = IO()
rfid = RFID(lcd, io)

lcd.text("Welcome!", 1)
time.sleep(2)

while True:
    lcd.text("Read or write?", 2)

    io_state = io.read_buttons()

    if io_state == "read":
        rfid.read_card()
    elif io_state == "write":
        rfid.write_card()
