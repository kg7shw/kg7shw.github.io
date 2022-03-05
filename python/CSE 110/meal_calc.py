
#import string


number_children = int(input("How many children are there? "))
number_adults = int(input("How many adults are there?  "))
number_drinks = int(input("How many drinks are there? "))
number_seniors = int(input("How many Seniors are there? "))
number_veterans = int(input("How many Veterans are there? "))

price_seniors = float(input("What is the price of a Seniors meal? "))
price_veterans = float(input("What is the price of a Veterans? "))
price_drinks = float(input("What is the price of a drink? "))
price_children = float(input("What is the price of a child's meal? "))
price_adults = float(input("What is the price of a adults's meal? "))

percentage_tip = input("What is the tip percentage? ")
percentage_tip = percentage_tip.split('%')
percentage_tip = float(percentage_tip[0])


#if percentage_tip == string.replace("!","")
# while :
#     print('Inncorrect input. Please input number only example: 0.06')
#     persentage_tip = 0
#     percentage_tip = float(input("What is the tip percentage? "))
#     print(type(percentage_tip))

#percentage_tip = float(percentage_tip)


if percentage_tip > 1:
    percentage_tip /= 100
sales_tax_rate = float(input("What is the sales tax rate? "))
if sales_tax_rate > 1:
    sales_tax_rate /= 100

drinks = price_drinks + number_drinks
child = price_children * number_children
adult = price_adults * number_adults
senior = price_seniors * number_seniors
veteran = price_veterans * number_veterans

subtotal = child + adult + drinks + senior + veteran
tip = subtotal * percentage_tip
sales_tax = sales_tax_rate * subtotal
total = subtotal + sales_tax + tip



print(f"Subtotal: ${subtotal:.2f} ")
print(f"Tip: ${tip:.2f} ")
print(f"Sales Tax: ${sales_tax:.2f}")
print(f"Total: ${total:.2f}")
print()
payment_amount = float(input("What is the payment amount? "))
change = payment_amount - total
print(f"Change: ${change:.2f}")


