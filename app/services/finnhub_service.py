import requests

API_KEY = 'd3aigg9r01qlsbrrj460d3aigg9r01qlsbrrj46g'

def get_stock_quote(symbol):
    url = f'https://finnhub.io/api/v1/quote?symbol={symbol}&token={API_KEY}'
    response = requests.get(url)
    print(symbol, response.status_code, response.json())
    if response.status_code == 200:
        return response.json()
    else:
        return None

