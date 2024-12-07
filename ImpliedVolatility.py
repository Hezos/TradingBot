import yfinance as yf
import yahoo_fin.stock_info
from datetime import datetime
import pandas as pd
import yahooquery as yq
import matplotlib.pyplot as plt

TickerSymbol = 'MSFT'


#Using the impiled volatility method
CompanyData = yq.Ticker(TickerSymbol)
df = CompanyData.option_chain
#print(df.head)