import json

with open('catalog.json', 'r') as f:
    catalog_data = json.load(f)

jacket_data = [item for item in catalog_data if item['name'] == 'jacket']

if jacket_data:
    
    quantity = len(jacket_data)

    prices = [item['price'] for item in jacket_data]

    max = max(prices)

    min = min(prices)

    print("jacketの個数: {}".format(quantity))
    print("jacketの最高価格: {}".format(max))
    print("jacketの最低価格: {}".format(min))
else:
    print("データがありません")
