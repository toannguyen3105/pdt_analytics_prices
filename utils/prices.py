import csv

header = ['Name', 'Price 5e', 'Price TradeIT', 'Price Swap', 'Price Loot.farm', 'Recommend']


def generate_data(items):
    etop_items = []
    for item in items:
        etop_items.append([item['name'], item['value'], '', '', '', ''])

    return etop_items


def create_price_csv(mode, items):
    with open('prices.csv', mode, encoding='UTF8', newline='') as f:
        writer = csv.writer(f)

        # write the header
        writer.writerow(header)

        # write multiple rows
        writer.writerows(generate_data(items))
