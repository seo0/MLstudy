#problem3 바이너리 서치 만들기(1,2번을 빨리 끝냈으면)

from time import sleep

def is_sorted(array):
    pass
    """
    Check if an array is sorted in ascending order (assumes an array of numbers, such as integers or float)
    :param array: the array to be checked
    :return: a message ("Array is sorted" or "Array is not sorted")
    """
    pass

def binary_search(array, elem, first, last):
    pass

    """
    Search for an element in an array using binary search
    :param array: array to look for element
    :param elem: the element to look for
    :param first: the index of the first position in the array
    :param last: the index of the last position in the array
    :return: a message showing the element (if found) or "Element not found" (if not found)
    """
    pass

#main은 건들이지 마시오.
""" main() to test the implementation"""
if __name__ == '__main__':
    # A is sorted
    A = (1,5,6,7,9,13,16,17)
    # B is not sorted
    B = (1,6,7,8,2)
    print(is_sorted(A))
    print(is_sorted(B))
    # Search for element 16 in A
    print(binary_search(A, 16, 0, len(A) - 1))
    #Serach for element 56 in A
    print(binary_search(A, 56, 0, len(A) - 1))
"""
===output===
Array is sorted
Array is not sorted
True
False
"""

