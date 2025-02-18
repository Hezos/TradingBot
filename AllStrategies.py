from tradingview_ta import TA_Handler, Interval, Exchange
import tradingview_ta
import yfinance as yf
import ta
from stockstats import wrap
import stockstats
from ta.volatility import BollingerBands
import pandas as pd
from sklearn import linear_model
import pandas_ta

from mplchart.chart import Chart
from mplchart.primitives import Candlesticks, Volume
from mplchart.indicators import SMA, EMA, ROC, RSI, MACD



stock = TA_Handler(
    symbol="MRVI",
    screener="america",
    exchange="NASDAQ",
    interval=Interval.INTERVAL_1_MINUTE
)

#print(stock.get_analysis().indicators['MACD.macd'])
#print(stock.get_analysis().indicators['MACD.signal'])
#print(stock.get_indicators()['EMA200'])
ticker = yf.Ticker('MRVI')
#print(ticker.option_chain())

ticker = yf.download('MRVI',start='2024-12-05', end='2025-02-13')
info = ticker.dropna()
#https://pypi.org/project/stockstats/
info = wrap(ticker)
#ticker["Adown"] = ta.trend.AroonIndicator(ticker['High'],ticker['Low']).aroon_down()
#ticker["Aup"] = ta.trend.AroonIndicator(ticker['High'],ticker['Low']).aroon_up()
#ticker["Aroon"] = ta.trend.AroonIndicator(ticker['High'],ticker['Low']).aroon_indicator()
#print(ticker)
#print(info['macdh'].tail(10))
indicator_bb = BollingerBands(close=info['close'],window=20,window_dev=2)
info['bb_bbh'] = indicator_bb.bollinger_hband()
info['bb_bbl'] = indicator_bb.bollinger_lband()
MACDcomponent = info[['macd', 'macds','macdh']]

#print(f"Historical:{MACDcomponent}")
#data = stockstats.StockDataFrame._get_ema(info,stockstats._Meta('Close))
#print(data)
#print(info['close_10_lrma'])

#regression:
X = info[["open", "low", "high"]]
y = info["close"]

regression = linear_model.LinearRegression()
regression.fit(X,y)

predicted = regression.predict([[470,450,490]])
#print(predicted, regression.coef_)

