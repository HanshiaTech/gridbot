import configparser
from threading import Thread
import MetaTrader5 as mt5
from classes import Bot

config = configparser.ConfigParser()
config.read('mt5_settings.ini')  #path of your .ini file

#Start Setup/Configuration Trading

#Bot BackTesting
#server = 'OctaFX-Demo'
#login = 212928873
#password = '%AhDu6qz'

#Real Account
#server = 'OctaFX-Real2'
#login = 44707226
#password ='M3uYj%dM'

#########################################################################################
#symbols=("EURUSD","GBPUSD","USDJPY", "USDCHF","EURJPY","GBPJPY")
serverx = config.get("Settings", "Server")
loginx = int(config.get("Settings", "login"))
passwordx = config.get("Settings", "password")
symbolx = config.get("Settings", "symbol")
volumex = float(config.get("Settings", "volume_per_trade"))

max_orderx = int(config.get("Settings", "max_order"))
print(serverx, loginx, passwordx, symbolx, volumex,max_orderx)
#########################################################################################

server = serverx
login = loginx
password = passwordx

#Tested Pair EURUSD,GBPUSD
symbol = symbolx
volume = volumex
max_order = max_orderx

#End of Setup/Configuration

mt5.initialize(login=login, server=server, password=password)

# n Minimal 7 dapat 1 order limit
# n 5 = 7 order limit
# default profit_target = 2
# default proportion = 1

#Multiple Bot
bot1 = Bot(max_orderx, symbol, volume, 2, 1)


#bot2 = Bot(10,"BTCUSD",0.01,2,1)
#bot3 = Bot(8,"EURUSD",0.01,2,1)

def b1():
    bot1.run()


#def b2():
#   bot2.run()
#def b3():
#    bot3.run()

thread1 = Thread(target=b1)
#thread2 = Thread(target=b2)
#thread3 = Thread(target=b3)

thread1.start()
#thread2.start()
#thread3.start()

#Hedging Bot can't be run on Highest/Lowest Price. Avoid it