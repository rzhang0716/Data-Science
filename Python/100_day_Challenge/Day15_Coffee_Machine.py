#  Prompt user by asking: What would you like? (espresso/latte/cappuccino):
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
input_list = ["espresso", "latte", "cappuccino", "report", "off"]
coffee_list = ["espresso", "latte", "cappuccino"]
machine_resource = {'Water': 300, 'Milk': 200, 'Coffee': 100, 'Money': 0}


# Check resources sufficient
# machine_water = 300, machine_milk = 200, machine_coffee = 100)
def resource_check(coffee):

    coffee_type_ing = MENU[coffee]["ingredients"]
    water_ing = coffee_type_ing["water"]
    milk_ing = coffee_type_ing["milk"]
    coffee_ing = coffee_type_ing["coffee"]

    if machine_resource['Water'] >= water_ing and machine_resource['Milk'] >= milk_ing and machine_resource['Coffee'] >= coffee_ing:
        machine_resource['Water'] -= water_ing
        machine_resource['Milk'] -= milk_ing
        machine_resource['Coffee'] -= coffee_ing
    elif machine_resource['Water'] < water_ing:
        print('Sorry there is not enough water.')
        quit()
    elif machine_resource['Milk'] < milk_ing:
        print('Sorry there is not enough milk.')
        quit()
    elif machine_resource['Coffee'] < coffee_ing:
        print('Sorry there is not enough coffee.')
        quit()


# Process coins.
def coins():
    print("Please insert coins.")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickels = int(input("How many nickels?: "))
    pennies = int(input("How many pennies?: "))
    user_coin = (25 * quarters + 10 * dimes + 5 * nickels + pennies) / 100
    return user_coin


# Check transaction successful?
def transaction_result(coffee):
    coffee_cost = MENU[coffee]["cost"]
    user_coin = coins()
    if coffee_cost <= user_coin:
        charge = round(user_coin - coffee_cost,1)
        machine_resource['Money'] += coffee_cost
        print(f"Here is your {coffee} ☕. Enjoy!")
        print(f"Here is ${charge} in charge")
    else:
        print("Sorry that's not enough money. Money refunded")
        quit()


def coffee_machine_func():
    user_ins = input("What would you like? (espresso/latte/cappuccino):\n")
    if user_ins in input_list:

        # Turn off the machine when input off
        if user_ins == 'off':
                quit()

        # Show the ingredients left when input report
        elif user_ins == 'report':
            print(f"Water: {machine_resource['Water']}ml")
            print(f"Milk: {machine_resource['Milk']} ml")
            print(f"Coffee: {machine_resource['Coffee']} ml")
            print(f"Money: ${machine_resource['Money']}")
            coffee_machine_func()

        # Coffee
        elif user_ins in coffee_list:
            coffee_type = user_ins
            resource_check(coffee=coffee_type)
            transaction_result(coffee=coffee_type)
            coffee_machine_func()
    else:
        quit()


coffee_machine_func()
