recipes = {
    "espresoo": {"water": 50, "coffee": 18, "milk": 0},
    "latte": {"water": 200, "coffee": 24, "milk": 150},
    "cappuccino": {"water": 250, "coffee": 24, "milk": 100},
}
resources = {"water": 300, "coffee": 100, "milk": 200}
coins = {
    'penny': 1,
    'dime': 10,
    'nickel': 5,
    'quater': 25
}


# print report resources left
# check if possible of a drink
# process the coins
# complete the transactions
# make the coffee
class CoffeeMachine:

    def __init__(self):
        self.resources = {"water": 300, "coffee": 100, "milk": 200, "money": 0}
        self.recipes = {
            "espresso": {"water": 50, "coffee": 18, "milk": 0},
            "latte": {"water": 200, "coffee": 24, "milk": 150},
            "cappuccino": {"water": 250, "coffee": 24, "milk": 100},
        }
        self.cost = {
            "espresso": 1.5,
            "latte": 2.5,
            "cappuccino": 3
        }
        self.coins = {
            'penny': 0.01,
            'dime': 0.10,
            'nickel': 0.05,
            'quarter': 0.25
        }
        self.start()

    def start(self):
        while True:
            print("What would you like? (espresso/latte/cappuccino):")
            choice = input()
            if choice == "report":
                self.print_report()
            elif choice == "off":
                break
            elif choice in self.recipes.keys():
                self.check_transaction(dish=choice)
            else:
                print("Invalid Input")

    def print_report(self):
        for resource, quantity in self.resources.items():
            print(f"{resource.title()}: {quantity}")

    def check_resources(self, dish):
        for ingredient, quantity in self.recipes[dish].items():
            if self.resources[ingredient] < quantity:
                return f"Sorry there is not enough {ingredient}."
        return ""

    def process_coins(self):
        amount = 0
        for coin, value in self.coins.items():
            amount += int(input(f"Please enter the number of {coin.title()}")) * value
        return amount

    def check_transaction(self, dish):
        resources_info = self.check_resources(dish)
        if resources_info == "":
            take_money = self.process_coins()
            if take_money < self.cost[dish]:
                print("Sorry that's not enough money. Money refunded.")
            else:
                refund = take_money - self.cost[dish]
                if refund != 0:
                    print(f"Here is ${refund} dollars in change.")
                self.make_coffee(dish)

        else:
            print(resources_info)

    def make_coffee(self, dish):
        self.resources['money'] += self.cost[dish]
        for ingredient, quantity in self.recipes[dish].items():
            self.resources[ingredient] -= quantity
        print(f"Here is your {dish.title()}. Enjoy!")


if __name__ == "__main__":
    CoffeeMachine()
