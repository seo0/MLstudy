# Note the import of the function time
# from ... import is the Python's construct to reuse "modules" (i.e., other programmes) in your own programme
# for more about it: https://en.wikibooks.org/wiki/A_Beginner%27s_Python_Tutorial/Importing_Modules
from time import time
from time import sleep

"""
In this week you will implement and test the functions example1 and example3 of p.143 in the GTG book
and test their execution time.
The functions are given, so you should only try to understand their code.
However, the main is not given, so you should implement your own main to test these functions.
Both function take as input a list S (not a dictionary!!!)

What is the Big-Oh complexity of example1 and example3?
"""



def example1(S):
    """
    EXAMPLE 1: Return the sum of the elements in S
    :param S: a sequence of numbers, e.g. [3, 9, 2]
    :return: the sum of elements in S
    """
    #time() captures the value of current system time
    start_time = time()
    n = len(S)
    total = 0
    for j in range(n):
        """sleep(0.15) delays the execution of each execution of the loop of 0.15 seconds
        This to add some constant delay, otherwise your computer will probably
        be too fast to see some meaningful time difference in executing such a simple algorithm!"""
        sleep(0.15)
        total += S[j]
    end_time = time()
    exec_time = end_time - start_time
    print("EXAMPLE 1 - Sum of elements in S is: {0}".format(total))
    print("EXAMPLE 1 - EXEC TIME: {0} seconds".format(exec_time))


def example3(S):
    """
    EXAMPLE 1: Return the sum of prefix sums in S
    :param S: a sequence of numbers, e.g. [3, 9, 2]
    :return: the sum of prefix sums in S
    """
    start_time = time()
    n = len(S)
    total = 0
    for j in range(n):
        #the sleep(0.15) delays the execution of 0.15 seconds (same reason as above)
        sleep(0.15)
        for k in range(j+1):
            #again, same reason as above
            sleep(0.15)
            total += S[k]
    end_time = time()
    exec_time = end_time - start_time
    print("EXAMPLE 2 - Sum of all prefix sums in S is: {0}".format(total))
    print("EXAMPLE 2 - EXEC TIME: {0} seconds".format(exec_time))



"""main() function to test: this is the code that is executed when you "Run" this file
To "Run" this file, right click on the file in the left panel and click "Run compare_exec_times"
"""
if __name__ == '__main__':
    """ implement here your own code to test these two functions """
