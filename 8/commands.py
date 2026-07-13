def remove_item(database, history):
    product = input('Choose item to remove:\n').lower()
    if product in database:
        del database[product]
        history.append(f'Product {product} is successfully deleted.\n')
        print(f'Product {product} is successfully deleted.\n')
    else:
        print('Invalid input.\n')


def add_item(database, history):
    while True:
        product = input('Product name:\n').strip().lower()

        if product == '':
            print('Product name must not be empty!\n')
            continue

        if product in database:
            print('Product already exists!\n')
            continue

        try:
            price = int(input('Product price:\n'))
            amount = int(input('Amount added\n'))
        except ValueError:
            print('Price and amount must be numbers!\n')
            continue

        database[product] = {'cena': price, 'kolicina': amount}
        history.append(f'Product {product} is successfully added.\n')
        print(f'Product {product} is successfully added.\n')
        break


def print_database(database, history):
    history.append('Database print.\n')
    print(database)



def print_history(database, history):
    if not history:
        print('Empty history.\n')
    else:
        print('\n---Actions history---')
        for event in history:
            print(event.strip())


def delete_all(database, history):
    database.clear()
    print('Database has been cleared.')
    database.clear()
    history.append('Database cleared!')
    print('Database has been cleared!\n')


def most_expensive_product(database,history):
    if not database:
        print('Database is empty.\n')
        return

    m_e_p = None
    highest_price = 0
    for product in database:
        current_price = database[product]['cena']

        if current_price > highest_price:
            highest_price = current_price
            m_e_p = product

    print(m_e_p)


command_map = {
    'remove product': remove_item,
    'add product': add_item,
    'print database': print_database,
    'print history': print_history,
    'delete database': delete_all,
    'most expensive': most_expensive_product,
}
