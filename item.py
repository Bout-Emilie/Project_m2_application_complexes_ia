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

    def __getType(self):
        return self.type

    def __setValue(self,value):
        self.value = value

    def __setHeure(self,heure):
        self.heure=heure

    def __setType(self,type):
        self.type=type