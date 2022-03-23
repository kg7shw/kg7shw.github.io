import math
import statistics



numbers = []
print("Enter a list of numbers, type 0 when finished.")

sum = 0
number = -1

while number != 0:
    number = int(input("Enter number: "))
    if number != 0:
        numbers.append(number)


# for number in numbers:
#     sum += number

sum_total = sum(numbers)

print(f"Your sum total is: {sum:.2f}")


# amount = len(numbers)

# average = sum / amount

print(f"The average is: {average:.2f}")



largest_number = -1

for number in numbers:
    if number > largest_number:
        largest_number = number

print(f"The largest number is: {largest_number}")

# Compute the sum, or total, of the numbers in the list. Check

# Compute the average of the numbers in the list.

# Find the maximum, or largest, number in the list.