from time import sleep
from RPi import GPIO

from src.logger import logger
from src.safe_mode import safe_mode


def beep(time=0.2, BUZZER_PIN=32):
    logger.debug(f'buzzer pin {BUZZER_PIN}, time {time}')
    safe_mode()
    GPIO.setup(BUZZER_PIN, GPIO.OUT)
    GPIO.output(BUZZER_PIN, GPIO.LOW)
    sleep(time)
    GPIO.cleanup(BUZZER_PIN)
