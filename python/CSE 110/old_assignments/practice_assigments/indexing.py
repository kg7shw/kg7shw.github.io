shopping_list = []
item = None




print("Please enter the items of the shopping list (type: quit to finish):")

while item != "quit":
    item = input("Item: ")
    if item != "quit":
        shopping_list.append(item)
print()
print("The shopping list is: ")

for item in shopping_list:
    print(item)

print()

print("The shopping list with an index is:")

for i in range(len(shopping_list)):
    item = shopping_list[i]
    print(f"{i}. {item}")

print()

Which item would you like to change? 2
What is the new item?


index = int(input("Which item would you like to change? "))
new_item =

