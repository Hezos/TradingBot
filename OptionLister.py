#Theory:




#from yahoo_fin import options
import yfinance as yf
import greeks_package as gp



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
#list_call_options(symbol)


# Download Apple call options within 30 days, ±5% moneyness
opts = gp.download_options(symbol, opt_type="c", max_days=100)

# Calculate all Greeks in one line
all_greeks = opts.apply(gp.greeks, axis=1, ticker=symbol)

# Combine with original data
full_data = opts.join(all_greeks)
print(full_data[['strike', 'lastPrice', 'Delta', 'Gamma', 'Vega', 'Theta']].head())




