import socketio

sio = socketio.Client(logger=True, engineio_logger=True)
channel = '2010206354'


@sio.event
def connect():
    print('connection established')
    sio.emit('join', channel)


@sio.on('data')
def on_message(data):
    print('message received with ', data)


@sio.on('Info')
def on_message(info):
    print('message received with ', info)


@sio.event
def disconnect():
    print('disconnected from server')


if __name__ == "__main__":
    sio.connect("http://sockettest.viatomtech.com.cn/")
