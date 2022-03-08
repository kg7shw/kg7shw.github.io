grade_percentage = int(input('What is you grade percentage? '))

if grade_percentage >= 90:
    letter = 'A'
elif grade_percentage >= 80:
    letter = 'B'

elif grade_percentage >= 70:
    letter = 'C'

elif grade_percentage >= 60:
    letter = 'D'

else: letter = 'F'

plus_minus = grade_percentage % 10

if plus_minus >= 7:
    character = '+'

elif plus_minus <= 3:
    character = '-'

else:
    character = ''

if grade_percentage >= 93:
    character = ''

if letter == 'F':
    character = ''

print(f'Your grade letter is: {letter}{character}')

if grade_percentage >= 70:
    print('Congratulations on passing!🥳')
else: 
    print("You'll do better next time")
