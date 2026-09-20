
import MetaTrader5 as mt5

# Initialize MetaTrader 5
mt5.initialize()

# Get open positions
positions = mt5.positions_get()
current_account_info = mt5.account_info()
print (current_account_info.profit)
if current_account_info.profit == 10:
        mt5.Close("EURUSD")

if current_account_info.profit == -10:
        mt5.Close("EURUSD")

# Shut down MetaTrader 5
#mt5.shutdown()