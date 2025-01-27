from tradingview_ta import TA_Handler, Interval, Exchange
import tradingview_ta
import yfinance as yf
import ta

stock = TA_Handler(
    symbol="TSLA",
    screener="america",
    exchange="NASDAQ",
    interval=Interval.INTERVAL_1_DAY
)
#print(stock.get_analysis().indicators)
#print(stock.get_analysis().indicators.keys())
ticker = yf.Ticker('MSFT')
#print(ticker.option_chain())

ticker = yf.download('MSFT',start='2024-12-05', end='2025-01-24')

ticker["Adown"] = ta.trend.AroonIndicator(ticker['High'],ticker['Low']).aroon_down()
ticker["Aup"] = ta.trend.AroonIndicator(ticker['High'],ticker['Low']).aroon_up()
ticker["Aroon"] = ta.trend.AroonIndicator(ticker['High'],ticker['Low']).aroon_indicator()
print(ticker)