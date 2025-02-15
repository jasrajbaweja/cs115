############################################################
#Name: Jasraj Baweja
#Pledge: I pledge my honor that I have abided by the Stevens Honor System.
#CS115 Lab 2
#
############################################################

def dot(L,k):
    """The function returns the dot product of the lists L and K"""

    if L==[]:
        return 0
    else:
        return L[0] * k[0]+dot(L[1:], k[1:])
    

def explode(S):
    """Thxe function takes a string S as input and returns a list of the characters"""

    if S == "":
        return []
    else:
         return [S[0]]+explode(S[1:])

def ind(e,L):
    """The function takes a list input and an element. It will return the length of the list if element e is not found in list, or it will return the first index of elemnent"""

    if L==[]:
        return 0
    if L == "":
        return 0
    elif L[0] == e:
        return 0
    else:
        return 1 + ind(e, L[1:])

def removeAll(e,L):
    """The function takes an element and a list and returns the same list after removing all instances of element e."""

    if L==[]:
        return []
    elif L[0]==e:
        return removeAll(e,L[1:])
    return [L[0]] + removeAll(e,L[1:])

def even(X):
    """The function returns if input X is even"""

    if x%2==0:
        return True
    else:
        return False

def myFilter(f, L):
    """The function takes a function and list input and only keeps the elements in the list that make the function return true."""

    if L==[]:
        return []
    if f(L[0]):
        return [L[0]] + myFilter(f, L[1:])
    return (myFilter(f, L[1:]))

def deepReverse(L):
    """This function takes a list input and returns a reversal of the elements in the list; any lists within elements are also reversed."""

    if L==[]:
        return []
    elif isinstance(L[0], list):
        return deepReverse(L[1:]) + [deepReverse(L[0])]
    else:
        return deepReverse(L[1:])+[L[0]]
