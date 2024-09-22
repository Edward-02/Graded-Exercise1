products = {
    "IT Products": [
        ("Laptop", 1000),
        ("Smartphone", 600),
        ("Headphones", 150),
        ("Keyboard", 50),
        ("Monitor", 300),
        ("Mouse", 25),
        ("Printer", 120),
        ("USB Drive", 15)
    ],
    "Electronics": [
        ("Smart TV", 800),
        ("Bluetooth Speaker", 120),
        ("Camera", 500),
        ("Smartwatch", 200),
        ("Home Theater", 700),
        ("Gaming Console", 450)
    ],
    "Groceries": [
        ("Milk", 2),
        ("Bread", 1.5),
        ("Eggs", 3),
        ("Rice", 10),
        ("Chicken", 12),
        ("Fruits", 6),
        ("Vegetables", 5),
        ("Snacks", 8)
    ]
}

def display_sorted_products(products_list, sort_order):
    reverse = sort_order == "desc"
    return sorted(products_list, key=lambda x: x[1], reverse=reverse)

def display_products(products_list):
    output = []
    for index, (name, price) in enumerate(products_list, start=1):
        output.append(f"{index}. {name} - ${price:.2f}")
    return "\n".join(output)

def display_categories():
    output = []
    for index, category in enumerate(products.keys(), start=1):
        output.append(f"{index}. {category}")
    if output:
        print("\n".join(output))  # Print categories
        return len(products)  # Return count of categories for testing
    return 0  # Return 0 if there are no categories

def add_to_cart(cart, product, quantity):
    cart.append((product[0], product[1], quantity))

def display_cart(cart):
    if not cart:
        return "Your cart is empty."
    
    output = []
    total_cost = 0
    for item in cart:
        item_total = item[1] * item[2]
        total_cost += item_total
        output.append(f"{item[0]} - ${item[1]} x {item[2]} = ${item_total:.2f}")
    
    output.append(f"Total cost: ${total_cost:.2f}")
    return "\n".join(output)

def generate_receipt(name, email, cart, total_cost, address):
    output = []
    output.append(f"Customer: {name}")
    output.append(f"Email: {email}")
    output.append("Items Purchased:")
    for item in cart:
        item_total = item[1] * item[2]
        output.append(f"{item[2]} x {item[0]} - ${item[1]} = ${item_total:.2f}")
    output.append(f"Total: ${total_cost:.2f}")
    output.append(f"Delivery Address: {address}")
    output.append("Your items will be delivered in 3 days.")
    output.append("Payment will be accepted upon delivery.")
    return "\n".join(output)

def validate_name(name):
    parts = name.split()
    return len(parts) == 2 and all(part.isalpha() for part in parts)

def validate_email(email):
    return '@' in email

def main():
    cart = []
    
    while True:
        name = input("Enter your name (First Last): ")
        if validate_name(name):
            break
        print("Invalid name. Please enter a valid name with first and last names.")

    while True:
        email = input("Enter your email address: ")
        if validate_email(email):
            break
        print("Invalid email. Please enter a valid email address with '@'.")

    while True:
        category_count = display_categories()
        category_choice = input("Select a category number: ")
        
        if category_choice.isdigit():
            category_choice = int(category_choice)
            categories = list(products.keys())
            if 1 <= category_choice <= category_count:
                selected_category = categories[category_choice - 1]
                product_list = products[selected_category]
                sorted_product_list = product_list.copy()
                
                while True:
                    print(display_products(sorted_product_list))
                    action = input("Choose an action: \n1. Select a product to buy\n2. Sort products by price\n3. Go back to categories\n4. Finish shopping\n")
                    
                    if action.isdigit():
                        action = int(action)
                        
                        if action == 1:
                            product_choice = input("Enter the number of the product you want to buy: ")
                            if product_choice.isdigit():
                                product_choice = int(product_choice)
                                if 1 <= product_choice <= len(sorted_product_list):
                                    quantity = int(input("Enter the quantity: "))
                                    add_to_cart(cart, sorted_product_list[product_choice - 1], quantity)
                                else:
                                    print("Invalid product number.")
                        
                        elif action == 2:
                            sort_order = input("Sort by price: \n1. Ascending\n2. Descending\n")
                            if sort_order in ['1', '2']:
                                order = "asc" if sort_order == '1' else "desc"
                                sorted_product_list = display_sorted_products(product_list, order)
                                print(display_products(sorted_product_list))
                            else:
                                print("Invalid sort order.")
                        
                        elif action == 3:
                            break
                        
                        elif action == 4:
                            if cart:
                                print("Here is your cart:")
                                cart_output = display_cart(cart)
                                print(cart_output)
                                total_cost = sum(item[1] * item[2] for item in cart)
                                address = input("Enter your delivery address: ")
                                receipt_output = generate_receipt(name, email, cart, total_cost, address)
                                print(receipt_output)
                            else:
                                print("Thank you for using our portal. Hope you buy something from us next time. Have a nice day.")
                            return
                        
                        else:
                            print("Invalid option. Please try again.")
            else:
                print("Invalid category number. Please try again.")
        else:
            print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    main()
