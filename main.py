from data import *
import time
totalMoney = 0
while True:
    restartNeed = False
    selectedCoffee = input("Which would you like to buy? (espresso, latte, cappuccino): ")
    if selectedCoffee == "off":
        print("BYE!")
        break
    elif selectedCoffee == "report":
        for resource in resources:
            print(f" {resource}: {resources[resource]}")
        print(f" Money: {totalMoney}")
        continue
    elif not selectedCoffee in MENU.keys():
        print("invalid input!")
        continue
    for resource in resources:
        if selectedCoffee == "espresso" and resource == "milk":
            continue

        elif MENU[selectedCoffee]["ingredients"][resource] > resources[resource]:
            print(f"Not enough {resource}!")
            restartNeed = True

    if restartNeed: continue
    print(f"OK! total cost: {MENU[selectedCoffee]['cost']}")
    quarters = int(input("How many quarters: "))
    dimes = int(input("How many dimes: "))
    nickles = int(input("How many nickles: "))
    pennies = int(input("How many pennies: "))

    moneyEntered = quarters * 0.25 + dimes * 0.10 + nickles * 0.05 + pennies * 0.01
    print(moneyEntered)
    if MENU[selectedCoffee]["cost"] > moneyEntered:
        print("Not enough money! All moneys refunded")
        moneyEntered = 0
        continue
    remainder = moneyEntered - MENU[selectedCoffee]["cost"]
    totalMoney += MENU[selectedCoffee]["cost"]
    print(f"Coffee on the way! BTW {remainder}$ refunded")
    time.sleep(3)
    print(f"Here is your {selectedCoffee}. Enjoy!")
    for resource in resources:
        if selectedCoffee == "espresso" and resource == "milk":
            continue
        resources[resource] -= MENU[selectedCoffee]["ingredients"][resource]
