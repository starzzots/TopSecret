from main import *
import time
import csv


def store_data(symbol="DOGE-USD", csvname='test.csv'):
    """
    Append data to CSV
    """
    api_trading_client = CryptoAPITrading()
    data = api_trading_client.get_estimated_price(symbol=symbol, side="ask", quantity="1")
    new_row = data['results'][0]

    # File path for the CSV file
    csv_file_path = csvname

    # Check if the file exists and whether a header is needed
    try:
        with open(csv_file_path, mode='r') as file:
            header_exists = file.readline().strip() != ''
    except FileNotFoundError:
        header_exists = False

    # Open the file in append mode
    with open(csv_file_path, mode='a', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=new_row.keys())

        # Write the header if it doesn't exist
        if not header_exists:
            writer.writeheader()

        # Write the new row of data
        writer.writerow(new_row)

    print(f"Data appended to {csv_file_path}")


if __name__ == "__main__":

    while True:
        store_data(symbol="BTC-USD", csvname=f"data/BTC2")  # Append new data
        store_data(symbol="BTC-USD", csvname=f"data/DODE2")  # Append new data
        store_data(symbol="BTC-USD", csvname=f"data/ETH2")  # Append new data
        store_data(symbol="BTC-USD", csvname=f"data/LTC2")  # Append new data
        time.sleep(60)  # Wait for 1 minute before the next update