from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

while True:
    order = input(f"What would you like? ({Menu().get_items()}): ")
    if order == "off":
        break
    elif order == "report":
        CoffeeMaker().report()
        MoneyMachine().report()
    else:
        if MoneyMachine().make_payment(Menu().find_drink(order).cost):
            drink = Menu().find_drink(order)
            coffee_maker = CoffeeMaker()
            if coffee_maker.is_resource_sufficient(drink):
                coffee_maker.make_coffee(drink)
