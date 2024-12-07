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


#print(df)

for i in range(0, len(df)-1):
    if resistance(df, i,3,3) == 1:
        print("found")


print("Program ended.")