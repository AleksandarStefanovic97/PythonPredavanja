delivery_cost = {
    'Beograd': 500,
    'Novi Sad': 700,
    'Nis': 800,
}




def calculate_delivery(location):
    if location in delivery_cost:
        print(f'Delivery cost is: {delivery_cost[location]}')

    else:
        print('Incorrect location')


calculate_delivery('Beograd')