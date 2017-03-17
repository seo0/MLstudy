"""
Your task is to complete the functions below, which deal with basic processing
of strings of characters
"""

# this functions only demonstrates how to return multiple values from a function
def foo():
    # note how a function can return an arbitrary number of values
    # see in the main() how to access multiple returned values in your code
    ret_param1 = "Hello"
    ret_param2 = "world"
    ret_param3 = 567
    return ret_param1, ret_param2, ret_param3



def tokenize_imdb_entry(entry):
    """
    This function "tokenises" an entry of the Internet Movie Database (IMDB) by returning
    in separate variables (i) the title of the movie, (ii) the year it was released and (iii) the average review score.
    An entry of the db is a string like "<avg review score> <title> <(year)>"
    Example: "8.7 The Lord of the Rings: The Fellowship of the Ring (2001)"
    Note that <avg review score> is always a number between 0.0 and 9.9 (only one digit after the comma),
    <year> is the year the movie was released (4 digits)
    :param entry: the entry to be tokenized
    :return:
    """
    pass

def add_ing(str1):
    """
    this function add 'ing' at the end of a given string str1 (length of str should be at least 3).
    If the given string already ends with 'ing' then add 'ly' instead.
    If the string length of the given string is less than 3, leave it unchanged
    Sample String : 'abc'
    Expected Result : 'abcing'
    Sample String : 'string'
    Expected Result : 'stringly'
    """
    pass

def check_against_alphabet(str, alphabet_lan):
    """
    This function takes as input a string "str", and checks it against the alphabet specified by alphabet_lan.
    Checking means to print out:
    (i) which letters in the selected alphabet are not in "str"
    (ii) which letters in "str" are not in the selected alphabet
    Assume there are two possible alphabets:
    alphabet_lan = "ENG" is the standard English alphabet, i.e. the string "abcdefghijklmnopqrstuvwyxz"
    alphabet_lan = "ITA" is the standard Italian alphabet "abcdefghilmnopqrstuvz"
    For example, if we check "the quick red fox jumped over the lazy brown sleeping dog" against "ENG",
    it will not output anything, since all the letters of the alphabet are contained in it. If we check
    the same string against "ITA", it will print j, k, x, w, y (which are not in the Italian alphabet)
    If we check "the quick cat jumped over the lazy brown sleeping dog" against "ENG", the function prints 'f' and 'x'.
    !!! Assume also that "str" contains only lower case characters and white spaces !!!
    Beware of white spaces!!!
    """
    pass


def xmlify(word, tag):
    """
    This function creates a XML (or HTML) version of word using the given tag.
    Tha is, it returns a string that wraps the tag "tag" around "word".
    Sample function and result :
    add_tags('i', 'Python') -> '<i>Python</i>'
    add_tags('b', 'Python Tutorial') -> '<b>Python Tutorial </b>'
    :param str1:
    :return:
    """
    pass

if __name__ == '__main__':
    foo_return = foo()
    print(foo_return[0])                        # multiple return values are stored in a list and can be accessed using indexes
    print(foo_return[1])
    print(foo_return[2])
    movie = "8.9 Life is beautiful (2014)"
    tokens = tokenize_imdb_entry(movie)
    print("Title: {0}".format(tokens[0]))
    print("Year: {0}".format(tokens[1]))
    print("Score: {0}".format(tokens[2]))
    str1 = "the quick red fox jumped over the lazy brown sleeping dog"
    str2 = "the quick cat jumped over the lazy brown sleeping dog"
    check_against_alphabet(str1,"ENG")
    check_against_alphabet(str2, "ENG")
    check_against_alphabet(str1, "ITA")
    check_against_alphabet(str2, "ITA")
    print(xmlify("Marco", "name"))