MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.8
    }
}

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def is_resource_sufficient(order_ingredients):
    """return True if ingredients are sufficient"""
    for ingredient in order_ingredients:
        if order_ingredients[ingredient] > resources[ingredient]:
            print(f"sorry we ran out the {ingredient} ingredient")
            return False
    return True


def process_coin():
    """return calculated coins in total"""
    print("please insert coins.")
    total = int(input("how many quarters? ")) * 0.25
    total += int(input("how many dimes? ")) * 0.10
    total += int(input("how many nickles? ")) * 0.05
    total += int(input("how many pennies? ")) * 0.01
    return total

def is_transaction_successful(money_recieved, drink_cost ):
    if money_recieved >= drink_cost:
        change = round(money_recieved - drink_cost, 2)
        print(f"here's your change: {change}")
        global profit
        profit += money_recieved
        return True
    else:
        print("Sorry that's not enough money, money refunded")
        return False

def make_coffee(drink_name, order_ingredient):
    """deduct the ingredient"""
    for item in order_ingredient:
        resources[item] -= order_ingredient[item]
    print(f"Heres your {drink_name}-coffee.")

is_on = True
while is_on:
    choice = input("what would you like? (espresso/cappuccino/latte)")
    if choice == "off":
        is_on = False
    if choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}gr")
        print(f"Money: {profit}$")
    else:
        drink = MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coin()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])
