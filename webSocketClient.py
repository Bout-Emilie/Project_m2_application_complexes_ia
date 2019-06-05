import socketio
import item
import poc
import normalize
import constantes

sio = socketio.Client()
last_once = {
    'Heure': [1],
    'Temperature': [0.5],
    'Burglar': [1],
    'Power': [0.00],
    'Luminance': [0.00],
    'Sensor': [0],
}

#file_training = normalize.Normalize(constantes.data_training)
#file_training.normalizer()

#file_test = normalize.Normalize(constantes.data_test)
#file_test.normalizer()

ia = poc.Tensor("Alerte", constantes.data_training, constantes.data_test)
ia.train(100, 1000)

@sio.event
def connect():

    ##Init IA
    print('connection established')


@sio.event
def smartphonee(data):
    data_format = format_data_phone(data)
    print(data_format)
    print('message received with smartphone ', data)


@sio.event
def eye(data):
    new_item = format_data_eye(data)
    if new_item is not None:
        new=[]
        print(new_item.__getValue__())
        print(new_item.__getType__())
        value = new_item.__getValue__()
        type = new_item.__getType__()
        new.append(value)
        last_once[type] =  new
        print(last_once)
        res_ia = ia.predict(last_once,100)
        print(res_ia)

    print('message received with eye ', data)




@sio.event
def wallpluge(data):
    print('message received with  wallplug', data)


@sio.event
def disconnect():
    print('disconnected from server')


def format_data_phone(data):

    label = data.get("label")

    standing = 1
    if(label=="Accelerometer"):

        values = data.get("values")
        y = values.get("y")

        if(y <= -0 ):
             standing = 0

        print(standing)

    new_item = item.Item("Accelerometre",standing)
    return new_item


def format_data_eye(data):

    label = data.get("label")
    value = 0
    sauv = 1



    if(label == "Burglar"):
           valeur = data.get("value")
           print(valeur)
           if(valeur != 0):
                value = 1
           sauv =0

    if(label == "Sensor"):
        valeur = data.get("value")
        print('test')
        if(valeur == "True"):
            value = 1
            sauv =0

    if(label =="Luminance"):
        value =  data.get("value")
        value = normalizer(constantes.MaxLux,constantes.MinLux,int(value))
        sauv = 0

    if(label == "Temperature"):
        value =  data.get("value")
        value = normalizer(constantes.MaxTemp, constantes.MinTemp, int(value))
        sauv = 0

    if(sauv == 0):
     new_item = item.Item(label,value)
     return new_item



def format_data_waal_plug(data):

    label = data.get("label")

    if(label == "Power"):

        diff = int(data.get("preValue")) - int(data.get("value"))
        diff= abs(diff)

        if(diff > 2):
            value = data.get("value")
            new_item = item.Item(label,value)

    return new_item


def normalizer(XMax,XMin,data):

    divisor = XMax - XMin
    res = round((data - XMin) / divisor,2)
    return res


def main():

    sio.connect(constantes.URI)
    print('my sid is', sio.sid)



if __name__ == '__main__':
    main()
