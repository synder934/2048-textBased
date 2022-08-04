
from random import randint
from copy import deepcopy
import msvcrt
import os

from numpy import char


validInputs = ['w','a','s','d']


def display(i: list):
    lenDic= {
        1:'   ',
        2:'  ',
        3:' ',
        4:''
    }
    out = f'''+------+------+------+------+
| {i[0][0]}{lenDic[len(str(i[0][0]))]} | {i[0][1]}{lenDic[len(str(i[0][1]))]} | {i[0][2]}{lenDic[len(str(i[0][2]))]} | {i[0][3]}{lenDic[len(str(i[0][3]))]} |
+------+------+------+------+
| {i[1][0]}{lenDic[len(str(i[1][0]))]} | {i[1][1]}{lenDic[len(str(i[1][1]))]} | {i[1][2]}{lenDic[len(str(i[1][2]))]} | {i[1][3]}{lenDic[len(str(i[1][3]))]} |
+------+------+------+------+
| {i[2][0]}{lenDic[len(str(i[2][0]))]} | {i[2][1]}{lenDic[len(str(i[2][1]))]} | {i[2][2]}{lenDic[len(str(i[2][2]))]} | {i[2][3]}{lenDic[len(str(i[2][3]))]} |
+------+------+------+------+
| {i[3][0]}{lenDic[len(str(i[3][0]))]} | {i[3][1]}{lenDic[len(str(i[3][1]))]} | {i[3][2]}{lenDic[len(str(i[3][2]))]} | {i[3][3]}{lenDic[len(str(i[3][3]))]} |
+------+------+------+------+'''
    return out

def vert(b: list, dir: str):
    canMove= False

    dirDic={
        -1:[1,2,3],
        1:[2,1,0]
    }

    while True:
        movements= 0
        for line in range(4):
            for pos in dirDic[dir]:
                if b[pos+dir][line] == ' ' and b[pos][line] != ' ':
                    b[pos+dir][line] = b[pos][line]
                    b[pos][line] = ' '
                    movements+=1
                    canMove = True
                
                if b[pos+dir][line] == b[pos][line] and b[pos][line] != ' ':
                    b[pos+dir][line] = b[pos+dir][line]*2
                    b[pos][line] = ' '
                    movements+=1
                    canMove = True

        if movements == 0: break
    return b, canMove

def horz(b: list, dir: int):
    dirDic={
        -1:[1,2,3],
        1:[2,1,0]
    }
    canMove = False
    while True:
        movements= 0
        for line in b:
            for val in dirDic[dir]:
                if line[val+dir] == ' ' and line[val] != ' ':
                    line[val+dir] = line[val]
                    line[val] = ' '
                    movements+=1
                    canMove = True

                if line[val+dir] == line[val] and line[val] != ' ':
                    line[val+dir] = line[val+dir]*2
                    line[val] = ' '
                    movements+=1
                    canMove = True

        if movements == 0: break
    return b, canMove

def move(move: str, b: list):
    if move == validInputs[0]:
        b, canMove = vert(b, -1)
        pass

    elif move == validInputs[1]:
        b, canMove = horz(b, -1)
        pass

    elif move == validInputs[2]:
        b, canMove = vert(b, 1)
        pass

    elif move == validInputs[3]:
        b, canMove = horz(b, 1)
        pass

    return b, canMove

def addNewNum(b:list):
    while True:
        x,y = randint(0,3), randint(0,3)
        if b[x][y] == ' ':
            b[x][y] = 2
            break


def checkLose(b:list):
    for m in validInputs:
        check= move(m, b)[1]
        if check == True: return True
    return False

validInputs = ['w','a','s','d']

while True:
    board = [[' ' for x in range(0,4)] for y in range(0,4)]
    addNewNum(board)
    while True:
        os.system('CLS')
        if checkLose(deepcopy(board)) == False: break
        try:
            print(f'{display(board)}\nur move! <{validInputs}>: ')
            turn= msvcrt.getwch()
            print(turn)
            validInputs.index(turn)
            board, canMove = move(turn, board)
            if canMove == False: raise Exception
        except:
            continue
        addNewNum(board)
        pass
    score=0
    for x in range(4):
        for y in range(4):
            if board[y][x] > score:
                score = board[y][x]
    if input(f'{display(board)}\nyour score was {score}!!!\n\nreplay? <y>: ') == 'y':
        continue
    break