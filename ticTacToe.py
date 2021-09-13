#Program simulating Tic Tac Toe

import sys

#Keep track of which players turn it is
turnCounter = 1

#Representation of the initial game board prior to game start
theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
            'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
            'bot-L': ' ', 'bot-M': ' ', 'bot-R': ' '
            }

#Prints the playing board
def printBoard():
    print('   A  ' + ' B  ' + ' C  ')
    print()
    print('     |   |    ')
    print('1  ' + theBoard['top-L'] + ' | ' + theBoard['top-M'] + ' | ' + theBoard['top-R'] + ' ')
    print('  ___|___|___ ')
    print('     |   |    ')
    print('2  ' + theBoard['mid-L'] + ' | ' + theBoard['mid-M'] + ' | ' + theBoard['mid-R'] + ' ')
    print('  ___|___|___ ')
    print('     |   |    ')
    print('3  ' + theBoard['bot-L'] + ' | ' + theBoard['bot-M'] + ' | ' + theBoard['bot-R'] + ' ')
    print('     |   |  ')
    print()

#Empty the board before beginning each game
def resetBoard():
    for k in theBoard.keys():
        theBoard[k] = ' '

#Check for a tie
def checkForTie():
    slotsOccupied = 0
    for i in theBoard.values():
        if i != ' ':
            slotsOccupied += 1
    if slotsOccupied == 9:
        return True
    else:
        return False

#Prompt to play again
def playAgain():
    print('Answer: ', end='')
    playAgain = input()
    while playAgain != 'Y' and playAgain != 'N':
        print('Invalid choice. Enter Y for Yes or N for No.')
        print('Answer: ', end='')
        playAgain = input()
    if playAgain == 'N':
        sys.exit()
    else:
        return True

#Check for a win
#Return 1 if player 1 wins and 2 if player 2 wins
def checkForWin():
    #Check player 1
    if theBoard['top-L'] == 'X':
        if theBoard['mid-L'] == 'X':
            if theBoard['bot-L'] == 'X':
                return 1
        if theBoard['mid-M'] == 'X':
            if theBoard['bot-R'] == 'X':
                return 1
        if theBoard['top-M'] == 'X':
            if theBoard['top-R'] == 'X':
                return 1
    if theBoard['top-M'] == 'X':
        if theBoard['mid-M'] == 'X':
            if theBoard['bot-M'] == 'X':
                return 1
    if theBoard['top-R'] == 'X':
        if theBoard['mid-M'] == 'X':
            if theBoard['bot-L'] == 'X':
                return 1
        if theBoard['mid-R'] == 'X':
            if theBoard['bot-R'] == 'X':
                return 1
    if theBoard['bot-L'] == 'X':
        if theBoard['bot-M'] == 'X':
            if theBoard['bot-R'] == 'X':
                return 1

    #Check player 2
    if theBoard['top-L'] == 'O':
        if theBoard['mid-L'] == 'O':
            if theBoard['bot-L'] == 'O':
                return 2
        if theBoard['mid-M'] == 'O':
            if theBoard['bot-R'] == 'O':
                return 2
        if theBoard['top-M'] == 'O':
            if theBoard['top-R'] == 'O':
                return 2
    if theBoard['top-M'] == 'O':
        if theBoard['mid-M'] == 'O':
            if theBoard['bot-M'] == 'O':
                return 2
    if theBoard['top-R'] == 'O':
        if theBoard['mid-M'] == 'O':
            if theBoard['bot-L'] == 'O':
                return 2
        if theBoard['mid-R'] == 'O':
            if theBoard['bot-R'] == 'O':
                return 2
    if theBoard['bot-L'] == 'O':
        if theBoard['bot-M'] == 'O':
            if theBoard['bot-R'] == 'O':
                return 2

#Game's main loop. Alternate between players letting each player provide a set of coordinates specifying where they want to place their marker
while True:
    token = 'X'
    print('-----------------------------------------------------------------------------------------------------')
    print('Enter the coordinate where you want to make your move (e.g. A1, C3, etc.)')
    print()
    printBoard()
    print()
    if turnCounter % 2 == 1:
        print("Player 1's turn. Token is X.")
        token = 'X'
    else:
        print("Player 2's turn. Token is O.")
        token = 'O'
    print('Your move: ', end='')
    move = input()

    #Error handling for the user input formatting
    while move != 'A1' and move != 'A2' and move != 'A3' and move != 'B1' and move != 'B2' and move != 'B3' and move != 'C1' and move != 'C2' and move != 'C3':
        print('Must enter a valid coordinate in the form A1, B2, C3, etc.')
        print('Your move: ', end='')
        move = input()

    #Put the tokens onto the board
    if  move == 'A1' and theBoard['top-L'] == ' ':
        theBoard['top-L'] = token
    elif move == 'B1' and theBoard['top-M'] == ' ':
        theBoard['top-M'] = token
    elif move == 'C1' and theBoard['top-R'] == ' ':
        theBoard['top-R'] = token
    elif move == 'A2' and theBoard['mid-L'] == ' ':
        theBoard['mid-L'] = token
    elif move == 'B2' and theBoard['mid-M'] == ' ':
        theBoard['mid-M'] = token
    elif move == 'C2' and theBoard['mid-R'] == ' ':
        theBoard['mid-R'] = token
    elif move == 'A3' and theBoard['bot-L'] == ' ':
        theBoard['bot-L'] = token
    elif move == 'B3' and theBoard['bot-M'] == ' ':
        theBoard['bot-M'] = token
    elif move == 'C3' and theBoard['bot-R'] == ' ':
        theBoard['bot-R'] = token
    else:
        print('Space is already occupied. Enter a different move.')
        continue

    #Alternate whose turn it is
    turnCounter += 1

    #check for a win
    if checkForWin() == 1:
        print('-----------------------------------------------------------------------------------------------------')
        printBoard()
        print('Player 1 wins! Play again? Enter Y for Yes and N for No.')
        if playAgain() == True:
            resetBoard()
    elif checkForWin() == 2:
        print('-----------------------------------------------------------------------------------------------------')
        printBoard()
        print('Player 2 wins! Play again? Enter Y for Yes and N for No.')
        if playAgain() == True:
            resetBoard()

    #check for a tie
    if checkForTie() == True:
        print("It's a tie! Play again? Enter Y for Yes and N for No.")
        if playAgain() == True:
            resetBoard()
