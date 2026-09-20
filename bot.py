import MetaTrader5 as mt5
import pandas as pd
import numpy as np

import time
from Personal_MT5_library import *
from datetime import datetime

mt5.initialize()


def random(symbol):
    values = [True, False]
    buy = np.random.choice(values)
    sell = not buy

    return buy, sell


current_account_info = mt5.account_info()
print("------------------------------------------------------------------")
print(f"Login: {mt5.account_info().login} \tserver: {mt5.account_info().server}")
print(f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
print(
    f"Balance: {current_account_info.balance} USD, \t Equity: {current_account_info.equity} USD, \t Profit: {current_account_info.profit} USD")
print(f"Run time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
print("------------------------------------------------------------------")

launching = [[0, "00:15:59"]
             ]

symbols_list = {
    "EURUSD": ["BTCUSD", 0.2],
}

while True:

    # TSL
    MT5.trailing_stop_loss()
    MT5.verif_tsl()

    # Launch the algorithm
    # Verfication for launch
    current_time = [datetime.now().weekday(), datetime.now().strftime("%H:%M:%S")]
    if current_time in launching:
        is_time = True
    else:
        is_time = False

    # is_time=True #Only to run the trading NOW

    if is_time:
        # Open the trades

        for asset in symbols_list.keys():
            # Initialize the inputs
            symbol = symbols_list[asset][0]
            lot = symbols_list[asset][1]

            # Attemp to enable the symbol in the MT5 MarketWatch
            selected = mt5.symbol_select(symbol)
            if not selected:
                print(f"\nERROR - Failed to select '{symbol}' in MetaTrader 5 with error :", mt5.last_error())

            else:
                # Create the signals
                buy, sell = random(symbol)

                # Run the algorithm
                MT5.run(symbol, buy, sell, lot, pct_tp=0.1, pct_sl=0.05)