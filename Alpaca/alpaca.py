from alpaca.trading.stream import TradingStream
from datetime import datetime, timedelta
import alpaca
from alpaca.data.historical.option import OptionHistoricalDataClient, OptionLatestQuoteRequest
from alpaca.data.historical.stock import StockHistoricalDataClient, StockLatestTradeRequest
from alpaca.trading.client import TradingClient, GetAssetsRequest
from alpaca.trading.requests import GetOptionContractsRequest, LimitOrderRequest, MarketOrderRequest, GetOrdersRequest
from alpaca.trading.enums import AssetStatus, ContractType, OrderSide, OrderType, TimeInForce, QueryOrderStatus


trade_client = TradingClient(api_key="", secret_key="", paper=True)
stock_data_client = StockHistoricalDataClient(api_key="", secret_key="")
option_data_client = OptionHistoricalDataClient(api_key="", secret_key="")

acct = trade_client.get_account()
print(f"Options Approved level:{acct.options_approved_level}")
print(f"Options Trading level:{acct.options_trading_level}")
print(f"Options Buying Power:{acct.options_buying_power}")

acct_config = trade_client.get_account_configurations()
print(f"Max Options Trading Level = {acct_config.max_options_trading_level}")
acct_config.max_options_trading_level = 1
trade_client.set_account_configurations(acct_config)

acct_config = trade_client.get_account_configurations()
print(f"Max Options Trading Level:{acct_config.max_options_trading_level}")

request = GetAssetsRequest(
    status = AssetStatus.ACTIVE,
    attributes = "options_enabled"
)

options_enabled_underlyings = trade_client.get_all_assets(request)
print(f"Number of underlyings with Options:{len(options_enabled_underlyings)}")
underlying_symbol = "MRVI"
underlying = trade_client.get_asset(symbol_or_asset_id=underlying_symbol)
print(f"{underlying_symbol} has options? {'options_enabled' is underlying.attributes}")

positions = trade_client.get_all_positions()

for p in positions:
    print(p)


alpaca_keys = {}

trade_stream_client = TradingStream(api_key="", secret_key="",paper=True)

async def trade_updates_handler(data):
    print(data)

trade_stream_client.subscribe_trade_updates(trade_updates_handler)
trade_stream_client.run()







