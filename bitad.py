import requests
from bs4 import BeautifulSoup
import time
# Get Bitcoin Price From ArzDigital Web site every 1 sec
# first use this : 
# pip install requests
# pip install bs4
# pip install time

def get_bitcoin_price():
    url = 'https://arzdigital.com/coins/bitcoin/'
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        price_tag = soup.find('div', {'class': 'arz-coin-page-data__coin-price coinPrice btcprice pulser-dollar-bitcoin'})
        if price_tag:
            bitcoin_price = price_tag.text.strip()
            return bitcoin_price
    return None

while True:
    bitcoin_price = get_bitcoin_price()
    if bitcoin_price:
        print(f"The current price of Bitcoin is {bitcoin_price}")
    else:
        print("Failed to retrieve Bitcoin price")
    time.sleep(1)  # Refresh every 1 second
