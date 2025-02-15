############################################################
# Name: Jasraj Baweja
# Pledge: I pledge my honor that I have abided by the Stevens Honor System.
# CS115 Lab 4
#
############################################################
from functools import reduce

def knapsack(capacity, itemList):
    
    '''this function takes an input and returns the maximum value and the list of items that make this value, without exceeding the capacity of the knapsack'''

    if capacity <= 0:
        return [0,[]]
    elif itemList == []:
        return [0,[]]
    elif itemList[0][0] > capacity:
        return knapsack(capacity,itemList[1:])
    else:
        useIt = knapsack(capacity - itemList[0][0], itemList[1:])
        loseIt = knapsack(capacity, itemList[1:])
        if loseIt[0] < itemList[0][1] + useIt[0]:
            return [itemList[0][1] + useIt[0]] + [[itemList[0]] + useIt[1]]
        else:
            return [loseIt[0]] + [loseIt[1]]
