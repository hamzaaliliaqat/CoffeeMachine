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


def is_resource_sufficient(order_ingridients):
    for item in order_ingridients:
        if order_ingridients[item] >= resources[item]:
            print(f"Sorry {item} is not enough.")
            return False
    return True


def process_payment():
    print("Please insert the coins.")
    quarters = float(input("How many quarters? "))
    dimes = float(input("How many dimes? "))
    nickels = float(input("How many nickels? "))
    pennies = float(input("How many pennies? "))

    quarter = 0.25
    dime = 0.10
    nickel = 0.05
    penny = 0.01

    total_quarters = quarter * quarters
    total_dimes = dime * dimes
    total_nickels = nickel * nickels
    total_pennies = penny * pennies
    payment = total_pennies + total_dimes + total_nickels + total_quarters
    return payment


def is_transaction_successful(money_recieved, drink_cost):
    if money_recieved >= drink_cost:
        change = round(money_recieved - drink_cost, 2)
        print(f"Here is your ${change} change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry the money is insufficient. Payment refunded.")
        return False


def make_coffee(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
        print(f"Here is your {order} ☕.")
        return


profit = 0
is_on = True
while is_on:

    order = input("What would you like to have? Espresso, Latte or Cappuccino. ").lower()

    if order == "off":
        is_on = False
    elif order == "report":
        print(f"Water: {resources['water']}")
        print(f"Milk: {resources['milk']}")
        print(f"Coffee: {resources['coffee']}")
        print(f"Profit: {profit}")
    else:
        drink = MENU[order]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_payment()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(order, drink["ingredients"])

# Input 'off' to end the process and 'report' to check the available resources.
