
shopping_cart = []
action = 0


def menu():
    #menu
    print("Welcome to the Shopping Cart Program!")
    print()
    print("Please select one of the following:")
    print("1. Add item")
    print("2. View cart")
    print("3. Remove item")
    print("4. Compute total")
    print("5. Quit")
    action = int(input("Please enter an action: "))

def add_item():
    # 1. Add item
    if action == 1:
        product_name = input("What item would you like to add? ")
        product_price = input(f"What is the price of '{product_name}'? ")
        
        product = []
        product.append(product_name)
        product.append(product_price)
        cart = []
        cart.append()


# Please enter an action: 1
# What item would you like to add? Milk
# What is the price of 'Milk'? 3.49
# 'Milk' has been added to the cart.

def view_cart():
    #2. View cart
    elif action == 2:
        # for thing in shopping_cart:
        pass

def remove_item():
    #3. Remove item
    elif action == 3:
        pass

def compute_total():
    #4. Compute total
    elif action == 4:
        pass

def quit():
    #5. Quit
    else:
        print("Thank you. Goodbye.")


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











