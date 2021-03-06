import requests

def forexScrapeIntraday(from_currency,to_currency,interval,key):
    ''' Function to scrape intraday forex data from alphavantage '''
    f_curr = from_currency
    to_curr = to_currency
    tick = f'{f_curr}_{to_curr}'
    interval = interval
    key = key
    BASE_URL = 'https://www.alphavantage.co/query?function=FX_INTRADAY&'

    url = f'{BASE_URL}from_symbol={f_curr}&to_symbol={to_curr}&interval={interval}&outputsize=full&apikey={key}'
    print(url)
    data = requests.get(url=url).json()

    print('Complete')
    return data
