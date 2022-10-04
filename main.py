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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

power_on = True


def count_change(penn, nick, dime, quar):
    count = (penn + 5*nick + 10*dime + 25*quar)/100
    return count


while power_on:
    choice = input("Please choose: (e)spresso $1.50, (l)atte $2.50, or (c)appuccino $3.00:\ne, l, c?: ")
    qua = int(input("How many quarters will you insert?: "))
    dim = int(input("How many dimes will you insert?: "))
    nic = int(input("How many nickles will you insert?: "))
    pen = int(input("How many pennies will you insert?: "))
    resources["money"] = count_change(pen, nic, dim, qua)
    if choice == "off":
        print("Goodbye")
        power_on = False
    elif choice == "report":

        print(f"Milk: {resources['milk']} mL remaining")
        print(f"Water: {resources['water']} mL remaining")
        print(f"Coffee: {resources['coffee']} g remaining")
        print(f"money: ${resources['money']} currently")
    elif choice == "e":
        print(f"{MENU['espresso']['ingredients']['water']}")
        print(f"{MENU['espresso']['ingredients']['coffee']}")
        if resources['coffee'] - MENU['espresso']['ingredients']['coffee'] > 0 \
                and resources['water'] - MENU['espresso']['ingredients']['water'] > 0 \
                and resources['money'] - MENU['espresso']['cost'] > 0:
            print('You can have a espresso!')
            resources['coffee'] = resources['coffee'] - MENU['espresso']['ingredients']['coffee']
            resources['water'] = resources['water'] - MENU['espresso']['ingredients']['water']
            resources['money'] = resources['money'] - MENU['espresso']['cost']
            if resources['money'] > 0:
                print(f"Your change is ${resources['money']}, spend it wisely")
                resources['money'] = 0
            print(resources)
        else:
            print('insufficient resources for espresso')
            if resources['coffee'] - MENU['espresso']['ingredients']['coffee'] < 0:
                print("not enough coffee")
            if resources['water'] - MENU['espresso']['ingredients']['water'] < 0:
                print("not enough water")
            if resources['money'] - MENU['espresso']['cost'] < 0:
                print(f"not enough money")
            print(f"here is your ${resources['money']} back. ")
    elif choice == "l":
        print(f"{MENU['latte']['ingredients']['water']}")
        print(f"{MENU['latte']['ingredients']['coffee']}")
        print(f"{MENU['latte']['ingredients']['milk']}")
        if resources['coffee'] - MENU['latte']['ingredients']['coffee'] > 0 \
                and resources['water'] - MENU['latte']['ingredients']['water'] > 0 \
                and resources['milk'] - MENU['latte']['ingredients']['milk'] > 0 \
                and resources['money'] - MENU['latte']['cost'] > 0:
            print('You can have a latte!')
            resources['coffee'] = resources['coffee'] - MENU['latte']['ingredients']['coffee']
            resources['water'] = resources['water'] - MENU['latte']['ingredients']['water']
            resources['milk'] = resources['milk'] - MENU['latte']['ingredients']['milk']
            resources['money'] = resources['money'] - MENU['latte']['cost']
            print(resources)
            if resources['money'] > 0:
                print(f"Your change is ${resources['money']}, spend it wisely")
                resources['money'] = 0
            print(resources)
        else:
            print('insufficient resources for Latte')
            if resources['coffee'] - MENU['latte']['ingredients']['coffee'] < 0:
                print("not enough coffee")
            if resources['water'] - MENU['latte']['ingredients']['water'] < 0:
                print("not enough water")
            if resources['milk'] - MENU['latte']['ingredients']['milk'] < 0:
                print("not enough milk")
            if resources['money'] - MENU['latte']['cost'] < 0:
                print(f"not enough money")
            print(f"here is your ${resources['money']} back. ")
    elif choice == "c":
        print(f"{MENU['cappuccino']['ingredients']['water']}")
        print(f"{MENU['cappuccino']['ingredients']['coffee']}")
        print(f"{MENU['cappuccino']['ingredients']['milk']}")
        if resources['coffee'] - MENU['cappuccino']['ingredients']['coffee'] > 0 \
                and resources['water'] - MENU['cappuccino']['ingredients']['water'] > 0 \
                and resources['milk'] - MENU['cappuccino']['ingredients']['milk'] > 0 \
                and resources['money'] - MENU['cappuccino']['cost'] > 0:
            print('You can have a cappuccino!')
            resources['coffee'] = resources['coffee'] - MENU['cappuccino']['ingredients']['coffee']
            resources['water'] = resources['water'] - MENU['cappuccino']['ingredients']['water']
            resources['milk'] = resources['milk'] - MENU['cappuccino']['ingredients']['milk']
            resources['money'] = resources['money'] - MENU['cappuccino']['cost']
            print(resources)
            if resources['money'] > 0:
                print(f"Your change is ${resources['money']}, spend it wisely")
                resources['money'] = 0
            print(resources)
        else:
            print('insufficient resources for cappuccino')
            if resources['coffee'] - MENU['cappuccino']['ingredients']['coffee'] < 0:
                print("not enough coffee")
            if resources['water'] - MENU['cappuccino']['ingredients']['water'] < 0:
                print("not enough water")
            if resources['milk'] - MENU['cappuccino']['ingredients']['milk'] < 0:
                print("not enough milk")
            if resources['money'] - MENU['cappuccino']['cost'] < 0:
                print(f"not enough money")
            print(f"here is your ${resources['money']} back. ")
