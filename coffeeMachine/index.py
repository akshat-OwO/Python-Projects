MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 18,
    "money": 0
}

running = True

def processCoins():
    print('Insert Coins.')
    quarters = int(input('Quarter(s): ')) * 0.25
    dimes = int(input('Dime(s): ')) * 0.10
    nickles = int(input('Nickle(s): ')) * 0.05
    pennies = int(input('Penny(s): ')) * 0.01
    return round(quarters + dimes + nickles + pennies, 2)

def checkTransaction(order, total):
    if total < MENU[order]["cost"]:
        print("Sorry theres not enough money. Money refunded.")
        return False
    elif total > MENU[order]["cost"]:
        change = round(total - MENU[order]["cost"], 2)
        resources["money"] += MENU[order]["cost"]
        print(f"Here is ${change} in change")
        return True
    else:
        resources["money"] += total
        return True

def checkResource(order):
    for resource in resources:
        if resource == 'money':
            continue
        if resources[resource] < MENU[order]['ingredients'][resource]:
            print(f"Sorry theres not enough {resource}")
            return False
    return True

def makeCoffee(order):
    for resource in resources:
        if resource == 'money':
            continue
        resources[resource] -= MENU[order]['ingredients'][resource]
    print(f'Here is your {order}. Enjoy!')


while running:
    order = input('What would you like? (espresso/latte/cappuccino): ')

    if order == 'off':
        running = False
    elif order == 'report':
        for resource in resources:
            print(f'{resource}: {resources[resource]}')
    elif order == 'espresso':
        if checkResource(order):
            if checkTransaction(order, processCoins()):
                makeCoffee(order)
    elif order == 'latte':
        if checkResource(order):
            if checkTransaction(order, processCoins()):
                makeCoffee(order)
    elif order == 'cappuccino':
        if checkResource(order):
            if checkTransaction(order, processCoins()):
                makeCoffee(order)