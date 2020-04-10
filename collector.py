import json
import requests
from datetime import datetime
from .config import BASE_URL, API_KEY, BUCKET_NAME, BUCKET_FOLDER
import utils

#https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=5min&outputsize=full&apikey=demo

def handler(event, context):
	print(context)
	tickers = event.get('tickers', [])
	interval = event.get('interval', '5min')
	if len(tickers) > 5:
		print(f'Limit 5 tickers per request.')
		tickers = tickers[:5]
	for tick in tickers:
		url = f'{BASE_URL}function=TIME_SERIES_INTRADAY&symbol={tick}&interval={interval}&outputsize=full&apikey={API_KEY}'
		data = requests.get(url=url).json()
		file_name = f'{tick}_{datetime.now().strftime("%d-%m-%Y")}.json'
		utils.write_s3_json_file(data, BUCKET_NAME, f'{BUCKET_FOLDER}/{file_name}')
		print(f'uploaded {file_name}')
