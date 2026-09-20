import MetaTrader5 as mt5

# Initialize MetaTrader 5
mt5.initialize()

# Get open positions
positions = mt5.positions_get()


# Close all open positions
for position in positions:
    result = mt5.Close(symbol='BTCUSD',ticket=position.ticket)
    if result != True:
        print(f"Failed to close position {position.ticket}: {result.comment}")
    else:
        print(f"Position {position.ticket} closed successfully")

# Shut down MetaTrader 5
mt5.shutdown()