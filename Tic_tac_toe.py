import random,os


status=[" "," "," "," "," "," "," "," "," "]

board="""

 1 | 2 | 3         {} | {} | {}
-----------       -----------
 4 | 5 | 6         {} | {} | {}
-----------       -----------
 7 | 8 | 9         {} | {} | {}
"""



def printBoard(board,status):
    board=board.format(*status)
    print(board)



def cls():
    os.system('cls' if os.name == 'nt' else 'clear')



def userChoice():
    global board,status
    while True:
        choice=input("Enter Choice:")
        try:
            choice=int(choice)-1
        except ValueError:
            cls()
            print("Enter Valid Cell")
            printBoard(board,status)
            continue
        else:
            played=validMove(choice)
            if  played == True:
                continue
            if  played == False:
                break
    return choice



def computerChoice():
    while True:
        choice=random.randrange(0,9)
        played=validMove(choice)
        if played == True:
            continue
        else:
            break
    return choice



def validMove(choice):
    global status
    if status[choice] == " ":
        return False
    else:
        cls()
        print("That move was already played.")
        printBoard(board,status)
        return True



def gameOver():
    global board,status
    winning_positions=((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))
    winner=None
    for a,b,c in winning_positions:
        x=status[a]+status[b]+status[c]
        if x=="XXX":
            winner = "Player"
            break
        if x=="OOO":
            winner = "Computer"
            break
    if status.count(" ")==0:
        winner = "Draw"

    if winner==None:
        return False
    elif winner=="Player" or winner=="Computer":
        cls()
        printBoard(board,status)
        print("The {} wins!".format(winner))
        return True
    elif winner=="Draw":
        cls()
        printBoard(board,status)
        print("The Game is a DRAW.")
        return True



while True:
    cls()
    printBoard(board,status)

    user_choice=userChoice()
    status[user_choice]="X"

    game_over=gameOver()
    if game_over==True:
        break

    computer_choice=computerChoice()
    status[computer_choice]="O"

    game_over=gameOver()
    if game_over==True:
        break
