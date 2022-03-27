


shopping_cart = []
total_price = 0


def menu():
    action = 0
    print("Welcome to the Shopping Cart Program!")
    while action != 5:
        #menu
        print()
        print("Please select one of the following:")
        print("1. Add item")
        print("2. View cart")
        print("3. Remove item")
        print("4. Compute total")
        print("5. Quit")
        action = int(input("Please enter an action: "))
        if action == 1:
            add_item()
        elif action == 2:
            view_cart()
        elif action == 3:
            remove_item()
        elif action == 4:
            compute_total()
        elif action == 5:
            print("Thank you. Goodbye.")
        else:
            print("Error unknown action")
    

def add_item():
    product_name = input("What item would you like to add? ")
    product_price = input(f"What is the price of '{product_name}'? ")
    
    product_price = float(product_price)

    product = []
    product.append(product_name)
    product.append(product_price)
    #product = [apple,1.35]
    #cart = [(apple,1.35),...]
    shopping_cart.append(product)
    print(f"'{product_name}' has been added to the cart.")


# Please enter an action: 1
# What item would you like to add? Milk
# What is the price of 'Milk'? 3.49
# 'Milk' has been added to the cart.

def view_cart():
    print("The contents of the shopping cart are:")
    number = 0
    for product in shopping_cart:
        number +=1
        print(f"{number}. {product[0]} - ${product[1]:.2f}")
        #print(len(shopping_cart),".", product[0], "- $",product[1])

def remove_item():
    product_to_remove = input("which item would you like to remove? ")
    for product in shopping_cart:
        if product[0] == product_to_remove:
            shopping_cart.remove(product)
    print("Item removed.")


def compute_total():
    total_price = 0
    for product in shopping_cart:
        total_price += product[1]
    print(f"The total price of the items in the shopping cart is: ${total_price:.2f}")
    total_price = 0



menu()






























# product_list = []
# shopping_cart = []

# item = ""
# item_is_product = False
# total_price = 0


# #menu
# print("Welcome to the Shopping Cart Program!")
# print()
# print("Please select one of the following:")
# print("1. Add item")
# print("2. View cart")
# print("3. Remove item")
# print("4. Compute total")
# print("5. Quit")

# action = int(input("Please enter an action: "))

# # 1. Add item
# if action == 1:
    
#     while item != "quit":
#         item = input("Add item to shopping cart: ")
#         for product in product_list:
#             if product[0] == item:
#                 shopping_cart.append(product)
#                 total_price += product[1]
#             else:
#                 print("Error! Item is not found in our product list.")

# #2.
# elif action == 2:
#     # for thing in shopping_cart:
#     pass
# #3.
# elif action == 3:
#     pass
# #4.
# elif action == 4:
#     pass
# #5. Quit
# else:
#     print("Thank you. Goodbye.")











#     # for product in product_list:
#     #     if product == 0:
#     #         item_is_product = True
#     #     else:
#     #         item_is_product = False
#     # if item_is_product == True:
#     #     if item == "apple":
#     #         item_price = 2
#     #     elif item ==

