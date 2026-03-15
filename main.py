from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
from art import LOGO

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

is_on = True

print(LOGO)
print("☕️ Welcome to the Coffee Machine! ☕️")

print("\n📋 MENU:")
for item in menu.menu:
    print(f"   • {item.name.title()}: ${item.cost:.2f}")
    
print("\n⚙️  COMMANDS:")
print("   • 'report' - View machine status")
print("   • 'off' - Shutdown machine")
print("   • 'exit' - Exit the program")

while is_on:
    choice = input("\nWhat would you like? ").lower()
    
    if choice == "off":
        print("🔴 Shutting down the coffee machine...")
        is_on = False
    elif choice == "exit":
        print("👋 Thanks for using the coffee machine! Goodbye!")
        is_on = False
    elif choice == "report":
        print("\n📊 MACHINE REPORT:")
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        
        if drink:
            print(f"\nYou selected: {drink.name.title()} - ${drink.cost:.2f}")
            if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)
                print("\n✅ Enjoy your coffee!")
        else:
            print("❌ Invalid selection. Please choose from the menu.")

print("🔌 Machine powered off.")