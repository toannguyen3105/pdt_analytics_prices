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
        'cookie': 'i18n_redirected=en; _scid=198c3981-3e0a-4f3a-a43d-0c63b6dcee65; sessionid=s%3A5ES3rMzULymGBzJyBWNezpInXcxPY7rb.QHDvghUJI3o57oXRcWxm7mCI%2F8AWVDSofA38tqcvliI; vuex={%22inventory%22:{%22siteInventory%22:{%22filters%22:{%22gameId%22:730}}%2C%22userInventory%22:{%22filters%22:{}}}%2C%22users%22:{%22analyticsAttributes%22:null}}; _ga=GA1.1.472040037.1697472600; ga4={"client_id":"472040037.1697472600"}; _rdt_uuid=1697472600369.10b0bb31-f15e-4966-9a55-ab7db108e5d4; _tt_enable_cookie=1; _ttp=xmmnByPZas_rlMl5oiwFIi8Ddzh; _sctr=1%7C1697389200000; tmr_lvid=03be2befee1a1eccbd6b7bd2184c9be6; tmr_lvidTS=1697472600567; _ym_uid=1697472601214323686; _ym_d=1697472601; _ym_isad=2; _fbp=fb.1.1697472602360.392532867; socketuuid=975c5519-7bd5-44b8-9c78-706be18a4abd; moe_uuid=314ef520-bd8b-4700-9aad-74fef7afc63e; tmr_detect=0%7C1697472682369; __stripe_mid=17666093-1e15-4289-befd-b38ca3f8611087b342; __stripe_sid=f3d1f4c8-9150-49fa-b275-310113383d4cf563ed; OPT_IN_SHOWN_TIME=1697472799369; SOFT_ASK_STATUS=%7B%22actualValue%22%3A%22shown%22%2C%22MOE_DATA_TYPE%22%3A%22string%22%7D; _uetsid=74c1f4606c3e11eea699e3732089e824; _uetvid=74c218406c3e11ee8f8c579f11a0078a; _scid_r=198c3981-3e0a-4f3a-a43d-0c63b6dcee65; _ga_RFHNPQTN51=GS1.1.1697472600.1.1.1697472973.59.0.0',
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
        tempfile = NamedTemporaryFile(mode='w', delete=False)

        fields = ['name', 'etopfun_price', 'tradeit_price', 'swap_price', 'loot_price', 'recommend']

        with open(filename, 'r', encoding='UTF8') as csvfile, tempfile:
            reader = csv.DictReader(csvfile, fieldnames=fields)
            writer = csv.DictWriter(tempfile, fieldnames=fields)
            for row in reader:
                for item in unique_items:
                    if item.get('name') == row['name']:
                        row['tradeit_price'] = format(item['price'] / 100, '.2f')
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
        logger.error('API: {}, with errors: {}'.format(ROOT, res['message']))
