# Coffee Machine:


resources = {
    "water": 300,
    "coffee": 100,
    "milk": 200,
    "money": 0
}


def order_coffee(coffee):
    if coffee == "espresso":
        quarters = float(input("how many quarters?"))
        dims = float(input("how many dims?"))
        nickles = float(input("how many nickles?"))
        pennies = float(input("how many pennies?"))
        transaction = 0.25 * quarters + 0.1 * dims + 0.05 * nickles + 0.01 * pennies
        if resources["water"] > 50 and resources["coffee"] > 18 and transaction > 1.5:
            if transaction > 1.5:
                print(f"Here's your change: {transaction - 1.5}")
            resources["water"] = resources["water"] - 50
            resources["coffee"] = resources["coffee"] - 18
            print("here your coffee!")
        else:
            print("The resource is insufficient!")

    elif coffee == "latte":
        quarters = float(input("how many quarters?"))
        dims = float(input("how many dims?"))
        nickles = float(input("how many nickles?"))
        pennies = float(input("how many pennies?"))
        transaction = 0.25 * quarters + 0.1 * dims + 0.05 * nickles + 0.01 * pennies
        if resources["water"] > 200 and resources["coffee"] > 24 and resources["milk"] > 150 and transaction > 2.4:
            if transaction > 2.4:
                print(f"here's your change: {transaction - 2.4}")
            resources["water"] = resources["water"] - 200
            resources["coffee"] = resources["coffee"] - 24
            resources["milk"] = resources["milk"] - 150
            print("here your coffee!")
        else:
            print("The resource is insufficient!")
    else:
        quarters = float(input("how many quarters?"))
        dims = float(input("how many dims?"))
        nickles = float(input("how many nickles?"))
        pennies = float(input("how many pennies?"))
        transaction = 0.25 * quarters + 0.1 * dims + 0.05 * nickles + 0.01 * pennies
        if resources["water"] > 250 and resources["coffee"] > 24 and resources["milk"] > 100 and transaction == 3:
            if transaction > 3:
                print(f"here's your change: {transaction - 3}")
            resources["water"] = resources["water"] - 250
            resources["coffee"] = resources["coffee"] - 24
            resources["milk"] = resources["milk"] - 100
            print("here your coffee!")
        else:
            print("The resource is insufficient!")

while True:
    user_input = input("what coffee would you like?")
    if user_input == "report":
        for resource in resources:
            print(f"{resource}: {resources[resource]}")
    elif user_input == "quit":
        break
    else:
        order_coffee(user_input)

