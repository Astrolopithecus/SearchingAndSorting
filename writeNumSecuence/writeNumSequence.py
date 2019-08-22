##Recursive function that returns the following pattern:
##for i = 0 writeNumSequence(i) returns 1
##for i = 1 writeNumSequence(i) returns 1
##for i = 2 writeNumSequence(i) returns 1 1
##for i = 3 writeNumSequence(i) returns 2 1 2
##for i = 4 writeNumSequence(i) returns 2 1 1 2
##for i = 5 writeNumSequence(i) returns 3 2 1 2 3
##for i = 6 writeNumSequence(i) returns 3 2 1 1 2 3
##for i = 7 writeNumSequence(i) returns 4 3 2 1 2 3 4
##for i = 8 writeNumSequence(i) returns 4 3 2 1 1 2 3 4
##for i = 9 writeNumSequence(i) returns 5 4 3 2 1 2 3 4 5

def writeNumSequence(n):
    if (n <= 1): # Base case for odd numbers
        return "1"
    elif (n  == 2): # Base case for even numbers
        return "1 1"
    else:
        #Same pattern works for both odd or even numbers
        s = str((n+1)//2)
        return s + " " + writeNumSequence(n-2) + " " + s
