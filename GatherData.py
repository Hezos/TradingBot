#This file was created to copy data from tradinview.com by hand and then do calculations with that data
import pandas as pd
from sklearn import linear_model
import json
import random

class StockInfo:
        SandPdirection = 0
        beta = 0
        suggestion = 'n'
        isnewsaffected = 'n'
        currentprice = 0
        linearregressionslope = 0
        leastsquaresmovingaveragedirection = 0
        linearregressionaccuarity = 0
        closestsupportlevel = 0
        fiftytwoweeklow = 0
        SMAcross = 'n'
        RSI = 0
        MACDline = 0
        MACDsignal = 0
        bollingerbands = 0
        EMA = 0
        def __str__(self):
            return json.dump(self)

    
class Refined: 
    SandP = 0
    analystrating = 0
    affected = 0
    linearregslope = 0
    linearregline = 0
    levelsupport = 0
    movingaveragecross = 0
    relativestrength = 0
    MACDcross = 0
    bollinger = 0
    EMAsign = 0


'''
samples = int(input("How many samples do you want to register?\n"))


infos = []
for i in range(0, samples):
    info = StockInfo()
    info.SandPdirection = float(input("The direction of the S&P500\n"))
    info.beta = float(input("The beta of the stock:\n"))
    info.suggestion = input("Did analysts suggest buying? (y/n)\n")
    info.isnewsaffected = input("Did you read any news for this day? Yes or no? (y/n)\n")
    info.currentprice = float(input("The stock price:\n"))
    info.linearregressionslope = float(input("The direction of the linear regression slope (The higher number the higher the accelaration):\n"))
    info.leastsquaresmovingaveragedirection = float(input("The least squares moving average direction with value:\n"))
    info.linearregressionaccuarity = float(input("The accuarity of the linear regression:\n"))
    info.closestsupportlevel = float(input("The closest support level:\n"))
    info.fiftytwoweeklow = float(input("The 52 week low:\n"))
    info.SMAcross = input("Did the SMA200and50 cross?\n")
    info.RSI = float(input("The RSI value:\n"))
    info.MACDline = float(input("MACD line value:\n"))
    info.MACDsignal = float(input("MACD signal value:\n"))
    info.bollingerbands = float(input("The lower bollinger bands' value:\n"))
    info.EMA = []
    print("The last 5 EMA values:")
    for i in range(0,5):
        info.EMA.append(float(input("EMA value here:\n")))
    infos.append(info)

refineds = []
for info in infos:
    ref = Refined()
    ref.SandP = 0
    #Use DOE (Design Of Experiments later to correct the numbers which were embeded here)
    if info.SandPdirection < 0 and info.beta > 0.4:
        print("Not woth buying.")
        break
    else:
        ref.SandP = info.SandPdirection * info.beta * 10 #Change 10 later

    ref.analystrating = 0
    ref.affected = 0
    if info.suggestion == 'y':
        ref.analystrating = 10
    else:
        ref.analystrating = -10

    if info.isnewsaffected == 'y':
        ref.affected = -10
    else:
        ref.affected = 0

    ref.linearregslope = info.linearregressionslope * -1
    ref.linearregline = info.leastsquaresmovingaveragedirection * info.linearregressionaccuarity
    #Sidenote: What if the price is under the support level? Maybe don't count with that factor?????????
    ref.levelsupport = (info.currentprice - info.closestsupportlevel) * -1 - (info.currentprice - info.fiftytwoweeklow) * -1
    ref.movingaveragecross = 0
    if info.SMAcross == 'y':
        ref.movingaveragecross = 10
    else:
        ref.movingaveragecross = 0

    ref.relativestrength = info.RSI * -1
    ref.MACDcross = abs(info.MACDsignal-info.MACDline) * -1
    ref.bollinger = (info.currentprice - info.bollingerbands) * -1

    #using patterns for EMA: LHLHH LLHHH
    ref.EMAsign = 0
    if info.EMA[0] < info.EMA[1] and info.EMA[1] > info.EMA[2] and info.EMA[2] < info.EMA[3] and info.EMA[3] < info.EMA[4]:
        ref.EMAsign = 10
    elif info.EMA[0] > info.EMA[1] and info.EMA[1] > info.EMA[2] and info.EMA[2] < info.EMA[3] and info.EMA[3] < info.EMA[4]:
        ref.EMAsign = 10
    else:
        break
    
    refineds.append(ref)
'''

refinds = []

for i in range(0, 3):
    #testing class conversion to dataframe:
    myrefind = Refined()
    myrefind.SandP = random.randrange(1,10)
    myrefind.analystrating = random.randrange(1,20)
    myrefind.affected = random.randrange(1,25)
    myrefind.linearregslope = random.randrange(1,40)
    myrefind.linearregline = random.randrange(1,5)
    myrefind.levelsupport = random.randrange(1,31)
    myrefind.movingaveragecross = random.randrange(1,53)
    myrefind.relativestrength = random.randrange(1,24)
    myrefind.MACDcross = random.randrange(1,14)
    myrefind.bollinger = random.randrange(1,15)
    myrefind.EMAsign = random.randrange(1,62)
    refinds.append(myrefind)


'''
data = pd.DataFrame(data= myrefind.__dict__, index=[0,1,2,3,4,5])
print(data)
'''

dataDictionaries = []
for item in refinds:
    dataDictionaries.append(item.__dict__)

#index is just a placeholder to have an index field.
data = pd.DataFrame(data= dataDictionaries, index=[0,1,2])
print(data)
regression = linear_model.LinearRegression()

y=pd.DataFrame(data=[random.randrange(1,10),random.randrange(1,10),random.randrange(1,10)], index=[0,1,2])
regression.fit(data,y)

print(regression.coef_)
randoms = []
for i in range(0, 11):
    randoms.append(random.randrange(0,30))
print(regression.predict([randoms]))

print("Linear regression samples have been created.")
