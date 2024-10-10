# products 字典（示例数据）
products = {
    "IT products": [("Laptop", 1000), ("USB Drive", 15)],
    "Electronics": [("Smartphone", 600), ("Headphones", 150)]
}

def validate_name(name):
    parts = name.split()
    return len(parts) == 2 and all(part.isalpha() for part in parts)

def validate_email(email):
    return "@" in email and email.strip() != ""

def display_categories():
    print("Available Categories:")
    for index, category in enumerate(products.keys(), start=1):
        print(f"{index}. {category}")
    
    while True:
        try:
            category_index = int(input("Select a category by number: ")) - 1
            if 0 <= category_index < len(products):
                return category_index
            else:
                print("Invalid selection. Please try again.")
        except ValueError:
            print("Please enter a valid number.")
        except StopIteration:
            return None  # 处理输入结束的情况

def display_products(products_list):
    for index, (product, price) in enumerate(products_list, start=1):
        print(f"{index}. {product} - ${price}")

def display_sorted_products(products_list, sort_order):
    if sort_order == "asc":
        return sorted(products_list, key=lambda x: x[1])
    else:
        return sorted(products_list, key=lambda x: x[1], reverse=True)

def add_to_cart(cart, product, quantity):
    cart.append((*product, quantity))

def display_cart(cart):
    total_cost = 0
    print("Items in your cart:")
    for product, price, quantity in cart:
        cost = price * quantity
        total_cost += cost
        print(f"{product} - ${price} x {quantity} = ${cost}")
    print(f"Total cost: ${total_cost}")

def generate_receipt(name, email, cart, total_cost, address):
    print(f"Customer: {name}\nEmail: {email}\nItems Purchased:")
    for product, price, quantity in cart:
        cost = price * quantity
        print(f"{quantity} x {product} - ${price} = ${cost}")
    print(f"Total: ${total_cost}\nDelivery Address: {address}")
    print("Your items will be delivered in 3 days.\nPayment will be accepted upon delivery.")

def main():
    name = input("Enter your name (First Last): ")
    while not validate_name(name):
        print("Invalid name. Please enter your first and last name (only alphabets).")
        name = input("Enter your name (First Last): ")

    email = input("Enter your email address: ")
    while not validate_email(email):
        print("Invalid email. Please include an '@' in your email address.")
        email = input("Enter your email address: ")

    cart = []
    while True:
        category_index = display_categories()
        if category_index is None:
            print("Category selection ended. Exiting...")
            return
        
        selected_category = list(products.keys())[category_index]
        print(f"You selected category: {selected_category}")
        display_products(products[selected_category])

        while True:
            action = input("Choose an option:\n1. Select a product to buy\n2. Sort products\n3. Go back to categories\n4. Finish shopping\n")
            if action == '1':
                product_choice = input("Select product by number: ")
                try:
                    product_index = int(product_choice) - 1
                    selected_product = products[selected_category][product_index]
                    quantity = input("Enter quantity: ")
                    if quantity.isdigit() and int(quantity) > 0:
                        add_to_cart(cart, selected_product, int(quantity))
                        print(f"Added {quantity} x {selected_product[0]} to cart.")
                    else:
                        print("Invalid quantity. Please enter a positive number.")
                except (ValueError, IndexError):
                    print("Invalid product selection. Please try again.")

            elif action == '2':
                sort_order = input("Sort by price:\n1. Ascending\n2. Descending\n")
                if sort_order in ['1', '2']:
                    order = "asc" if sort_order == '1' else "desc"
                    sorted_products = display_sorted_products(products[selected_category], order)
                    display_products(sorted_products)
                else:
                    print("Invalid selection. Please try again.")

            elif action == '3':
                break

            elif action == '4':
                if cart:
                    total_cost = sum(price * quantity for _, price, quantity in cart)
                    address = input("Enter delivery address: ")
                    display_cart(cart)
                    generate_receipt(name, email, cart, total_cost, address)
                else:
                    print("Thank you for using our portal. Hope you buy something from us next time. Have a nice day.")
                return

            else:
                print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
