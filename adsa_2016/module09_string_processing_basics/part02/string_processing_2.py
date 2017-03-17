"""
Your task is to complete the functions below, which deal with basic processing
of strings of characters
"""



def count_unique_words(str):
    """
    This functions counts and prints out the number of unique words in string str.
    Example: when applied to "the quick red fox jumped over the lazy brown sleeping fox",
    it should print 9 ("the" and "fox" are repeated).
    Again, assume str contains only lower case characters and white spaces
    :param str:
    :return:
    """
    pass

def find_word_frequencies(text, min):
    """
    This function returns a dictionary storing the frequencies of words in a string "text".
    The dictionary only retains those strings that appear at least "min" times in "text"
    Example: if text = "this is this text" should, then
    find_word_frequencies(text, 1) returns { "this" : 2, "is" : 1, "text" : 1}
    find_word_frequencies(text, 2) returns { "this" : 2}
    """
    pass




if __name__ == '__main__':
    foo_return = foo()
    print(foo_return[0])                        # multiple return values are stored in a list and can be accessed using indexes
    print(foo_return[1])
    print(foo_return[2])


    str1 = "the quick red fox jumped over the lazy brown sleeping dog"
    str2 = "the quick cat jumped over the lazy brown sleeping dog"

    # =========== test count_unique_words() ================
    count_unique_words(str1)
    count_unique_words(str2)
    str3 = "the quick red fox jumped over the quick red sleeping dog"
    count_unique_words(str3)
    str4 = "a quick red fox jumped over the sleeping dog"
    count_unique_words(str4)

    # ============ test find_word_frequencies() =================

    text1 = "this is this text"
    text2 = """over the last week, the fashion groupies
           have stood for hours to get a piece of Topshop,
           sometimes in the rain, sometimes as curious tourists
           took their pictures in their L train get-ups.
           They may have suspected they were being manipulated,
           since the store, which opened at 478 Broadway on
           April 2, did not appear all that crowded. Still,
           they waited, and waited, and then they bought such
           items of this very moment as pink leopard-print
           dresses no bigger than a house cat, black leggings
           with fringe along the sides and sunglasses with
           lenses shaped like lips."""



    print(find_word_frequencies(text1,1))
    print(find_word_frequencies(text1,2))
    print(find_word_frequencies(text2,3))

