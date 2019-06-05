import datetime

class Item:

    def __init__(self,type,value):
        self.type = type
        self.value = value
        date = datetime.datetime.now()
        self.heure = date.hour



    def __getValue__(self):
        return self.value

    def __getHeure__(self):
        return self.heure

    def __getType__(self):
        return self.type

    def __setValue__(self,value):
        self.value = value

    def __setHeure__(self,heure):
        self.heure=heure

    def __setType__(self,type):
        self.type=type