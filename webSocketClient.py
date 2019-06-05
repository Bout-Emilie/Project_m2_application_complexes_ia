import socketio
import item

sio = socketio.Client()

@sio.event
def connect():

    #init IA



    print('connection established')


@sio.event
def smartphone(data):
    data_format = format_data_phone(data)
    print(data_format)
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


def format_data_phone(data):

    label = data.get("label")

    if(label=="Accelerometer"):
        Values = data.get("Values")
        Y = Values.get("y")

        if(Y <= -0):
            value="Laying"
        else:
            value="Standing"

    new_item = item.Item('Acellerometer',value)
    #return data.get("label")
    return new_item



sio.connect('https://6b6cc65c.ngrok.io')
print('my sid is', sio.sid)

#if temps time hours
sio.wait()


