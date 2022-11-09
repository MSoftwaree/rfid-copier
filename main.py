from rpi_lcd import LCD
from core.io import IO
from core.rfid import RFID


lcd = LCD()
io = IO()
rfid = RFID(lcd)

lcd.text("Welcome!", 1)

while True:
    lcd.text("Read or write?", 2)

    io_state = io.read_buttons()

    if io_state == "read":
        rfid.read_card()
    elif io_state == "write":
        rfid.write_card()
        