# 1. delcare a list with 9 blocks of empty space
# 2. print the board on screen
# 3. select who will go first
# 4. take input from user A or user B with specific position
# 5. check if the pos is empty then only take it as a valid input, else ask again
# 6. after the input is placed, check is some player has won,its a draw
# 7. ask if the user want to play again
# 8. enter the score for all the matches

def emptylist_xo():
    tmp_list = []
    for i in range(9):
        tmp_list.append(' ')
    return tmp_list
XO_list = emptylist_xo()
def printborad(xolist):
    print(xolist[0], "|", xolist[1], "|", xolist[2])
    print("_________")
    print(xolist[3], "|", xolist[4], "|", xolist[5])
    print("_________")
    print(xolist[6], "|", xolist[7], "|", xolist[8])
# printborad(XO_list)
import random
def whowillgofirst():
    player = random.randint(0,2)
    if player == 0:
        print("player A | O will go first ")
    else:
        print("player B | X will go first ")
    return player
def takeInput(player,xoList):
  print("Hey player, ",player )
  flag = 0
  while flag ==0:
    pos = int(input("Enter the position in between [ 0 to 8] - "))
    if pos>= 0 and pos <= 8:
      if xoList[pos] == ' ':
        print("valid input")
        if player == 0:
          xoList[pos] = 'O'
        else:
          xoList[pos] = 'X'
        return xoList
        flag = 1
      else:
        print("please enter again, its occupied")
        flag = 0
    else:
      print("please give valid input again ")
      flag = 0
# XO_list = takeInput(1,XO_list)
# if return is 0 then player A is winner
# if return is 1 then player B is winner
# if return is 2 then its a draw
def checkWin(xoList):
    flag = 0
    for i in range(9):
        if xoList[i] == ' ':
            flag = 1
    if (xoList[0] == 'O' and xoList[1] == 'O' and xoList[2] == 'O') or (xoList[3] == 'O' and xoList[4] == 'O' and xoList[5] == 'O') or (xoList[6] == 'O' and xoList[7] == 'O' and xoList[8] == 'O') or (xoList[0] == 'O' and xoList[3] == 'O' and xoList[6] == 'O') or (xoList[1] == 'O' and xoList[4] == 'O' and xoList[7] == 'O') or (xoList[2] == 'O' and xoList[5] == 'O' and xoList[8] == 'O') or (xoList[0] == 'O' and xoList[4] == 'O' and xoList[8] == 'O') or (xoList[2] == 'O' and xoList[4] == 'O' and xoList[6] == 'O'):
        print('player A is  winner')
        return 0
    elif (xoList[0] == 'X' and xoList[1] == 'X' and xoList[2] == 'X') or (xoList[3] == 'X' and xoList[4] == 'X' and xoList[5] == 'X') or (xoList[6] == 'X' and xoList[7] == 'X' and xoList[8] == 'X') or (xoList[0] == 'X' and xoList[3] == 'X' and xoList[6] == 'X') or (xoList[1] == 'X' and xoList[4] == 'X' and xoList[7] == 'X') or (xoList[2] == 'X' and xoList[5] == 'X' and xoList[8] == 'X') or (xoList[0] == 'X' and xoList[4] == 'X' and xoList[8] == 'X') or (xoList[2] == 'X' and xoList[4] == 'X' and xoList[6] == 'X'):
        print('player B is  winner')
        return 1
    elif flag == 1 :
        return -1
    else:
        print("match is draw")
        return 2
# printborad(XO_list)

XO_list = emptylist_xo()
printborad(XO_list)
play = whowillgofirst()
ScoreA = 0
ScoreB = 0

gameStatus = 0
chance = 0

while gameStatus == 0:
    if play == 0:
        XO_list = takeInput(0, XO_list)
        printborad(XO_list)
        winStat = checkWin(XO_list)
        play = 1
    else:
        XO_list = takeInput(1, XO_list)
        printborad(XO_list)
        winStat = checkWin(XO_list)
        play = 0

    if winStat == 0 or winStat == 1 or winStat == 2:
        gameStatus = 1
        print('win - ', winStat)
    else:
        gamestatus = 0