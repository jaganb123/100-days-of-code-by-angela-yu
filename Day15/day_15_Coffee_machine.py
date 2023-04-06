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
    "water": 1000,
    "milk": 500,
    "coffee": 100,
}

# TODO 1: Prompt user by asking “ What would you like? (espresso/latte/cappuccino): ”
def serve_drink(coffee):
    for i,j in MENU[coffee]['ingredients'].items():
        resources[i] -= j
    print(f'Here is your {coffee}. Enjoy!')

def transaction_check(coffee, money):
    if money > MENU[coffee]['cost']:
        refund = money - MENU[coffee]['cost']
        print(f"here is the change ${round(refund, 2)}.")
        resources['money'] = resources.get('money', 0) + MENU[coffee]['cost']
        return True
    else :
        print(f"Sorry that's not enough money. Money refunded. ${money}")
        return False
def resource_check(coffee):
    ingredients = MENU[coffee]["ingredients"]
    for i in ['water', 'milk', 'coffee']:
        if not resources.get(i) >= ingredients.get(i,0):
            print(f"Sorry there is not enough {i}")
            return False
    print("all ingredients available")
    return True

def coffee_selected(coffee):
    ingredients = MENU[coffee]["ingredients"]
    cost = MENU[coffee]["cost"]
    isavailable = resource_check(coffee)
    if isavailable:
        denomination = [0.25, 0.10, 0.05, 0.01]
        coins = []
        coins.append(int(input("insert quaters : ")))
        coins.append(int(input("insert dimes : ")))
        coins.append(int(input("insert nickels : ")))
        coins.append(int(input("insert pennies : ")))
        for i in range(0, 4):
            coins[i] = denomination[i] * coins[i]
        total_money = sum(coins)
        if transaction_check(coffee=coffee, money=total_money):
            serve_drink(coffee)


#def collect_money():



def coffee_machine():
    machine_on = True
    while machine_on:
        user_input = input(" What would you like? (espresso $1.5/latte $2.5/cappuccino $3): ").lower()

        if user_input == 'off':
            print('Shutting down...... bye...')
            machine_on = False
            continue
        if user_input == 'report':
            print(f"Water  : {resources['water']}ml\nMilk   : {resources['milk']}ml\nCoffee : {resources['coffee']}g\nMoney  : ${resources.get('money', 0)}")
            continue
        if user_input in ['latte', 'espresso', 'cappuccino']:
            coffee_selected(coffee=user_input)
        else:
            print("Wrong input...")

coffee_machine()
here is the 5 cursers hahaha!!!!!!!!!!!!
here is the 5 cursers hahaha!!!!!!!!!!!!
here is the 5 cursers hahaha!!!!!!!!!!!!
here is the 5 cursers hahaha!!!!!!!!!!!!
here is the 5 cursers hahaha!!!!!!!!!!!!