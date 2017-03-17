"""
Your task is to implement the two functions below.

Note below the import statement to reuse the code that you have already seen in this week's "preclass"
"""
from module04_stacks_and_queues.part00_preclass.stack import ArrayStack

def transfer(S,T):
    """
    tranfer all the elements from stack S to stack T such that the elements at the top of S is the first
    to be inserted onto T, and the element at the bottom of S ends up at the top of T
    (that is, T will look like S with elements in reverse order)
    Note: you can assume that T is always EMPTY
    """
    pass

def print_reverse_order():
    """ This function reads a sequence of words provided through command line terminated by the "stop" word
    and prints them in reverse order.
    Each word is separated by the "enter", run the main() below for how to read user input from command line
    """
    pass

if __name__ == '__main__':
    """
    Run this to understand how to read user input from command line
    """
    print("Enter one word: ")
    word1 = input()
    print("You entered: {0}".format(word1))
    print("---- Read a sequence of words ---")
    word = " "
    stop = False
    while not stop:
        word = input()
        print("You entered: {0}".format(word))
        if word == "stop":
            print("STOP!")

    """
    NOTE: add some code to test your implementation of the two functions transfer and print_reverse_order
    """




