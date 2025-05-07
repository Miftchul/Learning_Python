import requests
import csv
import time
from datetime import datetime, timedelta

def get_crypto_price(crypto):
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={crypto}&vs_currencies=usd"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data.get(crypto, {}).get('usd', 'Price not available')
    else:
        return 'Error fetching data'

def log_prices_to_csv(filename, cryptos):
    with open(filename, mode='a', newline='') as file:
        writer = csv.writer(file)
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        row = [timestamp]
        for crypto in cryptos:
            price = get_crypto_price(crypto)
            row.append(price)
        writer.writerow(row)

def main():
    cryptos = ['bitcoin', 'ethereum', 'binancecoin']
    filename = 'crypto_prices.csv'

    # Write header to CSV file
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        header = ['Timestamp'] + [crypto.capitalize() for crypto in cryptos]
        writer.writerow(header)

    end_time = datetime.now() + timedelta(days=1)
    print("Logging crypto prices for the next 24 hours...")

    while datetime.now() < end_time:
        log_prices_to_csv(filename, cryptos)
        print(f"Logged prices at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        time.sleep(3600)  # Log every hour

    print(f"Logging completed. Data saved to {filename}")

if __name__ == "__main__":
    main()