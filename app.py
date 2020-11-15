import socketio
from flask import Flask
from flask_cors import CORS, cross_origin

from src.RfidReader import RfidReader
from src.ServoLock import ServoLock
from src.logger import logger

servo = ServoLock()
rfid_reader = RfidReader()

sio = socketio.Server(cors_allowed_origins='*', async_mode='threading')
app = Flask(__name__)
cors = CORS(app)
app.wsgi_app = socketio.Middleware(sio, app.wsgi_app)

app.config['SECRET_KEY'] = 'secret!'


@app.route("/")
def index():
    return app.send_static_file('./index.html')


@sio.event
def connect(sid, environ):
    logger.debug(f'connection established {sid}')
    sio.emit("card-read", {"locked": servo.locked})
