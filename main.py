import threading

from app import app
from servoAndRfid import runHWCode

if __name__ == '__main__':
    hwThread = threading.Thread(target=runHWCode)
    hwThread.start()

    app.run(threaded=True, host='0.0.0.0')
