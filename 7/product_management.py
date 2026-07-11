import products
import commands


while True:
    command = input('Choose action (remove product / add product / print database / exit): ').strip().lower()

    match command:
        case 'remove product':
            commands.remove_item(products.products)

        case 'add product':
            commands.add_item(products.products)

        case 'print database':
            commands.print_database(products.products)

        case 'exit':
            break

        case _:
            print(f'Error: "{command}" is not a valid command. Please try again.')





