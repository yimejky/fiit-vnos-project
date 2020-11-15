from RPi import GPIO
from src.logger import logger
from src.mfrc522 import SimpleMFRC522


# we used our changed version of simple mfrc522 reader library https://github.com/pimylifeup/MFRC522-python
class RfidReader:
    def __init__(self, RFID_PIN=37):
        self.RFID_PIN = RFID_PIN
        self.reader = SimpleMFRC522(bus=1,
                                    device=0,
                                    pin_mode=GPIO.BOARD,
                                    pin_rst=self.RFID_PIN,
                                    debugLevel="NOTSET")

    def read_card_id(self):
        logger.debug("reading card")
        id = self.reader.read_id()
        logger.debug(f"id {id}")
        return id

    def clean_pin(self):
        logger.debug(f"rfid cleaning pin {self.RFID_PIN}")
        GPIO.cleanup(self.RFID_PIN)
