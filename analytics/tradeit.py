import requests
from loggingUtil import logger
from tempfile import NamedTemporaryFile
import shutil
import csv


def update_items_trade_it(account):
    logger.warning('Update price of [TRADE]')

    headers = {
        'authority': 'tradeit.gg',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'en-US,en;q=0.9',
        'cookie': account.get('tradeit_cookie'),
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

    ROOT = 'https://tradeit.gg/api/v2/inventory/my/data'
    response = requests.get(ROOT, params=params, headers=headers)

    res = response.json()
    if res["success"]:
        items = res['items']
        all_items = []
        for y in items.values():
            for x in y:
                all_items.append({
                    "name": x['name'],
                    "price": x['price']
                })
        unique_items = list({item['name']: item for item in all_items}.values())

        filename = 'prices.csv'
        tempfile = NamedTemporaryFile(mode='w', encoding='UTF8', delete=False)

        fields = [
            'name', 'etopfun_price', 'tradeit_price', 'swap_price',
            'loot_price', 'recommend', 'buff_price', 'empire_price'
        ]

        with open(filename, 'r', encoding='UTF8') as csvfile, tempfile:
            reader = csv.DictReader(csvfile, fieldnames=fields)
            writer = csv.DictWriter(tempfile, fieldnames=fields)
            for row in reader:
                for item in unique_items:
                    if item.get('name') == row['name']:
                        row['tradeit_price'] = format(item.get('price') / 100, '.2f')
                        break
                row = {
                    'name': row['name'],
                    'etopfun_price': row['etopfun_price'],
                    'tradeit_price': row['tradeit_price'] if row['tradeit_price'] else 0,
                    'swap_price': row['swap_price'],
                    'loot_price': row['loot_price'],
                    'recommend': row['recommend'],
                    'buff_price': row['buff_price'],
                    'empire_price': row['empire_price']
                }
                writer.writerow(row)

        shutil.move(tempfile.name, filename)
    else:
        logger.error('API: {}, with errors: {}'.format(ROOT, res['message']))
