#This file was created to copy data from tradinview.com by hand and then do calculations with that data
import pandas as pd
from sklearn import linear_model
from sklearn.preprocessing import PolynomialFeatures
import json
import random
from pyDOE3 import *
from Models.stockinfo import stockinfo

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

    
'''
samples = int(input("How many samples do you want to register?\n"))


infos = []
for i in range(0, samples):
    info = StockInfo()
    print("\nInfo about the stock:\n")
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
    info.SMAcross = input("Did the SMA200and50 cross?(y/n)\n")
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

for i in range(0, 4):
    #testing class conversion to dataframe:
    myrefind = stockinfo()
    myrefind.SandP = random.randrange(1,5)
    myrefind.analystrating = random.randrange(1,5)
    myrefind.affected = random.randrange(1,5)
    myrefind.linearregslope = random.randrange(1,5)
    myrefind.linearregline = random.randrange(1,5)
    myrefind.levelsupport = random.randrange(1,5)
    myrefind.movingaveragecross = random.randrange(1,5)
    myrefind.relativestrength = random.randrange(1,5)
    myrefind.MACDcross = random.randrange(1,5)
    myrefind.bollinger = random.randrange(1,5)
    myrefind.EMAsign = random.randrange(1,5)
    print(myrefind.Dictionary(i))
    refinds.append(myrefind.Dictionary(i))

data = pd.DataFrame(data= refinds)
#delete these drops later
#data.drop(["Index", "SandP", "analystrating", "affected","linearregline","levelsupport"],axis="columns")
print(data)

def DesignOfExperimentsFunction(factors, randomize=False):
    design = fullfact([2]*len(factors))
    design = 2*design - 1
    df = pd.DataFrame(design, columns=factors)
    return df

def FactorAverages(data):
    result = []
    for col in data.columns:
        if col != "Index":
            sumValue = 0
            count = 0
            for i in range(0, len(data.index)):
                count += 1
                sumValue += data[col][i]
            result.append(sumValue / count)
    return result

#Removed the multiplication with the registered values, because DOE samples create every combination even the future ones, which don't have registered indicator value yet
def MainEffects(InputDF, ResultColumnName, factorAverages):
    factors = [col for col in InputDF.columns if col != ResultColumnName]
    main_effects = {}
    for factor in factors:
        mean_plus = df[df[factor] == 1][ResultColumnName].mean()
        mean_minus = df[df[factor] == -1][ResultColumnName].mean()
        main_effects[factor] = mean_plus - mean_minus
    return main_effects

def GetInfluenceRatios(factors, columnnames):
    resultArray = []
    sumValue = 0
    for name in columnnames:
        sumValue += factors[name]
    if sumValue != 0:
        for name in columnnames:
            resultArray.append(factors[name] / sumValue)
    else:
        print(f"tried to divide by zero {sumValue}")
    return resultArray
    

def RegressionFunction():
    dataDictionaries = []
    for item in refinds:
        dataDictionaries.append(item.__dict__)

    #index is just a placeholder to have an index field.
    data = pd.DataFrame(data= dataDictionaries, index=[0,1,2,3])
    print(data)
    polynomialfeatures = PolynomialFeatures(degree=3, include_bias=False)
    X_polinomial = polynomialfeatures.fit_transform(data)
    regression = linear_model.LinearRegression()

    #y=pd.DataFrame(data=[random.randrange(1,10),random.randrange(1,10),random.randrange(1,10)], index=[0,1,2])
    #regression.fit(data,y)
    y=pd.DataFrame(data=[random.randrange(1,5),random.randrange(1,5),random.randrange(1,5),random.randrange(1,5)], index=[0,1,2,3])
    regression.fit(X_polinomial,y)

    print(regression.coef_)
    #Using random values for testing, change to actual later!
    randoms = []
    #for i in range(0, regression.n_features_in_):
    for i in range(0, 11):
        randoms.append(random.randrange(0,1))
    #print(regression.predict([randoms]))
    print(regression.predict(polynomialfeatures.transform([randoms])))

    with open("LinearRegressionData.txt", "w") as f:
        f.write(json.dumps(regression.coef_.__str__()))
    print("Linear regression samples have been created.")
    #Does let me change coefficiants directly
    regression.coef_[0][0] = 1
    print(regression.predict(polynomialfeatures.transform([randoms])))
#RegressionFunction()
df = DesignOfExperimentsFunction(['RSI','EMA',"SMA","BBup","BBdown", "LevelSupport", "AnalystRating","MovingAverageCross"])

columnNames = ['RSI','EMA',"SMA","BBup","BBdown","LevelSupport", "AnalystRating","MovingAverageCross"]
factAver = pd.DataFrame(columnNames)
calculatedAverages = FactorAverages(data)
resultvalues = []
for i in range(0,pow(2, len(columnNames))):
    resultvalues.append(random.randrange(1,10))

with open("FactorAverages.txt", "w") as f:
        #f.write(json.dumps(calculatedAverages))
        f.write(json.dumps(sum(resultvalues)/len(resultvalues)))
f.close()

saveActuals = []
for i in range(0,len(resultvalues)):
    saveActuals.append(resultvalues[i])
with open("Actuals.txt", "w") as f:
        #f.write(json.dumps(calculatedAverages))
        f.write(json.dumps(saveActuals))
f.close()


print("Averages of factors were saved.")
for i in range(0, len(columnNames)): 
    factAver.insert(i, columnNames[i], calculatedAverages[i])


df.insert(6,"Result",resultvalues)
effects = MainEffects(df, "Result", factAver)
df = df.drop("Result", axis='columns')
InfluenceRatios = []

for i in range(0, len(resultvalues)):
    for j in range(0, len(resultvalues)):
        if i != j:
            temp = resultvalues[i]
            resultvalues[i] = resultvalues[j]
            resultvalues[j] = temp
            df.insert(5,"Result",resultvalues)
            temp = df.iloc[i]
            df.iloc[i] = df.iloc[j]
            df.iloc[j] = temp
            effects = MainEffects(df, "Result", factAver)
            df = df.drop("Result", axis='columns')
            #df = df.drop("FactorAverages", axis='columns')
            InfluenceRatio = GetInfluenceRatios(effects, df)
            InfluenceRatios.append(InfluenceRatio)
print("DOE samples have been created.")
with open("InfluenceRationData.txt", "w") as f:
        f.write(json.dumps(InfluenceRatios))
print("DOE samples were saved.")
