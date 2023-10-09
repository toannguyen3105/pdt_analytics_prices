import os
import csv
from dotenv import load_dotenv

from analytics.etopfun import get_items_etopfun

load_dotenv()

# Access environment variables
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")


def get_items_in_bag(a):
    get_items_etopfun(a)


with open('accounts.csv', newline='') as csvfile:
    accountsReader = csv.DictReader(csvfile)
    for account in accountsReader:
        if account['status'] == '1':
            get_items_in_bag(account)

# https://www.etopfun.com/en/
# https://www.etopfun.com/en/bag/ - an vao deposit
# https://swap.gg/trade - hom do ben trai
# https://tradeit.gg/csgo/trade - hom do ben trai
