import yfinance as yf
import pandas as pd
import pandas_ta as ta
import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from datetime import datetime
import matplotlib.pyplot as plt


print("Program started")

df = yf.download("VET", start="2023-04-01", end="2024-12-10",  interval = "1d")
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

openprices = df["Open"].to_list()
supports = []
resistances = []

closeToSupport = []
closeToResistance = []

for i in range(0, len(df)):
    if resistance(df, i, 3, 3):
        resistances.append(openprices[i])
    if support(df, i, 3,3):
        supports.append(openprices[i])

supports.sort() #keep lowest support when popping a level
for i in range(1,len(supports)):
    if(i>=len(supports)):
        break
    if abs(supports[i]-supports[i-1])<=0.001: # merging close distance levels
        supports.pop(i)

resistances.sort(reverse=True) # keep highest resistance when popping one
for i in range(1,len(resistances)):
    if(i>=len(resistances)):
        break
    if abs(resistances[i]-resistances[i-1])<=0.001: # merging close distance levels
        resistances.pop(i)

#----------------------------------------------------------------------
# joined levels
rrss = resistances+supports
rrss.sort()
for i in range(1,len(rrss)):
    if(i>=len(rrss)):
        break
    if abs(rrss[i]-rrss[i-1])<=0.0001: # merging close distance levels
        rrss.pop(i)



for i in range(0, len(df)):
    if closeSupport(i,supports,0.05,df) != 0:
        closeToSupport.append(df.iloc[i])
    if closeResistance(i,resistances,0.05,df) != 0:
        closeToResistance.append(df.iloc[i])


supportList = []
resistanceList = []

for l in range(0, len(closeToResistance)):
    if ( is_below_resistance(l,6,closeToResistance[l]["Open"], df) and df.RSI[l-1:l].min()<30 ):
        resistanceList.append(df.iloc[l])

for l in range(0, len(closeToSupport)):
    if( is_above_support(l,6,closeToSupport[l]["Open"],df) and df.RSI[l-1:l].max()>70 ):
        supportList.append(df.iloc[l])



def pivotid(df1, l, n1, n2): #n1 n2 before and after candle l
    if l-n1 < 0 or l+n2 >= len(df1):
        return 0
    
    pividlow=1
    pividhigh=1
    for i in range(l-n1, l+n2+1):
        if(df1.Low[l]>df1.Low[i]):
            pividlow=0
        if(df1.High[l]<df1.High[i]):
            pividhigh=0
    if pividlow and pividhigh:
        return 3
    elif pividlow:
        return 1
    elif pividhigh:
        return 2
    else:
        return 0
    
def pointpos(x):
    if x['pivot']==1:
        return x['Low']-1e-3
    elif x['pivot']==2:
        return x['High']+1e-3
    else:
        return np.nan

df['pivot'] = df.apply(lambda x: pivotid(df, x.name,10,10), axis=1)
df['pointpos'] = df.apply(lambda row: pointpos(row), axis=1)


print("Supports:")
for item in supportList:
    print(item)
print("Resistances:")
print(resistanceList)

print(len(closeToResistance))

dfpl = df

fig = go.Figure(data=[go.Candlestick(x=dfpl.index,
                open=dfpl['Open'],
                high=dfpl['High'],
                low=dfpl['Low'],
                close=dfpl['Close'])])

fig.update_layout(
    autosize=False,
    width=1000,
    height=800, 
    paper_bgcolor='black',
    plot_bgcolor='black')
fig.update_xaxes(gridcolor='black')
fig.update_yaxes(gridcolor='black')
fig.add_scatter(x=dfpl.index, y=dfpl['pointpos'], mode="markers",
                marker=dict(size=8, color="MediumPurple"),
                name="Signal")
#fig.show()



dfpl = df
fig = go.Figure(data=[go.Candlestick(x=dfpl.index,
                open=dfpl['Open'],
                high=dfpl['High'],
                low=dfpl['Low'],
                close=dfpl['Close'],
                increasing_line_color= 'green', 
                decreasing_line_color= 'red')])

fig.add_scatter(x=dfpl.index, y=dfpl['pointpos'], mode="markers",
                marker=dict(size=5, color="MediumPurple"),
                name="pivot")
fig.update_layout(xaxis_rangeslider_visible=False)
fig.update_xaxes(showgrid=False)
fig.update_yaxes(showgrid=False)
fig.update_layout(paper_bgcolor='black', plot_bgcolor='black')

#fig.show()

dfkeys = df[:]

# Filter the dataframe based on the pivot column
high_values = dfkeys[dfkeys['pivot'] == 2]['High']
low_values = dfkeys[dfkeys['pivot'] == 1]['Low']

# Define the bin width
bin_width = 0.003  # Change this value as needed

# Calculate the number of bins
bins = int((high_values.max() - low_values.min()) / bin_width)

# Create the histograms
plt.figure(figsize=(10, 5))
plt.hist(high_values, bins=bins, alpha=0.5, label='High Values', color='red')
plt.hist(low_values, bins=bins, alpha=0.5, label='Low Values', color='blue')

plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('Histogram of High and Low Values')
plt.legend()
#plt.show()

def check_candle_signal_plot(l, n1, n2, backCandles, df, proximity):
    ss = []
    rr = []
    for subrow in range(l-backCandles, l-n2):
        if support(df, subrow, n1, n2):
            ss.append(df.Low[subrow])
        if resistance(df, subrow, n1, n2):
            rr.append(df.High[subrow])
    
    ss.sort() #keep lowest support when popping a level
    i = 0
    while i < len(ss)-1:
        if abs(ss[i]-ss[i+1]) <= proximity:
            # ss[i] = (ss[i]+ss[i+1])/2
            # del ss[i+1]
            del ss[i+1]
        else:
            i+=1

    rr.sort(reverse=True) # keep highest resistance when popping one
    i = 0
    while i < len(rr)-1:
        if abs(rr[i]-rr[i+1]) <= proximity:
            #rr[i] = (rr[i]+rr[i+1])/2
            #del rr[i+1]
            del rr[i]
        else:
            i+=1

    dfpl=df[l-backCandles-n1:l+n2+50]
    fig = go.Figure(data=[go.Candlestick(x=dfpl.index,
                open=dfpl['Open'],
                high=dfpl['High'],
                low=dfpl['Low'],
                close=dfpl['Close'])])

    c=0
    while (1):
        if(c>len(ss)-1 ):
            break
        fig.add_shape(type='line', x0=l-backCandles-n1, y0=ss[c],
                    x1=l,
                    y1=ss[c],
                    line=dict(color="MediumPurple",width=2), name="Support"
                    )
        c+=1

    c=0
    while (1):
        if(c>len(rr)-1 ):
            break
        fig.add_shape(type='line', x0=l-backCandles-n1, y0=rr[c],
                    x1=l,
                    y1=rr[c],
                    line=dict(color="Red",width=2), name="Resistance"
                    )
        c+=1    

    # fig.add_scatter(x=dfpl.index, y=dfpl['pointpos'], mode="markers",
    #             marker=dict(size=5, color="MediumPurple"),
    #             name="Signal")

    fig.update_layout(
    autosize=False,
    width=1000,
    height=800,)
    
    fig.show()
 
 
    #----------------------------------------------------------------------
    cR = closeResistance(l, rr, 150e-5, dfpl)
    cS = closeSupport(l, ss, 150e-5, dfpl)
    #print(cR, is_below_resistance(l,6,cR, dfpl))
    if (cR and is_below_resistance(l,6,cR, dfpl) ):#and df.RSI[l]>65
        return 1
    elif(cS and is_above_support(l,6,cS,dfpl) ):#and df.RSI[l]<35
        return 2
    else:
        return 0

check_candle_signal_plot(231, 4,4,100,df,0.02)

print("Program ended.")