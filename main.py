MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
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
profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def resource_check(ingredients):
    for item in ingredients:
        if ingredients[item] >= resources[item]:
            print(f'Sorry there is not enough {item}.')
            return False
    return True


def process_coins():
    print('Please input coins.')
    total = int(input('How many quarters?: ')) * .25
    total += int(input("How many dimes?: ")) * .1
    total += int(input('How many nickles?: ')) * .05
    total += int(input('How many pennies?: ')) * .01
    return total


def transaction_success(money_entered, cost):
    if money_entered < cost:
        print("Sorry, that's not enough money. Money refunded.")
        return False
    else:
        global profit
        profit += cost
        change = round(money_entered - cost, 2)
        print(f'Here is ${change} dollars in change.')
        return True


def make_coffee(drink, ingredients):
    for item in ingredients:
        resources[item] -= ingredients[item]
    print(f'Here is your {drink}. Enjoy!')


running = True
while running:
    choice = input("What would you like?: (espresso/latte/cappuccino)").lower()
    if choice == "off":
        running = False
    elif choice == "report":
        print(f'Water: {resources["water"]}ml')
        print(f'Milk: {resources["milk"]}ml')
        print(f'coffee: {resources["coffee"]}g')
        print(f'Money: ${profit}')
    else:
        if resource_check(MENU[choice]['ingredients']):
            payment = process_coins()
            if transaction_success(payment, MENU[choice]['cost']):
                make_coffee(choice, MENU[choice]["ingredients"])