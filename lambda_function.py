from forex_scrape import forex_scrape_intraday
from config import API_KEY, BUCKET_NAME, BUCKET_FOLDER
from datetime import datetime
import boto3
import json

def lambda_handler(event,context):
    print(context)
    key = API_KEY
    curr1 = 'EUR'
    curr2 = 'JPY'
    file = f'{curr1}_{curr2}_{datetime.now().strftime("%d-%m-%Y")}.json'

    #Scrape Data
    data = forex_scrape_intraday(curr1,curr2,'1min',key)

    #Write to s3
    s3 = boto3.resource('s3')
    obj = s3.Object(BUCKET_NAME, f'{BUCKET_FOLDER}/{file}')
    obj.put(Body=json.dumps(data).encode('UTF-8'))

    print('Uploaded')
