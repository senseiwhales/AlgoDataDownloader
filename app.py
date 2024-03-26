import os
import yfinance as yf
import pandas as pd

def download_stock_data(stock_symbol, interval):
    try:
        # Download stock data
        stock_data = yf.download(stock_symbol, interval=interval)

        # Get the directory of the script
        script_dir = os.path.dirname(os.path.realpath(__file__))

        # Save data to CSV in the same directory as the script
        file_name = os.path.join(script_dir, f"{stock_symbol}_{interval}.csv")
        stock_data.to_csv(file_name)
        print(f"Stock data saved to {file_name}")
    except Exception as e:
        print(f"Error occurred: {str(e)}")

if __name__ == "__main__":
    # Input variables
    stock_symbol = input("Enter stock symbol: ").upper()
    interval = input("Enter interval (e.g., '1d' for daily, '1wk' for weekly): ")

    # Download and save stock data
    download_stock_data(stock_symbol, interval)
