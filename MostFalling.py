import yfinance as yf
import yahoo_fin.stock_info
from datetime import datetime
import pandas as pd
import yahooquery as yq
import matplotlib.pyplot as plt
import numpy as np


# Bank of Ireland Group plc BIRG or BIRG.IR
TickerSymbol = ["BIRG.IR", "MSFT"]
'''
for symbol in TickerSymbol:
    data = yf.download(symbol, start='2024-07-10', end='2024-09-07')
    array = data["Close"].to_numpy()
    print('\n')
    for i in range(1,len(array)):
        print(array[i])
'''
#print(data["Close"])
data = yq.Ticker(TickerSymbol)
print(data.option_chain)