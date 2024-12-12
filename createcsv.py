from config import *
import robin_stocks.robinhood as r
import matplotlib.pyplot as plt
import datetime
import os
import time as t
# Login to Robinhood
username = USER
password = PASS
r.login(username, password)

#!!! fill out the specific option information
strike = 608
date = "2024-12-12"
stock = "SPY"
optionType = "call" #or "put"
#!!!

# File saving variables
minutesToTrack = 1 
PrintInterval = 10 
endTime = t.time() + 60 * minutesToTrack
fileName = ".venv/options/spy/spy.csv"
writeType = "w" 

# Create directory if it doesn't exist
os.makedirs(os.path.dirname(fileName), exist_ok=True)

# Open file in write mode
with open(fileName, mode=writeType) as fileStream:
    # Write header row
    fileStream.write("Timestamp,")
    fileStream.write("Instrument_Key,Instrument_Value,")
    fileStream.write("Market_Key,Market_Value\n") 

    while t.time() < endTime:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Get the data
        try:
            instrument_data = r.get_option_instrument_data(stock, date, strike, optionType)
            market_data = r.get_option_market_data(stock, date, strike, optionType)
        except Exception as e:
            print(f"Error fetching data: {e}")
            continue  # Skip this iteration and continue with the loop

        # Write instrument data
        for key, value in instrument_data.items():
            fileStream.write(f"{timestamp},{key},{value},")

        # Write market data
        for key, value in market_data[0][0].items():
            fileStream.write(f",{key},{value}\n")

        print(timestamp)  # Print timestamp for visual feedback
        t.sleep(PrintInterval)