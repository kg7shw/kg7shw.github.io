# Sorry, that is a negative number. Please try again.
# Please type a positive number: 12
# The number is: 12

# May I have a piece of candy? yes
# Thank you.
from PIL import Image
print("The library is loaded correctly")
number = int(input('Please type a positive number: '))

while number < 0:
    print('Sorry, that is a negative number. Please try again.')
    number = int(input('Please type a positive number: '))
print(f'The number is: {number}')



candy = input('May I have a piece of candy? ')

while candy.lower != 'yes':
    candy = input('May I have a piece of candy? ')
print('Thank You')