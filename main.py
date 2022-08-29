from data import MENU, resources

reso = resources


def show_resources(r):
    for res in r:
        print(f"{res}: {r[res]}")


def make_coffee(x, resources):
    if (resources['water'] >= MENU[x]["ingredients"]["water"] and
            resources['coffee'] >= MENU[x]["ingredients"]["coffee"] and
            resources['milk'] >= MENU[x]["ingredients"]["milk"]):
        cost = MENU[x]['cost']
        print(f"Please insert {cost}")
        coins = insert_coins()
        while coins <= cost:
            print(f"Not enough coins. You have entered {coins}")
            coins = insert_coins()
        print(f"Your change: {round(coins - cost, 2)}")
        print(f"Here is your {x}")

        resources['water'] -= MENU[x]["ingredients"]["water"]
        resources['coffee'] -= MENU[x]["ingredients"]["coffee"]
        resources['milk'] -= MENU[x]["ingredients"]["milk"]
        resources['coins'] += cost
    else:
        print("Not enough resources")
    return resources


def insert_coins():
    pennies = int(input("How many pennies?: "))
    nickles = int(input("How many nickles?: "))
    dimes = int(input("How many dimes?: "))
    quarters = int(input("How many quarters?: "))
    return 0.01 * pennies + 0.05 * nickles + 0.10 * dimes + 0.25 * quarters


active = 1
while active:
    decision = input("What would you like? (espresso/latte/cappuccino): ")

    if decision == "off":
        active = 0
    elif decision == "report":
        show_resources(reso)
    elif decision == "espresso" or decision == "latte" or decision == "cappuccino":
        reso = make_coffee(decision, reso)
    else:
        print("Bad input")
