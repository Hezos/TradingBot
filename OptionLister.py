#from yahoo_fin import options
import yfinance as yf

def list_call_options(symbol):
    """
    Fetch and list all call options for the given stock symbol.
    Example: list_call_options("AAPL")
    """
    # Fetch stock data
    stock = yf.Ticker(symbol)

    # Get all available expiration dates
    expirations = stock.options
    if not expirations:
        print(f"No options found for {symbol}")
        return
    # Loop through each expiration and list call options
    for exp in expirations:
        opt_chain = stock.option_chain(exp)
        calls = opt_chain.calls

        print(f"=== CALL OPTIONS for {symbol} Expiring {exp} ===")
        print(calls[['contractSymbol', 'strike', 'lastPrice', 'bid', 'ask', 'volume', 'openInterest']])
        print("\n")

symbol = input("Enter stock symbol: ").strip().upper()
list_call_options(symbol)
