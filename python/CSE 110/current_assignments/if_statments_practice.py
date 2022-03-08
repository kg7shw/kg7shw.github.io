value_1 = int(input('Enter a number '))
value_2 = int(input('Enter a number '))

if value_1 > value_2:
    print("The first number is greater")
else:
    print("The first number is not greater")

if value_1 == value_2:
    print("The numbers are equal")
else:
    print("The numbers are not equal")

users_fav_animal = input('What is your favorite animal: ')
programers_fav_animal = 'Cat'

if users_fav_animal.lower() == programers_fav_animal.lower():
    print("That's my favorite animal too!")
else:
    print("That one is not my favorite.")