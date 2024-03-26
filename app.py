import os
import pandas as pd
import requests

def download_stock_data(stock_symbol, start_date, end_date, multiplier, timespan, api_key):
    try:
        # Define the API endpoint
        base_url = 'https://api.polygon.io/v2/aggs/ticker/'

        # Define the parameters
        params = {
            'adjusted': 'true',  # Adjusted data
            'limit': 50000,  # Maximum limit per request
            'apiKey': api_key
        }

        # Construct the URL
        url = f'{base_url}{stock_symbol}/range/{multiplier}/{timespan}/{start_date}/{end_date}'
        
        # Add parameters to the URL
        url += '?' + '&'.join([f'{k}={v}' for k, v in params.items()])

        # Print the request URL
        print(f"Request URL: {url}")

        # Make the API request
        response = requests.get(url)
        response.raise_for_status()  # Raise error if request fails
        data = response.json()

        # Check if the request was successful
        if data['status'] == 'OK':
            # Convert data to DataFrame
            df = pd.DataFrame(data['results'])
            
            # Get the directory of the script
            script_dir = os.path.dirname(os.path.realpath(__file__))
            
            # Save data to CSV in the same directory as the script
            file_name = os.path.join(script_dir, f"{stock_symbol}_{multiplier}_{timespan}_{start_date}_{end_date}.csv")
            df.to_csv(file_name, index=False)
            print(f"Stock data saved to {file_name}")
        else:
            print("Failed to retrieve data. Please check your API key and parameters.")
    except requests.exceptions.RequestException as e:
        print(f"Error occurred: {e}")

if __name__ == "__main__":
    # Input variables
    stock_symbol = input("Enter stock symbol: ").upper()
    start_date = input("Enter start date (YYYY-MM-DD): ")
    end_date = input("Enter end date (YYYY-MM-DD): ")
    multiplier = input("Enter multiplier: ")
    timespan = input("Enter timespan ('minute', 'hour', 'day'): ")
    api_key = 'k8Trr1VRMoixQgJUXA3BFqKzv0OUzsCm'

    # Download and save stock data
    download_stock_data(stock_symbol, start_date, end_date, multiplier, timespan, api_key)
