def remove_item(database):
    product = input('Choose item to remove: ').lower()
    if product in database:
        del database[product]
    else:
        print('Invalid input.')

def add_item(database):
    while True:
        product = input('Product name: ').strip().lower()

        if product == '':
            print('Product name must not be empty!')
            continue

        if product in database:
            print('Product already exists!')
            continue

        try:
            price = int(input('Product price: '))
            amount = int(input('Amount added'))
        except ValueError:
            print('Price and amount must be numbers!')
            continue

        database[product] = {'cena': price, 'kolicina': amount}
        print(f'Product {product} is successfully added.')
        break

def print_database(database):
    print(database)
