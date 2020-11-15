from time import sleep

from src.RfidReader import RfidReader
from src.ServoLock import ServoLock
from src.beep import beep

if __name__ == "__main__":
    allowed_rfid_ids = [512096389334, 588475052768]

    servo = ServoLock()
    servo.lock()
    rfid_reader = RfidReader()

    try:
        while True:
            read_id = rfid_reader.read_card_id()
            print(f"Read id {read_id}, {read_id in allowed_rfid_ids}")
            if read_id in allowed_rfid_ids:
                print("Access allowed!")
                servo.unlock() if servo.locked else servo.lock()
            else:
                print("Access denied!")
                beep(0.5)
            sleep(2)
    except KeyboardInterrupt:
        print("CTRL-C: Terminating program.")
    finally:
        rfid_reader.clean_pin()
