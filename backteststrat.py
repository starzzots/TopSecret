from config import *
import robin_stocks.robinhood as r
import matplotlib.pyplot as plt
import datetime as dt

# Login to Robinhood
username = USER
password = PASS
r.login(username, password)

#!!! fill out the specific option information
symbol = 'SPY'
symbol_name = r.get_name_by_symbol(symbol)
expirationDate = '2024-12-12' # format is YYYY-MM-DD.
strike = 608
strike1 = 609
optionType = 'call' # available options are 'call' or 'put' or None.
#!!!


findoption = r.find_options_by_expiration_and_strike(symbol, expirationDate, strike, optionType)
findoption2 = r.find_options_by_expiration_and_strike(symbol, expirationDate, strike1, optionType)
findoption3 = r.find_options_by_expiration(symbol, expirationDate, strike, optionType)
clean = findoption3
clean2 = findoption2[0]["ask_price"]

print(clean) 

