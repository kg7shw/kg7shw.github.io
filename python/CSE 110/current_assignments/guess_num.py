# import random

# number = random.randint(1, 10)
# print(number)

# candy = ""

# while candy != "yes":
#     candy = input("May I have a piece of candy? ")
# print("Thank you")


import random

magic_num = random.randint(1, 10)

guess_num = 0

while guess_num != magic_num:
    guess_num = int(input("What is your guess? "))

    if guess_num < magic_num:
        print("Guess higher")
    elif guess_num > magic_num:
        print("Guess lower")
    else:
        print("Correct! You guessed it!")
    