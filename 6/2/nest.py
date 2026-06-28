shops = {
    'Maxi' : {
        'hleb' : 100,
        'mleko' : 97,
        'sok' : 120
    },
    'Cili' : {
        'hleb' : 102,
        'mleko' : 95,
        'sok' : 121
    },
    'Metro' : {
        'hleb' : 104,
        'mleko' : 96,
        'sok' : 123
    },
    'FreeShop' : {
        'mleko' : 96,
        'sok' : 123
    },

}
hleb_prices = []
highest_price = 0
highest_shop = ''

for shop, items in shops.items():
    if 'hleb' in items:
        price = items['hleb']
        hleb_prices.append(items['hleb'])
    if price > highest_price:
        highest_price = price
        highest_shop = shop

avr = (sum(hleb_prices)) / len(hleb_prices)

print(f'Prosecna cena hleba je: {avr} dinara, dok je najvisa cena u prodavnici "{highest_shop}" i iznosi {highest_price} dinara.')
