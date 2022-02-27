print('Please enter the following information: ')
print()

first_name = input('First name: ')
last_name = input('Last name: ')
email_address = input('Email address: ')
phone_number = input('Phone Number: ')
job_title = input('Job title: ')
id_number = input('ID Number: ')
eye_color = input('Eye color: ')
hair_color = input('Hair color: ')
current_year = input('Current Year: ')
trained = input('Trained: ')

print('The ID Card is: ')
print('----------------------------------------')
print(f'{last_name.upper()}, {first_name.capitalize()}')


print(job_title)
print(f'ID: {id_number} ')
print()

print(email_address.lower())
print(phone_number)
print()
print(f'Hair color: {hair_color.capitalize()}, Eye color: {eye_color.capitalize()}')
print(f'Year: {current_year.capitalize()}, Trained: {trained.capitalize()}')
print('----------------------------------------')
