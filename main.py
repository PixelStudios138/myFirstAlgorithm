def login():
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    if username and password:
        print("Login successful!")
    return username

def choose_items():
    print("Select an option:")
    print("1. Burger - $5")
    print("2. Barry - $13.50")
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