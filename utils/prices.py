import csv
import os

header = [
    'name', 'etopfun_price', 'tradeit_price', 'swap_price',
    'loot_price', 'recommend', 'buff_price', 'empire_price'
]


def generate_data(items):
    etop_items = []
    for item in items:
        etop_items.append([item['name'], item['value'], '', '', '', ''])

    return etop_items


def create_price_csv(mode, items):
    ANALYTICS_FILENAME = os.getenv("ANALYTICS_FILENAME")

    with open(ANALYTICS_FILENAME, mode, encoding='UTF8', newline='') as f:
        writer = csv.writer(f)

        # write the header
        if mode == 'w':
            writer.writerow(header)

        # write multiple rows
        writer.writerows(generate_data(items))


def calculate_price(price, rate):
    return format(float(price) / float(rate), '.2f')
