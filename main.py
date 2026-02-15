def login():
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    if username != "" and password != "":
        print("Login successful!")
    else:
        print("Invalid username or password. Please try again.")
        login()
    return username

def choose_items():
    print("Select an option:")
    print("1. Burger - $5")
    print("2. Cheesecake - $13.50")
    print("3. Coke - $2.75")
    print("4. Donut - $5")
    print("5. Bacon & Egg Roll - $10.99")
    choices = []
    while True:
        item = input("Enter the number of the item you want to order (or 'done' to finish): ")
        if item.lower() == 'done':
            break
        elif item in ['1', '2', '3', '4', '5']:
            choices.append(item)
        else:
            print("Invalid choice. Please try again.")
    return choices


def calculate_total(choices):
    prices = {
        '1': 5.00,
        '2': 13.50,
        '3': 2.75,
        '4': 5.00,
        '5': 10.99
    }
    total = 0
    for choice in choices:
        total += prices.get(choice, 0)
    return total

def apply_discount(total):
    total *= 0.9
    return total

if __name__ == "__main__":
    name = login()
    choices = choose_items()
    total = calculate_total(choices)
    if total > 10:
        total = apply_discount(total)
    print(f"Hello {name}, you have selected {len(choices)} items. Your total is: ${total:.2f}")
    