import MetaTrader5 as mt5
import pandas as pd
from classes1 import Bot
from threading import Thread

#New Bot BackTesting
#OctaFX-Demo
#212928873
#%AhDu6qz


#New Bot BackTesting
#OctaFX-Demo
#213383700
#Up&g6BaM

#Real Account
#OctaFX-Real2
#44707226
#M3uYj%dM



mt5.initialize(login = 212928873,server = "OctaFX-Demo",password ="%AhDu6qz")

# n Minimal 7 dapat 1 order limit
# n 10 = 7 order limit
# default profit_target = 2
# default proportion = 1

bot1 = Bot(10,"AUDNZD",0.01,2,1)
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
