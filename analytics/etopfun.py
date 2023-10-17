import requests

from loggingUtil import logger
from utils.prices import create_price_csv


def get_items_etopfun(account):
    logger.warning('Get items from [ETOPFUN]')

    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'en-US,en;q=0.9',
        'Connection': 'keep-alive',
        'Cookie': '_ga=GA1.1.511772697.1696864201; locale=en; DJSP_UUID=18b14fcec853fde4e50eb5e3; SCRIPT_VERSION=29.31.06; Hm_lvt_1cb9c842508c929123cd97ecd5278a28=1697284553,1697373177,1697470874,1697555234; JSESSIONID=D2FEF6211E5D22FD08BC63BD5223596A; DJSP_USER=fELYbixIZp9V2JhJwh3kWSsptjlkwq7e9%2BsWHUlNnjSXnXTKib4Rei9lBAmUrcf1fk3KxpxRrU8o26aFfI1t8HcWSC6M2OuIK0yQ9WvfmB8%3D; _ga_TDF3LV246N=GS1.1.1697555233.10.1.1697556430.0.0.0; Hm_lpvt_1cb9c842508c929123cd97ecd5278a28=1697556431',
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

    ROOT = 'https://www.etopfun.com/api/user/inventory/730/list.do?appid=730&page=1&rows=200&lang=en'
    response = requests.get(ROOT, params=params,
                            headers=headers)

    res = response.json()
    if res and res['code'] == 0:
        mode = 'a' if account['id'] != '1' else 'w'
        create_price_csv(mode, res['datas']['list'])
    else:
        logger.error('API: {}, with errors: {}'.format(ROOT, res['errors']))
