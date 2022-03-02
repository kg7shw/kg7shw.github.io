
number_children = int(input("How many children are there? "))
number_adults = int(input("How many adults are there?  "))
drinks_number = int(input("How many drinks are there? "))
price_children = float(input("What is the price of a child's meal? "))
price_adults = float(input("What is the price of a adults's meal? "))
drinks_price = float(input("What is the price of a drink? "))
sales_tax_rate = float(input("What is the sales tax rate? "))
if sales_tax_rate > 1:
    sales_tax_rate /= 100

drinks = drinks_price + drinks_number
child = price_children * number_children
adult = price_adults * number_adults
subtotal = child + adult + drinks
sales_tax = sales_tax_rate * subtotal
total = subtotal + sales_tax


print(f"Subtotal: ${subtotal:.2f} ")
print(f"Sales Tax: ${sales_tax:.2f}")
print(f"Total: ${total:.2f}")
print()
payment_amount = float(input("What is the payment amount? "))
change = payment_amount - total
print(f"Change: ${change:.2f}")


