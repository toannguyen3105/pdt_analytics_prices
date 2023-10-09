import requests

from utils.prices import create_price_csv


def get_items_etopfun(account):
    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'en-US,en;q=0.9',
        'Connection': 'keep-alive',
        'Cookie': account['cookies'],
        'Referer': 'https://www.etopfun.com/en/bag/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
        'sec-ch-ua': '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Linux"',
    }

    params = {
        'appid': '730',
        'page': '1',
        'rows': '200',
        'lang': 'en',
    }

    response = requests.get('https://www.etopfun.com/api/user/inventory/730/list.do', params=params,
                            headers=headers)

    res = response.json()
    if res and res['code'] == 0:
        create_price_csv('w', res['datas']['list'])
