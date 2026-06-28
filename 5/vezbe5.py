def item_add():

    proizvodi = []

    while len(proizvodi) < 3:
        item_input = input('Unesite proizvod: ')
        proizvodi.append(item_input)

    print(proizvodi)

item_add()