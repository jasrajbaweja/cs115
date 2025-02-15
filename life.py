#
# life.py - Game of Life lab
#
# Name:
# Pledge:
#

import sys
import random

def createOneRow(width):
    '''This function returns one row of zeros of width "width"...
    You should use this in your createBoard(width,height) function'''
    row = []
    for col in range(width):
        row += [0]
    return row


def createBoard(width,height):
    '''This function returns creates a board with "height" rows and "width" cols'''
    A = []
    for row in range(height):
        A += [createOneRow(width)]
    return A

#print(createBoard(5,3))

def printBoard(A):
    '''This function prints out the 2d list-of-lists A without spaces'''
    for row in A:
        for col in row:
            sys.stdout.write(str(col))
        sys.stdout.write('\n')

#A = createBoard(5,3)
#printBoard(A)

def diagonalize(width,height):
    '''This function creates an empty board and then modifies it so that it
    has a diagonal strip of "on" cells'''
    A =createBoard(width,height)
    for row in range(height):
        for col in range(width):
            if row == col:
                A[row][col] = 1
            else:
                A[row][col] = 0
    return A

#A = diagonalize(7,6)
#printBoard(A)

def innerCells(w,h):
    '''This function creates a board with inner cells as 1's'''
    A = createBoard(w, h)
    for row in range(1, h - 1):
        for col in range(1, w - 1):
            A[row][col] = 1
    return A

#A = innerCells(5,5)
#printBoard(A)

def randomCells(w,h):
    '''This function returns an array of randomly-assigned 1's and 0's
    except the outer edge of the arry is completely empty'''
    A = innerCells(w,h)
    for row in range(h):
        for col in range(w):
            if A[row][col] == 1:
                A[row][col] = random.choice([0,1])
    return A

#A = randomCells(10,10)
#printBoard(A)

def copy(A):
    '''This function is a helper function copies a board and returns the copy'''
    newA = []
    for row in range(len(A)):
        newRow = []
        for col in range(len(A[row])):
            newRow.append(A[row][col])
        newA.append(newRow)
    return newA

#oldA = createBoard(2,2)
#printBoard(oldA)

#newA = copy(oldA)
#printBoard(newA)

#oldA[0][0] = 1
#printBoard(oldA)

#printBoard(newA)

def innerReverse(A):
    '''This function reverses the inner values and changes one generation
    of cells into a new generation'''
    newA = copy(A)
    height = len(newA)
    width = len(newA[0])
    for row in range(1, height - 1):
        for col in range(1, width - 1):
            if newA[row][col] == 1:
                newA[row][col] = 0
            else:
                newA[row][col] = 1
    return newA

#A = randomCells(8,8)
#printBoard(A)

#A2 = innerReverse(A)
#printBoard(A2)


def countNeighbor(A,r,c):
    '''This function counts the neighbors around an element'''
    count = 0
    for row in range(r-1, r+2):
        for col in range(c-1, c+2):
            if not(row == r and col == c) and A[row][col] == 1:
                count += 1
    return count

#A = randomCells(8,8)
#printBoard(A)
#print(countNeighbor(A,3,4))           
    

def next_life_generation(A):
    '''This function runs the game and using the rules specified returns the proceeding game level'''
    newA = copy(A)
    height = len(newA)
    width = len(newA[0])
    for row in range(height):
        for col in range(width):
            if row == 0 or row == height-1 or col == 0 or col == width-1:
                newA[row][col] = 0
            elif countNeighbor(A, row, col) < 2:
                newA[row][col] = 0
            elif countNeighbor(A, row, col) > 3:
                newA[row][col] = 1
            elif countNeighbor(A, row, col) == 3 and newA[row][col] == 0:
                newA[row][col] = 1
    return newA



#A = [[0,0,0,0,0],
#[0,0,1,0,0],
#[0,0,1,0,0],
#[0,0,1,0,0],
#[0,0,0,0,0]]
#printBoard(A)


#A2 = next_life_generation(A)
#printBoard(A2)

#A3 = next_life_generation(A2)
#printBoard(A3)
