################################################################
#Name: Jasraj Baweja
#Pledge: I pledge my honor to abide by the Stevens Honor System.
#CS 115 HW 4
################################################################

def pascal_row(n):
    '''This function takes an integer as an input and outputs a list of elements found in a certain row of Pascal’s Triangle'''
    if n==0:
        return [1]
    elif n==1:
        return [1,1]
    else:
        return [1]+pascal_help(pascal_row(n-1))

def pascal_help(lst):
    '''This function takes a list as an input and outputs a new list of sums of adjacent terms in the original list'''
    if lst==[]:
        return []
    elif len(lst)==1:
        return [1]
    else:
        return [lst[0]+lst[1]]+pascal_help(lst[1:])

def pascal_triangle(n):
    '''This function takes an integer as an input and outputs a list of lists containing the values of the all the rows up to and including row n'''
    if n==0:
        return [[1]]
    elif n==1:
        return[[1],[1,1]]
    else:
        return pascal_triangle(n-1)+[pascal_row(n)]

def test_pascal_row():
    '''This function tests the pascal_row function'''
    assert pascal_row(1)==[1,1]
    assert pascal_row(2)==[1,2,1]
    assert pascal_row(3)==[1,3,3,1]
    assert pascal_row(4)==[1,4,6,4,1]

def test_pascal_triangle():
    '''This function tests the pascal_triangle function'''
    assert pascal_triangle(1)==[[1],[1,1]]
    assert pascal_triangle(2)==[[1],[1,1],[1,2,1]]
    assert pascal_triangle(3)==[[1],[1,1],[1,2,1],[1,3,3,1]]
    assert pascal_triangle(4)==[[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
