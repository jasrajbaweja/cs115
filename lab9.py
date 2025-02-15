###########################################################
# Name: Jasraj Baweja
# Pledge: I pledge my honor that I have abided by the Stevens Honor System. -Jasraj Baweja
# Date Created: November 13, 2024
# CS 115 Lab 9
###########################################################

from cs5png import *

#Introduction to for Loops!
def mult(c,n):
    '''This function uses only a loop and addition to multiply c by the integer n.'''
    result = 0
    for i in range(n):
        result += c
    return result

'''
print('mult')

print(mult(6,7))
print(mult(1.5,28))

print('')
'''

def update(c,n):
    '''This function starts with z=0 and runs z = z**2 + c for a total of n times. It returns the final z.'''
    z = 0
    for i in range(n):
        if i == n:
            return z
        z = z**2 + c
    return z

'''
print('update')

print(update(1,3))
print(update(-1,3))
print(update(1,10))
print(update(-1,10))

print('')
'''

#The inMSet function
def inMSet(c,n):
    '''This function takes the inputs c and n, and uses n as the maximum number of times to run that step to see if c follows an MSet'''
    z = 0
    for i in range(n):
        z = z**2 +c
        if abs(z) > 2:
            return False
        return True

'''
print('inMSet')

c = 0 + 0j
print(inMSet(c,2))

c = 3 + 4j
print(inMSet(c, 25))

c = 0.3 + -0.5j
print(inMSet(c, 25))

c = -0.7 + 0.3j
print(inMSet(c, 25))

c = 0.42 + 0.2j
print(inMSet(c, 25))

print('')
'''

#Creating images with Python
def weWantThisPixel( col, row ):
    '''This function returns True if we want the pixel at col, row and False otherwise'''
    if col % 10 == 0 and row % 10 == 0:
        return True
    else:
        return False

def test():
    '''If we were to change the line from if col % 10 == 0 and row % 10 == 0
    to if col % 10 == 0 or row % 10 == 0, it would create a grid.'''
    
    '''This function demonstrates how to create and save a png image'''
    width = 300
    height = 200
    image = PNGImage(width, height)
    for col in range(width):
        for row in range(height):
            if weWantThisPixel( col, row ) == True:
                image.plotPoint(col, row)
    image.saveFile()

test()

#Writing the scale function
def scale( pix, pixelMax, floatMin, floatMax ):
    '''This function takes in
        pix, the current pixel column (or row)
        pixMax, the total # of pixel columns
        floatMin, the min floating-point value
        floatMax, the max floating-point value
    The function returns the floating-point value that corresponds to pix'''
    range = floatMax - floatMin
    return (pix/pixelMax) * range + floatMin

'''
print('scale')

print(scale(100, 200, -2.0, 1.0))
print(scale(100, 200, -1.5, 1.5))
print(scale(100, 300, -2.0, 1.0))
print(scale(25, 300, -2.0, 1.0))
print(scale(299, 300, -2.0, 1.0))

print('')
'''

#Visualizing the Mandelbrot set in black and white: mset
def mset():
    '''This function creates a 300x200 image of the Mandelbrot set'''
    width = 300
    height = 200
    image = PNGImage(width,height)
    for col in range(width):
        for row in range(height):
            x = scale(col,width, -2,1)
            y = scale(row, height, -1,1)
            c = x + (y * 1j)
            n = 25
            if inMSet(c,n) == True:
                image.plotPoint(col,row)
    image.saveFile()

mset()
