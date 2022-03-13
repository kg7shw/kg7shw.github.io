play_game = input('Do you want to play this adventure game? (YES/NO) ')

def popsicle():
    popsicle_color = input("What color of popsicle do you choose RED, YELLOW, BLUE ")
    if popsicle_color.lower() == "red" or popsicle_color.lower() == "r" :
        red()
    elif popsicle_color.lower() == "yellow" or popsicle_color.lower() == "y":
        yellow()
    elif popsicle_color.lower() == "blue" or popsicle_color.lower() == "b":
        blue()
    else:
        print('Incorrect input. Please enter RED, YELLOW, or BLUE ')
        popsicle()

def yellow():
    more = input("You eat a yellow popsicle it happens to be bananna flavored. It  is so nasty you throw it away. Do you want something else? (YES/NO) ")
    if more.lower() == 'yes' or more.lower() == 'y':
        choice()
    else:
        print("Thank you for playing!")

def blue():
    more = input("You eat a blue popsicle. it is super delicious. Do you want more?(YES/NO) ")
    if more.lower() == 'yes' or more.lower() == 'y':
        choice()
    else:
        print("Thank you for playing!")

def red():
    more = input("You eat a red popsicle. You are satisfied. Do you want more?(YES/NO) ")
    if more.lower() == 'yes' or more.lower() == 'y':
        choice()
    else:
        print("Thank you for playing!")

def glazed():
    more = input("You eat a glazed donut and love every bite. Do you want more?(YES/NO) ")
    if more.lower() == 'yes' or more.lower() == 'y':
        choice()
    else:
        print("Thank you for playing!")

def jelly():
    more = input("you eat a jelly donut and you are very satisfied. Do you want more?(YES/NO) ")
    if more.lower() == 'yes' or more.lower() == 'y':
        choice()
    else:
        print("thank you for playing!")

def creme():
    more = input("you eat a creme donut. It tastes like heaven. Do you want more?(YES/NO) ")
    if more.lower() == 'yes' or more.lower() == 'y':
        choice()
    else:
        print("thank you for playing!")

def donut():
    donut_choice = input("what kind of donut would you like to eat GLAZED, JELLY, CREME? ")
    if donut_choice.lower() == 'glazed' or donut_choice.lower() == 'g':
        glazed()
    elif donut_choice.lower() == 'jelly' or donut_choice.lower() == 'j':
        jelly()
    elif donut_choice.lower() == 'creme' or donut_choice.lower() == 'c':
        creme()
    else:
        print('incorrect input. Please enter GLAZED, JELLY, or CREME ')
        donut()

def choice():
    choice_level = input("You are hungry and you see two places that intrest you a donut shop or a popcsicle cart which do you choose? DONUT 🍩 or POPSICLE 🍭? ")
    if choice_level.lower() == 'donut' or choice_level.lower() == 'd':
        donut()
    elif choice_level.lower() == 'popsicle' or choice_level.lower() == 'p':
        popsicle()
    else:
        print('incorrect input. Please enter DONUT or POPSICLE ')
        choice() 

if play_game == 'yes' or play_game == 'y':
    print('Awesome! lets get started.')
    print('Here are the rules of the game. You will be given Choices in this game.')
    print('The choices are displyed in all CAPS. You will choose one of the choices by typing in the word or the first letter of the word. Example: PEACH or ORANGE? (Answer: peach or p)')
    print('The game will then play you the story or senario assiciated with the choice. Play along and have fun!')
    print()
    choice()
else: 
    print("Sorry you didn't want to play")