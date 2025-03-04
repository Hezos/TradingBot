#This file was created to copy data from tradinview.com by hand and then do calculations with that data
SandPdirection = input("The direction of the S&P500\n")
isnewsaffected = input("Did you read any news for this day? Yes or no? (y/n)\n")
currentprice = input("The stock price:\n")
linearregressionslope = input("The direction of the linear regression slope (The higher number the higher the accelaration):\n")
leastsquaresmovingaveragedirection = input("The least squares moving average direction:\n")
linearregressionaccuarity = input("The accuarity of the linear regression:\n")
closestsupportlevel = input("The closest support level:\n")
fiftytwoweeklow = input("The 52 week low:\n")
SMAcross = input("Did the SMA200and50 cross?\n")
RSI = input("The RSI value:\n")
MACDline = input("MACD line value:\n")
MACDsignal = input("MACD signal value:\n")
bollingerbands = input("The lower bollinger bands' value:\n")
EMA = []
print("The last 5 EMA values:")
for i in range(0,5):
    EMA.append(input("EMA value here:\n"))





print(RSI,MACDline,MACDsignal,EMA)
