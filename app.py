import os
import csv
from dotenv import load_dotenv

from analytics.etopfun import get_items_etopfun
from analytics.loot import update_items_loot
from analytics.recommend import recommend_all_price
from analytics.swap import update_items_swap
from analytics.tradeit import update_items_trade_it
from loggingUtil import logger

load_dotenv()

# Access environment variables
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")


def get_items_in_bag(a):
    get_items_etopfun(a)


def update_items_in_bag(a):
    update_items_trade_it(a)
    update_items_swap(a)
    update_items_loot(a)


def recommend_price():
    recommend_all_price()


ACTIVE_USER = '1'
with open('accounts.csv', newline='') as csvfile:
    logger.warning('===== START APP =====')

    accountsReader = csv.DictReader(csvfile, delimiter='|')
    for account in accountsReader:
        logger.warning('Cookie etopfun: {}'.format(account['etopfun_cookie']))

        if account['status'] == ACTIVE_USER:
            # Lay thong tin item trong bag cua etopfun
            get_items_in_bag(account)

            # Cap nhat gia cua tradeit, swap, lootfarm
            update_items_in_bag(account)

            # Cap nhat goi y
            recommend_price()

    logger.warning('===== END APP =====')
