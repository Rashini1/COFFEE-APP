# coffee_app.py

def display_menu():
    print("☕ Welcome to Python Coffee Shop! ☕")
    print("Menu:")
    print("1. Espresso - $2.50")
    print("2. Latte - $3.50")
    print("3. Cappuccino - $4.00")
    print("4. Exit")

def get_price(choice):
    prices = {
        1: 2.50,
        2: 3.50,
        3: 4.00
    }
    return prices.get(choice, 0)

def main():
    total = 0
    while True:
        display_menu()
        choice = int(input("Enter your choice (1-4): "))
        
        if choice == 4:
            break
        
        price = get_price(choice)
        if price == 0:
            print("Invalid choice. Try again.")
            continue
        
        size = input("Choose size (S/M/L): ").upper()
        if size == "M":
            price += 0.50
        elif size == "L":
            price += 1.00

        extras = input("Add milk or sugar? (y/n): ").lower()
        if extras == "y":
            price += 0.25
        
        total += price
        print(f"Added to order: ${price:.2f}\n")
    
    print(f"Your total bill: ${total:.2f}")
    print("Thank you for visiting Python Coffee Shop! ☕")

if __name__ == "__main__":
    main()
