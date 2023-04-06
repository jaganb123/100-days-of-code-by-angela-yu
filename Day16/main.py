from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
machine = CoffeeMaker()
money = MoneyMachine()
continue_serve = True
while continue_serve:
    user_option = input(f"What would you like? ({menu.get_items()}) ").lower()
    if user_option == 'off':
        print("Shutting down... Bye...")
        continue_serve = False
        continue
    if user_option == 'report':
        machine.report()
        money.report()
        continue
    else:
        coffee =  menu.find_drink(user_option)
        if machine.is_resource_sufficient(coffee) and money.make_payment(coffee.cost):
            machine.make_coffee(coffee)

