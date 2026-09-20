import MetaTrader5 as mt5
import pandas as pd

mt5.initialize()  # connect to MetaTrader 5

symbols = ['AUDCAD']

prices = {}

for symbol in symbols:
    data = mt5.copy_rates_from_pos(symbol, mt5.TIMEFRAME_D1, 0, 10)
    prices[symbol] = pd.DataFrame(data)[["time", "open", "high", "low", "close"]]
    print( prices[symbol])