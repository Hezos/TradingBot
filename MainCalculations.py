import json

def ReadDesignData():
    print("Reading DOE data from file....")
    f = open("InfluenceRationData.txt")
    ratioData = f.read()
    return json.loads(ratioData)

class gModel():
    RSI =  0
    EMA = 0
    SMA = 0
    BBup = 0
    BBdown = 0

def GetActualPrices():
    print("Read actual prices from a file")

#This is not right here
models = []
gen0 = ReadDesignData()
for genom in gen0:
    model = gModel()
    model.RSI = genom[0]
    model.SMA = genom[1]
    model.EMA = genom[2]
    model.BBup = genom[3]
    model.BBdown = genom[4]
    models.append(model)
print("Models were filled with file data.")


ActualsPrices = []


