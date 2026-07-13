import products
import commands


options_list = list(commands.command_map.keys()) + ['exit']
prompt_string = " / ".join(options_list)

while True:
    command = input(f'Choose action ({prompt_string}):\n').strip().lower()
    if command == exit:
        print('Goodbye.')
        break

    elif command in commands.command_map:
        action_function = commands.command_map[command]
        action_function(products.products, products.action_history)

    else:
        print(f'Error: {command} is not valid command.')
        print("-----------------------\n")







