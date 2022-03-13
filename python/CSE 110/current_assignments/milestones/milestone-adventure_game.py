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
        if choice_one.lower() == 'donuts' or choice_one.lower() == 'd' :
            choice_two = input('You go into the donut shop and you see the have three choices GLAZED, JELLY FILLED, CREME FILLED or do you go get a POPSICLE? ')
        elif choice_one == 'popsicle' or choice_one == 'p':
            choice_two = input('You go to the popsicle cart and you see the have three choices RED, YELLOW, BLUE or do you change your mind and get a DONUT instead? ')
        else:
            print("You weren't hungry after all and you go home.")
            print('The End!')
        
        if choice_two.lower() == 'glazed' or choice_two.lower() == 'g':
            choice_three = input('You ate it but wasnt satified do you CHOOSE ANOTHER or get a POPSICLE?')
        elif choice_two.lower() == 'jelly filled' or choice_two.lower() == 'j':
            choice_three = input('You buy it but it slpis out of your fingers and splas to the floor jelly spewing out you are still hungry do you CHOOSE ANOTHER or get a POPSICLE?')
        elif choice_two.lower() == 'creme filled' or choice_two.lower() == 'c':
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
