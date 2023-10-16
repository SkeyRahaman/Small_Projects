from typing import Any


class MenuItem:

    def __init__(self, name, water, milk, coffee, cost):
        self.name = name
        self.cost = cost
        self.ingredients = {
            "water": water,
            "milk": milk,
            "coffee": coffee
        }


class Menu:
    def __init__(self):
        self.items = {"latte": MenuItem(name="latte", cost=2.5, water=200, coffee=24, milk=150),
                      "espresso": MenuItem(name="espresso", cost=2.5, water=50, coffee=18, milk=0),
                      "cappuccino": MenuItem(name="cappuccino", cost=2.5, water=250, coffee=24, milk=100)
                      }

    def get_items(self) -> str:
        """
        Returns all the names of the available menu items as a concatenated string.
        """
        return "/".join(self.items.keys())

    def find_drink(self, order_name) -> Any | None:
        """
        Parameter order_name: (str) The name of the drinks order.
        Searches the menu for a particular drink by name. Returns a MenuItem object if it exists,
        otherwise returns None.
        """
        if order_name not in self.items:
            print("Sorry that item is not available.")
            return None
        return self.items[order_name]


class CoffeeMaker:

    def __init__(self):
        self.resources = {"water": 300, "coffee": 100, "milk": 200}

    def print_report(self):
        """Prints a report of all resources"""
        for resource, quantity in self.resources.items():
            print(f"{resource.title()}: {quantity}")

    def check_resources(self, drink: MenuItem) -> bool:
        """
        Parameter drink: (MenuItem) The MenuItem object to make.
        :param drink: menuItem
        :return:Returns True when the drink order can be made, False if ingredients are insufficient.
        """
        output = True
        for ingredient, quantity in drink.ingredients.items():
            if self.resources[ingredient] < quantity:
                print(f"Sorry there is not enough {ingredient}.")
                output = False
        return output

    def make_coffee(self, drink: MenuItem):
        for ingredient, quantity in drink.ingredients.items():
            self.resources[ingredient] -= quantity
        print(f"Here is your {drink.name.title()} ☕️. Enjoy!")


class MoneyMachine:
    COIN_VALUES = {
        'pennies': 1,
        'dimes': 10,
        'nickles': 5,
        'quarters': 25
    }

    def __init__(self):
        self.profit = 0

    def report(self):
        """Prints the current profit"""
        print(f"Current Profit :- {self.profit}")

    def make_payment(self, cost) -> bool:
        """
        :param cost: (float) The cost of the drink.
        :return: Returns True when payment is accepted, or False if insufficient.
        """
        money_received = 0
        for coin, value in self.COIN_VALUES.items():
            money_received += int(input(f"Please enter the number of {coin.title()}")) * value
        if money_received < cost:
            print("Sorry that's not enough money. Money refunded.")
            return False
        else:
            refund = money_received - cost
            if refund != 0:
                print(f"Here is ${refund} dollars in change.")
            self.profit += cost
            return True


def main():
    moneymachine = MoneyMachine()
    coffeemachine = CoffeeMaker()
    menu = Menu()
    while True:
        choice = input("What would you like? (espresso/latte/cappuccino):")
        drink = menu.find_drink(choice)
        if drink:
            # check resource
            if not coffeemachine.check_resources():
                continue
            # collect money
            if not moneymachine.make_payment(drink.cost):
                continue
            # make coffee
            coffeemachine.make_coffee(drink)
        elif choice == "report":
            coffeemachine.print_report()
            moneymachine.report()
        elif choice == "off":
            break
        else:
            print("Invalid Input")


if __name__ == "__main__":
    main()
