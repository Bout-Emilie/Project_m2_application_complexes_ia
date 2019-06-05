import os
import csv

#Constantes température
MaxTemp = int(30)
MinTemp = int(13)

#Constantes Lux
MaxLux = int(33000)
MinLux = int(0)

#Constantes accéléromètre

#Constantes electriques
MaxElec = int(2500)
MinElec = int(0)

def normalizeElec(dataElecList):
    normalizedElecList = []
    Xmax = MaxElec
    Xmin = MinElec
    divisor = Xmax-Xmin
    for i in range(len(dataElecList)):
        normalizedElecList.append(round((dataElecList[i]-Xmin)/divisor,2))
    # print("Liste conso elec normalisee : \n")
    # print(normalizedElecList)
    # print("\n")
    return normalizedElecList


def normalizeLux(dataLuxList):
    normalizedLuxList = []
    Xmax = MaxLux
    Xmin = MinLux
    divisor = Xmax-Xmin
    for i in range(len(dataLuxList)):
        normalizedLuxList.append(round((dataLuxList[i]-Xmin)/divisor,2))

    # print("Liste luminance normalisee : \n")
    # print(normalizedLuxList)
    # print("\n")
    return normalizedLuxList

def normalizeTemp(dataTempList):
    normalizedTempList = []
    Xmax = MaxTemp
    Xmin = MinTemp
    divisor = Xmax-Xmin
    for i in range(len(dataTempList)):
     normalizedTempList.append(round((dataTempList[i]-Xmin)/divisor,2))


    # print("Liste temperatures normalisee : \n")
    # print(normalizedTempList)
    # print("\n")
    return normalizedTempList

def writeInCsv(normalizedTempList, normalizedLuxList, normalizedElecList):
    with open('Iris_normalized.csv', 'w', newline='') as csvfile:
        data_writer = csv.writer(csvfile)
        for i in range(len(normalizedTempList)):
            data_writer.writerow([normalizedTempList[i], normalizedLuxList[i], normalizedTempList[i]])


def main():
    dataList = []
    dataTempList = []
    dataLuxList = []
    dataElecList = []
    with open('Iris.csv', newline='', encoding='utf8', errors='ignore') as csvfile:
        data_reader = csv.reader(csvfile, delimiter=';', quotechar='|')
        next(data_reader)
        
        # On passe dans un tableau les valeurs du csv
        for data in data_reader:
            dataList.append(data)

        # On attribue a chacune des liste les bonnes valeurs
        for i in range(len(dataList)):
            dataTempList.append(float(dataList[i][0]))
            dataLuxList.append(float(dataList[i][1]))
            dataElecList.append(float(dataList[i][2]))
    # print(dataTempList)
    # print(dataLuxList)
    writeInCsv(normalizeTemp(dataTempList), normalizeLux(dataLuxList), normalizeElec(dataElecList))



main()