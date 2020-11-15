from RPi import GPIO

from src.logger import logger


def safe_mode():
    actual_mode = GPIO.getmode()
    logger.debug(f"actual_mode {actual_mode}")
    if actual_mode == -1 or actual_mode is None:
        logger.debug(f"safe_mode setting BOARD")
        GPIO.setmode(GPIO.BOARD)

    return actual_mode
