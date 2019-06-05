import pandas
import csv

import constantes


class Normalize:


    def __init__(self,file,file_normalize):
        self.file=file
        self.file_normalize=file_normalize

    def normalize_one_column(self,data,Xmax,Xmin):
        normalizedData = []
        divisor = Xmax-Xmin
        for i in range(len(data)):
            if(type(data[i])== str):
                data[i]=data[i].replace(',','.')
            print(type(data[i]))
            normalizedData.append(round((float(data[i])-Xmin)/divisor,2))

        return normalizedData


    def normalize(self):
        with open(self.file, newline='', encoding='utf8', errors='ignore') as csvfile:
            data_reader = pandas.read_csv(csvfile)
            electricite = data_reader.Temperature
            lumiere = data_reader.Luminance
            power =data_reader.Power

            electricite_normalized = self.normalize_one_column(electricite,constantes.MaxTemp,constantes.MinTemp)
            lumiere_normalized = self.normalize_one_column(lumiere,constantes.MaxLux,constantes.MinLux)
            power_normalized = self.normalize_one_column(power,constantes.MaxElec,constantes.MinElec)


            data_reader.Temperature = electricite_normalized
            data_reader.Luminance =  lumiere_normalized
            data_reader.Power = power_normalized
            data_reader.to_csv(self.file,index=False)


test=Normalize('iris_training.csv','Iris_normalized.csv')
test.normalize()