# This program allows you to play battleship
import random
import time


# import pygame
# from pygame import *

# mixer.init()
# mixer.music.load('CoolSchool.ogg')
# mixer.music.play(-1,0.0)
# hitSound = pygame.mixer.Sound('Explosion+2.ogg')
# missedSound = pygame.mixer.Sound('Sad_Trombone.ogg')


##########
def cls():
    for i in range(0, 50):
        print('')


###################
def displayIntro():
    print('Welcome to Battleship')
    time.sleep(1)
    print('Battleship is a game where you are trying to sink all of your opponents resources.')
    time.sleep(1)
    print('You will get to choose where you place your ships and your opponent will also')
    time.sleep(1)
    print("Your goal is to guess where your opponent's ships are and be the first to get rid of them")
    time.sleep(1)
    print('Lets Go!')


################
def wantIntro():
    print('What is your name captain =>')

    myName = input()

    print('Hello Captain', myName, 'I hope you are ready to sink some enemy ships')
    print('but first would you like to read the intro?')
    cIntro = input()
    cIntro = cIntro.lower()

    if cIntro == 'y' or cIntro == 'yes':
        displayIntro()
        return myName
    else:
        return myName


################
def firstTurn():
    if random.randint(0, 1) == 0:
        return 'computer'
    else:
        return 'user'


##################
def getNewBoard():
    board = []
    for x in range(10):
        col = []
        for y in range(10):
            col.append(' e0 ')
        # end for y
        board.append(col)
    # end for x

    return board


###############################
def displayBoard(board, player):
    print("               ** " + player + "'s Board **")
    print('      A    B    C    D    E    F    G    H    I    J')
    rowBorder = '    +----+----+----+----+----+----+----+----+----+----+ '
    for row in range(10):
        print(rowBorder)
        print('{:>2}'.format(row + 1), end='  ')
        for col in range(10):
            print('|', end='')
            if player == 'computer':
                if '0' in board[row][col]:
                    print('    ', end='')
                    # print(board[row][col], end='')
                elif board[row][col] == ' e1 ':  # miss
                    print('Miss', end='')
                elif '1' in board[row][col]:
                    print('Boom', end='')  # hit
            else:  # user
                if board[row][col] == ' e0 ':
                    print('    ', end='')
                else:
                    print(board[row][col], end='')
        print('|')
    print(rowBorder)
    return


################
def playAgain():
    again = input('Do you want to play again').lower()
    if 'y' in again:
        main()
    else:
        input('Press <Enter> to exit.')
        exit()


######################################
def displayResult(cPts, uPts):
    if uPts == 0:

        print('The computer wins')
        print('The computer won with', cPts, ' Points')
        # playAgain()

    elif cPts == 0:

        print('You win, Congrats!!')
        print('You still have', uPts, ' Points')
        # playAgain()


#####################################
def setUpComputerBoard(cBoard, cPts):
    ## Aircraft Carrier ##
    cBoard = computerPlotShip(cBoard, 5, '-a0-')
    cPts = cPts + 5
    ## Destroyer ##
    cBoard = computerPlotShip(cBoard, 4, '-d0-')
    cPts = cPts + 4
    ## Battleship ##
    cBoard = computerPlotShip(cBoard, 3, '-b0-')
    cPts = cPts + 3
    ## Submarine ##
    cBoard = computerPlotShip(cBoard, 3, '-s0-')
    cPts = cPts + 3
    ## Cruiser ##
    cBoard = computerPlotShip(cBoard, 2, '-c0-')
    cPts = cPts + 2

    return cBoard, cPts


##############
def isHoriz():
    pick = random.randint(0, 100)
    if pick <= 50:
        return True
    else:
        return False


##############################################
def computerPlotShip(cBoard, sValue, sMarker):
    if isHoriz():
        overlap = True
        while overlap:
            overlap = False

            row = random.randint(0, 9)
            col = random.randint(0, 9 - sValue)
            for i in range(col, col + sValue):
                if cBoard[row][i] != ' e0 ':
                    overlap = True
        for i in range(col, col + sValue):
            cBoard[row][i] = sMarker
    else:  # for vertical
        overlap = True
        while overlap:
            overlap = False
            row = random.randint(0, 9 - sValue)
            col = random.randint(0, 9)
            for i in range(row, row + sValue):
                if cBoard[i][col] != ' e0 ':
                    overlap = True
        for i in range(row, row + sValue):
            cBoard[i][col] = sMarker

    return cBoard


#################################
def setupUserBoard(uBoard, uPts):
    print('')
    print('           @@@@@ Plot Your Aircraft Carrier @@@@@')
    print('')
    ## Aircraft Carrier ##
    uBoard = userPlotShip(uBoard, 5, '-a0-')
    uPts = uPts + 5
    ## Destroyer ##
    uBoard = userPlotShip(uBoard, 4, '-d0-')
    uPts = uPts + 4
    ## Battleship ##
    uBoard = userPlotShip(uBoard, 3, '-b0-')
    uPts = uPts + 3
    ## Submarine ##
    uBoard = userPlotShip(uBoard, 3, '-s0-')
    uPts = uPts + 3
    ## Cruiser ##
    uBoard = userPlotShip(uBoard, 2, '-c0-')
    uPts = uPts + 2
    return uBoard, uPts


####################
def enterRow(start):
    prompt = ('Row for ' + start + ' coordinate (1 thru 10) => ')
    row = input(prompt)
    while row not in '1 2 3 4 5 6 7 8 9 10':
        print('Sorry, Sir! Invalid Row. Please re-enter.')
        row = input(prompt)
    row = int(row) - 1
    return row


####################
def enterCol(start):
    prompt = ('Column for ' + start + ' coordinate (A thru J) => ')
    col = input(prompt)
    col = col.upper()
    while col not in 'ABCDEFGHIJ':
        print('Sorry, Sir! Invalid Column. Please re-enter.')
        col = input(prompt)
        col = col.upper()
    col = 'ABCDEFGHIJ'.index(col)

    return col


##########################################
def userPlotShip(uBoard, sValue, sMarker):
    print('          Here is the current board.')
    displayBoard(uBoard, 'user')
    orientation = ' '
    while not orientation in 'HV':
        orientation = input('Horiz(H) or Vert(V)? ')
        orientation = orientation.upper()
    if orientation == 'H':
        print('Aye-aye, Sir! Plot ship Horizontally!')
        overlap = True
        while overlap:
            overlap = False
            row = enterRow('left hand')
            col = enterCol('left hand')
            if col + sValue > 10:
                print('Invalid column. We must have ', sValue, ' spaces.')
                overlap = True
            else:
                for i in range(col, col + sValue):
                    if uBoard[row][i] != ' e0 ':
                        overlap = True
                        print('There is a ship at that position, Sir!')
        for i in range(col, col + sValue):
            uBoard[row][i] = sMarker
    else:  # orientation == 'V'
        print('Aye-aye, Sir! Plot ship Vertically!')
        overlap = True
        while overlap:
            overlap = False
            row = enterRow('top')
            col = enterCol('top')
            if row + sValue > 10:
                print('Invalid row. We must have ', sValue, ' spaces.')
                overlap = True
            else:
                for i in range(row, row + sValue):
                    if uBoard[i][col] != ' e0 ':
                        overlap = True
                        print('There is a ship at that position, Sir!')
        for i in range(row, row + sValue):
            uBoard[i][col] = sMarker

    return uBoard


################################
def pickASquare(uBoard):
    aRow = -1
    aCol = -1
    ## Run thru all board locations ##
    for row in range(10):
        for col in range(10):
            ## See if current location has been HIT ##
            if ('1' in uBoard[row][col] and uBoard[row][col] != ' e1 '):
                if row == 0:  # First Row
                    if '1' not in uBoard[row + 1][col]:  # checkDown
                        aRow = row + 1
                        aCol = col
                        break

                    if col == 0:
                        if '1' not in uBoard[row][col + 1]:  # checkRight
                            aRow = row
                            aCol = col + 1
                            break

                    elif col == 9:
                        if '1' not in uBoard[row][col - 1]:  # checkLeft
                            aRow = row
                            aCol = col - 1
                            break

                    else:
                        if '1' not in uBoard[row][col - 1]:  # checkLeft
                            aRow = row
                            aCol = col - 1
                            break
                        if '1' not in uBoard[row][col + 1]:  # checkRight
                            aRow = row
                            aCol = col + 1
                            break
                elif row == 9:  # Last Row
                    if '1' not in uBoard[row - 1][col]:  # checkUp
                        aRow = row - 1
                        aCol = col
                        break

                    if col == 0:
                        if '1' not in uBoard[row][col + 1]:  # checkRight
                            aRow = row
                            aCol = col + 1
                            break

                    elif col == 9:
                        if '1' not in uBoard[row][col - 1]:  # checkLeft
                            aRow = row
                            aCol = col - 1
                            break

                    else:
                        if '1' not in uBoard[row][col - 1]:  # checkLeft
                            aRow = row
                            aCol = col - 1
                            break
                        if '1' not in uBoard[row][col + 1]:  # checkRight
                            aRow = row
                            aCol = col + 1
                            break
                else:
                    if col == 0:
                        if '1' not in uBoard[row][col + 1]:  # checkRight
                            aRow = row
                            aCol = col + 1
                            break
                        if '1' not in uBoard[row - 1][col]:  # checkUp
                            aRow = row - 1
                            aCol = col
                            break
                        if '1' not in uBoard[row + 1][col]:  # checkDown
                            aRow = row + 1
                            aCol = col
                            break

                    elif col == 9:
                        if '1' not in uBoard[row][col - 1]:  # checkLeft
                            aRow = row
                            aCol = col - 1
                            break
                        if '1' not in uBoard[row - 1][col]:  # checkUp
                            aRow = row - 1
                            aCol = col
                            break
                        if '1' not in uBoard[row + 1][col]:  # checkDown
                            aRow = row + 1
                            aCol = col
                            break
                    else:
                        if '1' not in uBoard[row][col + 1]:  # checkRight
                            aRow = row
                            aCol = col + 1
                            break
                        if '1' not in uBoard[row][col - 1]:  # checkLeft
                            aRow = row
                            aCol = col - 1
                            break
                        if '1' not in uBoard[row - 1][col]:  # checkUp
                            aRow = row - 1
                            aCol = col
                            break
                        if '1' not in uBoard[row + 1][col]:  # checkDown
                            aRow = row + 1
                            aCol = col
                            break

                    # end if col
                # end else
            # end if '1' in
        # end for col
        if aRow != -1:
            break
    # end for row
    if aRow == -1 and aCol == -1:
        aRow = random.randint(0, 9)
        aCol = random.randint(0, 9)
    return aRow, aCol


###############################
def getComputerMove(uBd, uPts):
    cls()
    displayBoard(uBd, 'user')
    print("Here's the User Board")
    print("The computer will pick a point to bomb")
    input('Press <Enter> to continue...')
    row, col = pickASquare(uBd)

    if (uBd[row][col] == ' e0 '):
        # missedSound.play()  # Plays a sound if it's a miss
        cls()
        print('***** Computer Missed *****')
        uBd[row][col] = ' e1 '
    else:
        # hitSound.play()  # Plays a sound if it's a hit
        cls()
        print('***** Warning *****')
        print('Computer Scored a HIT')
        uBd[row][col] = uBd[row][col].replace('0', '1')
        uPts = uPts - 1

    displayBoard(uBd, 'user')
    input('Press <Enter> to continue')
    return uBd, uPts


#############################
def getUserMove(cBd, cPts):
    displayBoard(cBd, 'computer')
    print("Here's the computer board.")
    print('Pick he coordinates to bomb.')
    row = enterRow('Bomb')
    col = enterCol('Bomb')
    while ('1' in cBd[row][col]):
        print('This has been bombed')
        row = enterRow('Bomb')
        col = enterCol('Bomb')

    if (cBd[row][col] == ' e0 '):
        # missedSound.play() #Plays a sound if it's a miss
        print('You Missed')
        cBd[row][col] = ' e1 '
    else:
        # hitSound.play()  #Plays a sound if it's a hit
        cls()
        print('You have scored a hit')
        cBd[row][col] = cBd[row][col].replace('0', '1')
        cPts = cPts - 1

    displayBoard(cBd, 'computer')
    input('Press <Enter> to continue')
    return cBd, cPts


#############
def main():
    cls()
    myName = wantIntro()

    cPts = 20
    uPts = 20

    currentPlayer = firstTurn()

    computerBoard = getNewBoard()
    computerBoard, cPts = setUpComputerBoard(computerBoard, cPts)
    # displayBoard(computerBoard,'computer')
    # for x in range(10):
    #   for y in range(10):
    #      print(computerBoard[x][y], end='')
    # end for y
    # print()
    # end for x

    userBoard = getNewBoard()
    userBoard, uPts = setupUserBoard(userBoard, uPts)
    cls()
    # displayBoard(userBoard,'user')

    while cPts > 0 and uPts > 0:
        if currentPlayer == 'user':
            computerBoard, cPts = getUserMove(computerBoard, cPts)
            # AI for user turn
            currentPlayer = 'computer'
        else:  # computer turn
            # AI for computer turn
            userBoard, uPts = getComputerMove(userBoard, uPts)
            currentPlayer = 'user'

    displayResult(cPts, uPts)
    playagain()


main()
