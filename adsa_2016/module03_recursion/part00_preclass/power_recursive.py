"""
Your task is to complete the implementation of the functions below:
1) recursive_power: this function calculates the power of a number in a recursive way
2) non_recursive power: this function calculates the power in a non-recursive way
"""


def recursive_power(base, power):
    """
    Calculate the power of a number RECURSIVELY
    :param base: the base
    :param power: the power
    :return: the value of 'base' elevated to the power of 'power, e.g. base = 2, power = 3, returns 8
    """
    pass

def non_recursive_power(base, power):
    """
        Calculate the power of a number NON recursively
        :param base: the base
        :param power: the power
        :return: the value of 'base' elevated to the power of 'power, e.g. base = 2, power = 3, returns 8
    """
    pass




""" main() to d osome testing"""
if __name__ == '__main__':

    #Test the power() function
    base = 3
    power1 = 3
    power2 = 4
    print("Result: {0}".format(recursive_power(base, power1)))
    print("Result: {0}".format(non_recursive_power(base, power1)))
    print("Result: {0}".format(recursive_power(base, power2)))
    print("Result: {0}".format(non_recursive_power(base, power2)))

    power1 = 0
    print("Result: {0}".format(recursive_power(base, power1)))
    print("Result: {0}".format(non_recursive_power(base, power1)))
