import socketio

sio = socketio.Client()

@sio.event
def connect():
    print('connection established')


@sio.event
def caca(data):
    print('message received with ', data)
    sio.emit('my response', {'response': 'my response'})

@sio.event
def disconnect():
    print('disconnected from server')

sio.connect('https://635d7aa8.ngrok.io')
print('my sid is', sio.sid)
sio.wait()

