from time import sleep

from RPi import GPIO

from src.beep import beep
from src.logger import logger
from src.safe_mode import safe_mode


class ServoLock:
    def __init__(self, SERVO_PIN=29, SERVO_MAX_VALUE=10, SERVO_MIN_VALUE=6):
        self.SERVO_PIN = SERVO_PIN
        self.SERVO_MAX_VALUE = SERVO_MAX_VALUE
        self.SERVO_MIN_VALUE = SERVO_MIN_VALUE
        self.locked = None

    def setup_servo_pin(self):
        safe_mode()
        GPIO.setup(self.SERVO_PIN, GPIO.OUT)
        pwm_servo = GPIO.PWM(self.SERVO_PIN, 50)
        pwm_servo.start(0)
        return pwm_servo

    def move_servo(self, value):
        assert type(value) is int
        parsed_value = max(value, self.SERVO_MIN_VALUE)
        parsed_value = min(parsed_value, self.SERVO_MAX_VALUE)
        logger.debug(f'moving servo {self.SERVO_PIN}, value {parsed_value}')

        pwm_servo = self.setup_servo_pin()
        pwm_servo.ChangeDutyCycle(parsed_value)
        sleep(0.3)
        GPIO.cleanup(self.SERVO_PIN)

    def lock(self):
        if not self.locked:
            logger.debug(f"locking servo")
            beep(0.1)
            sleep(0.1)
            beep(0.1)
            self.move_servo(self.SERVO_MIN_VALUE)
            self.locked = True

    def unlock(self):
        if self.locked:
            logger.debug(f"unlocking servo")
            beep(0.1)
            sleep(0.1)
            beep(0.1)
            self.move_servo(self.SERVO_MAX_VALUE)
            self.locked = False
