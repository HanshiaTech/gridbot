import configparser
config = configparser.ConfigParser()
config.read('mt5_settings.ini') #path of your .ini file
year = config.get("Settings","Server")
print(year)


