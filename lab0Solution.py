############################################################
# Name: Jasraj Baweja
# Pledge: I pledge my honor that I have abided by the Stevens Honor System.
# CS115 Lab 0
#
############################################################

def same(x):

    ###The function below is going to convert the strong the user inputs into lowercase.

    x=x.lower()

    ###It will automatically return true if there is only one letter in the string.

    if len(x)==1:
        return True;
    first = x[0]

    if x[0]==x[-1]:
        return True
    else:
        return False
    
def consecutiveSum(x, y):
    ##Used the formula that was provided in the instructions in order to create a function.

    return (x+y)/2*(y-x-1)

