# product_list = ["apple", "orange", "banana", "peach"]

# prices = []


# items = []


# item = ""

# while item != "quit":
#     item = input("Add an item to your cart: ")

    
#     if item != "quit":
#         items.append(item)
# print()
# print("The items in your cart are: ")

# for item in items:
#     print(item)











# Welcome to the Shopping Cart Program!

# Please select one of the following: 
# 1. Add item
# 2. View cart
# 3. Remove item
# 4. Compute total
# 5. Quit
# Please enter an action:





product_list = [("apple", 1.5), ("orange", 2.5), ("banana", .25), ("peach", 2.50)]
shopping_cart = []

item = ""
item_is_product = False
total_price = 0



print("Welcome to the Shopping Cart Program!")
print()
print("Please select one of the following:")
print("1. Add item")
print("2. View cart")
print("3. Remove item")
print("4. Compute total")
print("5. Quit")

action = int(input("Please enter an action: "))

if action == 1:
    
    while item != "quit":
        item = input("Add item to shopping cart: ")
        for product in product_list:
            if product[0] == item:
                shopping_cart.append(product)
                total_price += product[1]
            else:
                print("Error! Item is not found in our product list.")


elif action == 2:
    # for thing in shopping_cart:
    pass

elif action == 3:
    pass

elif action == 4:
    pass

else:
    print("Thank you. Goodbye.")











    # for product in product_list:
    #     if product == 0:
    #         item_is_product = True
    #     else:
    #         item_is_product = False
    # if item_is_product == True:
    #     if item == "apple":
    #         item_price = 2
    #     elif item == 











