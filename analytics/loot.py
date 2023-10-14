import requests
from logging_example import logger
from tempfile import NamedTemporaryFile
import shutil
import csv


def update_items_loot(account):
    headers = {
        'authority': 'loot.farm',
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9',
        # 'cookie': account['loot_cookie'],
        'referer': 'https://loot.farm/',
        'sec-ch-ua': '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Linux"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
    }

    params = {
        'game': '730',
    }

    ROOT = 'https://loot.farm/fullprice.json'
    response = requests.get(ROOT, params=params, headers=headers)

    res = response.json()
    if res:
        filename = 'prices.csv'
        tempfile = NamedTemporaryFile(mode='w', delete=False)

        fields = ['name', 'etopfun_price', 'tradeit_price', 'swap_price', 'loot_price', 'recommend']

        with open(filename, 'r') as csvfile, tempfile:
            reader = csv.DictReader(csvfile, fieldnames=fields)
            writer = csv.DictWriter(tempfile, fieldnames=fields)
            for row in reader:
                for item in res:
                    if item.get('name') == row['name']:
                        row['loot_price'] = format(item['price'] * 0.97 / 100, '.2f')
                        break
                row = {
                    'name': row['name'],
                    'etopfun_price': row['etopfun_price'],
                    'tradeit_price': row['tradeit_price'],
                    'swap_price': row['swap_price'],
                    'loot_price': row['loot_price'],
                    'recommend': row['recommend']
                }
                writer.writerow(row)

        shutil.move(tempfile.name, filename)
    else:
        logger.error('API: {}, with errors: {}'.format(ROOT, res['errors']))
