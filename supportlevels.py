import yfinance as yf
import pandas as pd
import pandas_ta as ta

print("Program started")

df = yf.download("VET", start="2022-04-01", end="2023-05-03",  interval = "1d")
df=df[df['Volume']!=0]
df.reset_index(drop=True, inplace=True)
df.isna().sum()
df['RSI'] = ta.rsi(df.Close, length=12)
df.tail()

#threshold on what is considered notable difference
wick_threshold = 0.001
def support(df1, l, n1, n2): #n1 n2 before and after candle l
    if ( df1.Low[l-n1:l].min() < df1.Low[l] or df1.Low[l+1:l+n2+1].min() < df1.Low[l] ):
        return 0

    candle_body = abs(df1.Open[l]-df1.Close[l])
    lower_wick = min(df1.Open[l], df1.Close[l])-df1.Low[l]
    if (lower_wick > candle_body) and (lower_wick > wick_threshold): 
        return 1
    
    return 0

def resistance(df1, l, n1, n2): #n1 n2 before and after candle l
    if ( df1.High[l-n1:l].max() > df1.High[l] or df1.High[l+1:l+n2+1].max() > df1.High[l] ):
        return 0
    
    candle_body = abs(df1.Open[l]-df1.Close[l])
    upper_wick = df1.High[l]-max(df1.Open[l], df1.Close[l])
    if (upper_wick > candle_body) and (upper_wick > wick_threshold) :
        return 1

    return 0

#------------------------------------------------------------------------------------------------------------

def closeResistance(l,levels,lim, df):
    if len(levels)==0:
        return 0
    c1 = abs(df.High[l]-min(levels, key=lambda x:abs(x-df.High[l])))<=lim
    c2 = abs(max(df.Open[l],df.Close[l])-min(levels, key=lambda x:abs(x-df.High[l])))<=lim
    c3 = min(df.Open[l],df.Close[l])<min(levels, key=lambda x:abs(x-df.High[l]))
    c4 = df.Low[l]<min(levels, key=lambda x:abs(x-df.High[l]))
    if( (c1 or c2) and c3 and c4 ):
        return min(levels, key=lambda x:abs(x-df.High[l]))
    else:
        return 0
    
def closeSupport(l,levels,lim, df):
    if len(levels)==0:
        return 0
    
    
    c1 = abs(df.Low[l]-min(levels, key=lambda x: abs(x-df.Low[l])) )<=lim
    c2 = abs(min(df.Open[l],df.Close[l])-min(levels, key=lambda x:abs(x-df.Low[l])))<=lim

    c3 = max(df.Open[l],df.Close[l])>min(levels, key=lambda x:abs(x-df.Low[l]))

    c4 = df.High[l]>min(levels, key=lambda x:abs(x-df.Low[l]))

    if( (c1 or c2) and c3 and c4 ):
        return min(levels, key=lambda x:abs(x-df.Low[l]))
    else:
        return 0

def is_below_resistance(l, level_backCandles, level, df):
    return df.loc[l-level_backCandles:l-1, 'High'].max() < level

def is_above_support(l, level_backCandles, level, df):
    return df.loc[l-level_backCandles:l-1, 'Low'].min() > level


#print(df)

for l in range(0, len(df)):
    #if closeSupport(i,[10,11,15],0.08,df) > 0:
    #    print( "found" )
    #The key is on the level
    if is_above_support(l, 6,0.003,df):
        print(l)





print("Program ended.")