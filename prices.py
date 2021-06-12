import requests

headers = {
    'X-CMC_PRO_API_KEY': '',
    'Accepts': 'application/json'
}

parameters = {
    'start': '1',
    'limit': '20',
    'convert': 'CAD'
}

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'

json_data = requests.get(url, params=parameters, headers=headers).json()
