import requests
from loggingUtil import logger
from tempfile import NamedTemporaryFile
import shutil
import csv


def update_items_swap(account):
    logger.warning('Update price of [SWAP]')

    headers = {
        'authority': 'tradeit.gg',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'en-US,en;q=0.9',
        'cookie': account['tradeit_cookie'],
        'if-none-match': 'W/"d470-Vwf6dM+IjnUu1VT7GcuJXcnof/o"',
        'referer': 'https://tradeit.gg/csgo/trade',
        'sec-ch-ua': '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Linux"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
    }

    params = {
        'fresh': '0',
    }

    ROOT = 'https://api.swap.gg/prices/730?fbclid=IwAR0It3Kufu4mW2qtRjTo8MXzpB5sprTNWNoRRAiybUlGOqlg2rWKxrwXFE4'
    response = requests.get(ROOT, params=params, headers=headers)

    res = response.json()
    if res["status"] == "OK":
        items = res['result']
        filename = 'prices.csv'
        tempfile = NamedTemporaryFile(mode='w', delete=False)

        fields = [
            'name', 'etopfun_price', 'tradeit_price', 'swap_price',
            'loot_price', 'recommend', 'buff_price', 'empire_price'
        ]
        with open(filename, 'r', encoding='UTF8') as csvfile, tempfile:
            reader = csv.DictReader(csvfile, fieldnames=fields)
            writer = csv.DictWriter(tempfile, fieldnames=fields)
            for row in reader:
                for item in items:
                    if item.get('marketName') == row['name']:
                        row['swap_price'] = format(item['price']['value'] / 100, '.2f')
                        break
                row = {
                    'name': row['name'],
                    'etopfun_price': row['etopfun_price'],
                    'tradeit_price': row['tradeit_price'],
                    'swap_price': row['swap_price'] if row['swap_price'] else 0,
                    'loot_price': row['loot_price'],
                    'recommend': row['recommend'],
                    'buff_price': row['buff_price'],
                    'empire_price': row['empire_price']
                }
                writer.writerow(row)

        shutil.move(tempfile.name, filename)
    else:
        logger.error('API: {}, with errors: {}'.format(ROOT, res['errors']))
