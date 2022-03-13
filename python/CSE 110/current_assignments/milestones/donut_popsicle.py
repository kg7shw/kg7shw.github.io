play_game = input('Do you want to play this adventure game? (YES/NO) ')

def popsicle():
    popsicle_color = input("what color of popciple do you choose RED, YELLOW, BLUE")
    if popsicle_color == "red":
        red()
    elif popsicle_color == "yellow":
        yellow()
    elif popsicle_color == "blue":
        blue()
    else:
        print('incorrect input. Please enter RED, YELLOW, or BLUE ')
        popsicle()

def yellow():
    more = input("you eat a yellow popsicle. Do you want more?")
    if more == 'yes':
        choice()
    else:
        print("thank you for playing!")

def blue():
    more = input("you eat a blue popsicle. Do you want more?")
    if more == 'yes':
        choice()
    else:
        print("thank you for playing!")

def red():
    more = input("you eat a red popsicle. Do you want more?")
    if more == 'yes':
        choice()
    else:
        print("thank you for playing!")

def glazed():
    more = input("you eat a glazed donute. do you want more?")
    if more == 'yes':
        choice()
    else:
        print("thank you for playing!")

def filled():
    more = input("you eat a filled donute. do you want more?")
    if more == 'yes':
        choice()
    else:
        print("thank you for playing!")

def plain():
    more = input("you eat a plain donute. do you want more?")
    if more == 'yes':
        choice()
    else:
        print("thank you for playing!")

def donut():
    donute_choice = input("what kind of donute Glazed, filled, plain:")
    if donute_choice == 'glazed':
        glazed()
    elif donute_choice == 'filled':
        filled()
    else:
        plain()

def choice():
    choice = input("donut or popsicle? ")
    if choice == 'donut':
        donut()
    elif choice == 'popsicle':
        popsicle()

if play_game == 'yes':
    choice()
else: 
    print("Sorry you didn't want to play")