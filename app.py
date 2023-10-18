import os
from dotenv import load_dotenv

from accounts import accounts
from analytics.etopfun import get_items_etopfun
from analytics.loot import update_items_loot
from analytics.recommend import recommend_all_price
from analytics.swap import update_items_swap
from analytics.tradeit import update_items_trade_it
from loggingUtil import logger

load_dotenv()


def get_items_in_bag(a):
    get_items_etopfun(a)


def update_items_in_bag(a):
    update_items_trade_it(a)
    update_items_swap(a)
    update_items_loot(a)


def recommend_price():
    recommend_all_price()


ACTIVE_USER = 1
logger.warning('===== START APP =====')

for account in accounts:
    logger.warning('Cookie etopfun: {}'.format(account['etopfun_cookie']))

    if account['status'] == ACTIVE_USER:
        # Lay thong tin item trong bag cua etopfun
        get_items_in_bag(account)

        # Cap nhat gia cua tradeit, swap, lootfarm
        update_items_in_bag(account)

        # Cap nhat goi y
        recommend_price()

logger.warning('===== END APP =====')
