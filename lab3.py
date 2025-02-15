############################################################
# Name: Jasraj Baweja
# Pledge: I pledge my honor that I have abided by the Stevens Honor System.
# CS115 Lab 3
#
############################################################

def change(amount, coins):

    '''This function takes two inputs, an amount of money and a list of coin types, and returns the least number of coins that makes up that amount of money.'''

    if amount<=0:
        return 0

    if coins == []:
        return float("inf")

    elif len(coins) == 1: 
        return 1+change(amount -1, coins)

    elif coins[len(coins)-1]>amount:
        return change(amount, coins[:-1])

    else:
        use_it = 1+change(amount-coins[len(coins)-1], coins)
        lose_it = change(amount, coins[:-1])
        return min(use_it, lose_it)
