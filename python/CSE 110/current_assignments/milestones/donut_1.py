from secrets import choice


play_game = input('Do you want to play this adventure game? (YES/NO) ')

if play_game.lower() == 'yes' or play_game.lower() == 'y':
    print('Awesome! lets get started.')
    print('Here are the rules of the game. You will be given Choices in this game.')
    print('The choices are displyed in all CAPS. You will choose one of the choices by typing in the word or the first letter of the word.')
    print('The game will then play you the story or senario assiciated with the choice. Play along and have fun!')
    print()
    print('You are walking down the street and you are feeling snackish you see a donunt shop and a popcicle cart and you decide to choose one.')
    choice_one = input('Do you go get DONUTS or POPSICLE? ')
    customer_choice = 'yes'
    while customer_choice.lower() == 'yes' or customer_choice.lower() == 'y':
        if choice_one.lower() == 'donuts' or choice_one.lower() == 'd':
            choice_two = input('You go into the donut shop and you see the have three choices GLAZED, JELLY FILLED, CREME FILLED ')
        elif choice_one == 'popsicle' or choice_one == 'p':
            choice_two = input('You go to the popsicle cart and you see the have three choices RED, YELLOW, or BLUE? ')
        else:
            print("You weren't hungry after all and you go home.")
            print('The End!')
        
        
            print('You eat it and love every bite. You are satified and diecide to go home.')
            print('The End!')
    
        if choice_two.lower() == 'glazed' or choice_two.lower() ==  'g':
            choice_three = input('You ate it but wasnt satified do you CHOOSE ANOTHER or get a POPSICLE? ')
            if choice_three.lower() == 'choose another' or choice_three.lower() ==  'c':
                customer_choice = input('Do you want to choose andother donut?(YES/NO) ')
            else: choice_two = input('You go to the popsicle cart and you see the have three choices RED, YELLOW, BLUE or do you change your mind and get a DONUT instead? ')


        # elif choice_two.lower() == 'jelly filled' or choice_two.lower() == 'j':
        #     choice_three = input('You buy it but it slips out of your fingers and splas to the floor jelly spewing out you are still hungry do you CHOOSE ANOTHER or get a POPSICLE?')
        #     if choice_three.lower() == 'choose another' or choice_three.lower() ==  'c':
        #         customer_choice = input('Do you want to choose andother donut?(YES/NO) ')
        # elif choice_two.lower() == 'creme filled' or choice_two.lower() ==  'c':
        #     print('You eat it and love every bite. You are satified and diecide to go home.')
        #     print('The End!')
        # else:
        #     customer_choice = input('Do you want to choose andother donut?(YES/NO) ')
            
        customer_choice = input('Do you want to choose andother donut?(YES/NO) ')
    print('Thank you for playing')
    print('The End')
else:
    print("Sorry you didn't want to play please come back soon and play")

    #if choice_three.lower() == 'choose another':
     #   choice_two = input('You go into the donut shop and you see the have three choices GLAZED, JELLY FILLED, CREME FILLED or do you go get a POPSICLE? ')









play_game = input('Do you want to play this adventure game? (YES/NO) ')

def popsicle():
    popsicle_color = input("What color of popsicle do you choose RED, YELLOW, BLUE")
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
    more = input("You eat a yellow popsicle. Do you want more? (YES/NO) ")
    if more.lower() == 'yes' or more.lower() == 'y':
        choice()
    else:
        print("Thank you for playing!")

def blue():
    more = input("You eat a blue popsicle. Do you want more?(YES/NO) ")
    if more.lower() == 'yes' or more.lower() == 'y':
        choice()
    else:
        print("Thank you for playing!")

def red():
    more = input("You eat a red popsicle. Do you want more?(YES/NO) ")
    if more.lower() == 'yes' or more.lower() == 'y':
        choice()
    else:
        print("Thank you for playing!")

def glazed():
    more = input("You eat a glazed donut. do you want more?(YES/NO) ")
    if more.lower() == 'yes' or more.lower() == 'y':
        choice()
    else:
        print("Thank you for playing!")

def jelly():
    more = input("you eat a jelly donut. Do you want more?(YES/NO) ")
    if more.lower() == 'yes' or more.lower() == 'y':
        choice()
    else:
        print("thank you for playing!")

def creme():
    more = input("you eat a creme donut. do you want more?(YES/NO) ")
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
        jelly()
    else:
        print('incorrect input. Please enter GLAZED, JELLY, or CREME ')

def choice():
    choice = input("You are hungry and you see two places that intrest you a donut shop or a popcsicle cart which do you choose? A DONUT 🍩 or A POPSICLE 🍭? ")
    if choice.lower() == 'donut' or choice.lower() == 'd':
        donut()
    elif choice.lower() == 'popsicle' or choice.lower() == 'p':
        popsicle()

if play_game == 'yes' or play_game == 'y':
    choice()
else: 
    print("Sorry you didn't want to play")




















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