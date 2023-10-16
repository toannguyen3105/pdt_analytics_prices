import os
from tempfile import NamedTemporaryFile
import csv
import shutil
from loggingUtil import logger


def recommend_all_price():
    logger.warning('Recommend website')

    ETOPFUN_RATE = os.getenv("ETOPFUN_RATE")
    TRADEIT_RATE = os.getenv("TRADEIT_RATE")
    SWAP_RATE = os.getenv("SWAP_RATE")
    LOOT_RATE = os.getenv("LOOT_RATE")

    filename = 'prices.csv'
    tempfile = NamedTemporaryFile(mode='w', delete=False)

    fields = ['name', 'etopfun_price', 'tradeit_price', 'swap_price', 'loot_price', 'recommend']

    with open(filename, 'r', encoding='UTF8') as csvfile, tempfile:
        reader = csv.DictReader(csvfile, fieldnames=fields)
        writer = csv.DictWriter(tempfile, fieldnames=fields)
        for row in reader:
            if row['name'] == 'name':
                writer.writerow(row)
                continue
            if not row['etopfun_price'] or not row['tradeit_price'] or not row['swap_price'] or not row['loot_price']:
                logger.error(
                    'Errors!!! Item {} has etopfun price: {}, tradeit price: {}, swap price: {}, loot price: {}'.format(
                        row['name'],
                        row['etopfun_price'],
                        row['tradeit_price'],
                        row['swap_price'],
                        row['loot_price']
                    )
                )
                return

            etopfun_price = format(float(ETOPFUN_RATE) * float(row['etopfun_price']), '.2f')
            tradeit_price = format(float(TRADEIT_RATE) * float(row['tradeit_price']), '.2f')
            swap_price = format(float(SWAP_RATE) * float(row['swap_price']), '.2f')
            loot_price = format(float(LOOT_RATE) * float(row['loot_price']), '.2f')

            x = max(etopfun_price, tradeit_price, swap_price, loot_price)

            if x == etopfun_price:
                row['recommend'] = 'etopfun'
            elif x == tradeit_price:
                row['recommend'] = 'tradeit'
            elif x == swap_price:
                row['recommend'] = 'swap'
            else:
                row['recommend'] = 'loot'

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
