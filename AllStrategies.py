from tradingview_ta import TA_Handler, Interval, Exchange
import tradingview_ta
import yfinance as yf
import ta
from stockstats import wrap
import stockstats

stock = TA_Handler(
    symbol="MSFT",
    screener="america",
    exchange="NASDAQ",
    interval=Interval.INTERVAL_1_DAY
)
print(stock.get_analysis().indicators['MACD.macd'])
print(stock.get_indicators()['EMA200'])
ticker = yf.Ticker('MSFT')
#print(ticker.option_chain())

ticker = yf.download('MSFT',start='2025-1-05', end='2025-01-28')
info = wrap(ticker)
#ticker["Adown"] = ta.trend.AroonIndicator(ticker['High'],ticker['Low']).aroon_down()
#ticker["Aup"] = ta.trend.AroonIndicator(ticker['High'],ticker['Low']).aroon_up()
#ticker["Aroon"] = ta.trend.AroonIndicator(ticker['High'],ticker['Low']).aroon_indicator()
#print(ticker)
#print(info['macdh'].tail(10))
#data = stockstats.StockDataFrame._get_ema(info,stockstats._Meta('Close))
#print(data)