from time import sleep

from app import sio, servo, rfid_reader
from src.beep import beep
from src.logger import logger


def runHWCode():
    logger.debug("running rfid/servo code")
    allowed_rfid_ids = [512096389334, 588475052768]
    sio.emit("card-read", {"locked": servo.locked})
    servo.lock()

    try:
        while True:
            read_id = rfid_reader.read_card_id()
            logger.debug(f"Read id {read_id}, {read_id in allowed_rfid_ids}")
            if read_id in allowed_rfid_ids:
                logger.debug("Access allowed!")
                sio.emit("card-read", {"locked": not servo.locked})
                servo.unlock() if servo.locked else servo.lock()
            else:
                logger.debug("Access denied!")
                beep(0.5)
            sleep(2)
    except KeyboardInterrupt:
        logger.debug("CTRL-C: Terminating program.")
    finally:
        rfid_reader.clean_pin()
