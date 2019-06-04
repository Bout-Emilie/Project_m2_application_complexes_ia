import socketio

sio = socketio.Client()

@sio.event
def connect():
    print('connection established')


@sio.event
def smartphone(data):
    print('message received with smartphone ', data)


@sio.event
def eye(data):
    print('message received with eye ', data)


@sio.event
def wallplug(data):
    print('message received with  wallplug', data)


@sio.event
def disconnect():
    print('disconnected from server')

sio.connect('https://635d7aa8.ngrok.io')
print('my sid is', sio.sid)
sio.wait()


