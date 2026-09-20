import MetaTrader5 as mt5
import pandas as pd

# Initialize MetaTrader 5
mt5.initialize()

# Get open positions
positions = mt5.positions_get()
lot = 1
distance=400
point = mt5.symbol_info("BTCUSD").point
symbol_tick = mt5.symbol_info_tick("BTCUSD")
ask = symbol_tick.ask
bid = symbol_tick.bid
buy_profit = mt5.order_calc_profit(mt5.ORDER_TYPE_BUY, "BTCUSD", lot, ask, ask + distance * point)
print("Account currency:",buy_profit)