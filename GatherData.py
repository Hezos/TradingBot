#This file was created to copy data from tradinview.com by hand and then do calculations with that data
import pandas as pd
from sklearn import linear_model

samples = int(input("How many samples do you want to register?\n"))

class StockInfo:
    def __init__(self, SandPdirection, beta, suggestion, isnewsaffected, currentprice, linearregressionslope, leastsquaresmovingaveragedirection,
        linearregressionaccuarity, closestsupportlevel, fiftytwoweeklow, SMAcross, RSI, MACDline, MACDsignal, bollingerbands, EMA):
        this.SandPdirection = SandPdirection
        this.beta = beta
        this.suggestion = suggestion
        this.isnewsaffected = isnewsaffected
        this.currentprice = currentprice
        this.linearregressionslope = linearregressionslope
        this.leastsquaresmovingaveragedirection = leastsquaresmovingaveragedirection
        this.linearregressionaccuarity = linearregressionaccuarity
        this.closestsupportlevel = closestsupportlevel
        this.fiftytwoweeklow = fiftytwoweeklow
        this.SMAcross = SMAcross
        this.RSI = RSI
        this.MACDline = MACDline
        this.MACDsignal = MACDsignal
        this.bollingerbands = bollingerbands
        this.EMA = EMA

class Refined:
    def __init__(self, SandP, analystrating, affected, linearregslope, linearregline, levelsupport, movingaveragecross, relativestrength, MACDcross, bollinger,
         EMAsign):
        this.SandP = SandP
        this.analystrating = analystrating
        this.affected = affected
        this.linearregslope = linearregslope
        this.linearregline
        this.levelsupport
        this.movingaveragecross = movingaveragecross
        this.relativestrength = relativestrength
        this.MACDcross = MACDcross
        this.bollinger = bollinger
        this.EMAsign = EMAsign


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
    if info.SandPdirection < 0 and beta < 0.4:
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

data = pd.DataFrame(refineds, ignore_index=True)
regression = linear_model.LinearRegression()
#regression.fit(X,y)

print("Linear regression samples have been created.")
