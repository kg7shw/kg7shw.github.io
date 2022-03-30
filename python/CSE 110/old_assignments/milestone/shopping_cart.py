items = []


item = ""

while item != "quit":
    item = input("Add an item to your cart: ")

    
    if item != "quit":
        items.append(item)

print()
print("The items in your cart are: ")

for item in items:
    print(item)