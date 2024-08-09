import random
l = ["rock", "paper", "scissor"]
ucount = 0
ccount = 0
while True:
    user_input = int(input('''
    Game Start...
    1.Yes
    2.No|Exit
    
    '''))
    if user_input == 1:
        for a in range(1,6):
            userInput = int(input('''
            1.Rock
            2.Paper
            3.Scissor
                       
            '''))
            if userInput == 1:
                uchoice = "rock"

            elif userInput == 2:
                uchoice = "paper"
            elif userInput == 3:
                uchoice = "scissor"
            Cchoice = random.choice(l)

            if Cchoice == uchoice:
                print("Computer Choice:",Cchoice)
                print("Your Choice:",uchoice)
                print("Draw Game")
                ucount = ucount + 1
                ccount = ccount + 1

            elif (uchoice == 'rock' and Cchoice == 'scissor') or (uchoice == 'paper' and Cchoice == 'rock') or (uchoice == 'scissor' and Cchoice == 'paper'):
                print("Computer Choice:", Cchoice)
                print("Your Choice:", uchoice)
                print("You Win")
                ucount = ucount + 1
            else:
                print("Computer Choice:", Cchoice)
                print("Your Choice:", uchoice)
                print("Computer Win")
                ccount = ccount + 1
        print("")
        if ccount == ucount:
            print("Final Game is dra")
            print("Computer score is: ", ccount)
            print("Your score is: ", ucount)
        elif ccount > ucount:
            print("Cmputer Win the Game")
            print("Computer score is: ", ccount)
            print("Your score is: ", ucount)
        elif ucount > ccount:
            print("You win the game")
            print("Computer score is: ", ccount)
            print("Your score is: ", ucount)


    else:
        break