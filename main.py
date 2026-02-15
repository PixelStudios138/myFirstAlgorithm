def login():
    # Ask for username and password
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    # Check to make sure that there is a username and password entered
    if username != "" and password != "":
        print("Login successful!")
    else:
        print("Invalid username or password. Please try again.")
        login()
    # allow the username to be reused for the receipt
    return username

def choose_items():
    # display the options
    print("Select an option:")
    print("1. Burger - $5")
    print("2. Cheesecake - $13.50")
    print("3. Coke - $2.75")
    print("4. Donut - $5")
    print("5. Bacon & Egg Roll - $10.99")
    choices = []
    choice_list = ['1', '2', '3', '4', '5']
    while True:
        # ask for input
        item = input("Enter the number of the item you want to order (or 'done' to finish): ")
        if item.lower() == 'done':
            break
        elif item in choice_list:
            # add selections to a list
            choices.append(item)
        else:
            # if given an incorrect choice
            print("Invalid choice. Please try again.")
    # allow the choices to be used to calculate the cost
    return choices


def calculate_total(choices):
    # set up the prices for each item
    prices = {
        '1': 5.00,
        '2': 13.50,
        '3': 2.75,
        '4': 5.00,
        '5': 10.99
    }
    # create variable for total cost
    total = 0
    for choice in choices:
        # Checks each choice to see if it is in the prices dictionary, and 
        # returns the corresponding price and adds it to the total.
        # Better than using prices[], as it prevents a KeyError. The 0 is the value
        # that will be returned should it get a value not in the dictionary
        total += prices.get(choice, 0)
    return total

def apply_discount(total):
    # if called, applies a 10% discount to the total
    total *= 0.9
    return total

# only runs if the file is not a module
if __name__ == "__main__":
    # call functions
    name = login()
    choices = choose_items()
    total = calculate_total(choices)
    # checks to see if discount can be applied
    if total > 10:
        total = apply_discount(total)
    # print the receipt. The {total:.2f} returns the total cost, but 
    # rounding it off to 2 decimal places in case a discount is applied and a value 
    # like $30.302 is returned.
    print(f"Hello {name}, you have selected {len(choices)} items. Your total is: ${total:.2f}")
    