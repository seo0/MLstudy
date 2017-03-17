"""
Your task is to complete the implementation of the functions below.
Some functions implement different metrics to evaluate the  "lexical richness" of a "text"
The rank_on_lex_complexity() functions allows to rank 3 texts based on lexical richness

The function get_nltk_text_from_string() is GIVEN and allows you to create a nltk "text" from
a string variable.
Note that a nltk text isin practice a Python list of strings.
"""

from nltk.book import *
from time import sleep
import nltk




def get_nltk_text_from_string(str):
    """
    This function is GIVEN and returns a "text" obtained from a
    string that can be used with the functions provided by NLTK
    :param str:
    :return:
    """
    text = nltk.word_tokenize(str)
    return text




def metric1(text,weights):
    """
    Lexical complexity in this case is calculated as
    the normalised number of words in text longer than weights[0], that is,
    the number of long words divied by the total number of words in the text
    :param text:
    :param weights:
    :return:
    """
    pass


def metric2(text, weights):
    """
    lexical complexity in this case is the normalised number of hapaxes in text longer than weights[0]
    (a hapax is a word that appears only once in a text)
    :param text:
    :param weights:
    :return:
    """
    pass


def metric3(text, weights):
    """
    lexical complexity in this case is the sum of metric1 and metric2 weighted by weights[2] and weights[3], that is:
    weights[2] * metric1 + weights[3] * metric2
    Note: to stay normalised between 0 and 1, weights[2] + weights[3] must be 1.0 (and weights[2], weights[3] < 1)
    Note 2: weights[0] is the parameter required by metric1, weights[1] the parameter required by metric2
    :param text:
    :param weights:
    :return:
    """
    pass

def rank_on_lex_complexity(text_a, text_b, text_c, metric, weights=[]):
    """
    This function prints out the most complex corpus among a b and c based on the value of a complexity "metric"
    which can be "0" (metric0), "1", "2" or "3"
    weights is the list of parameter required to calculate the value of metrics
    Note: your function should check, for the chosen metric, that weights[] has the correct number and values
    of parameters
    """
    # calculate metric value: have to managed parameters carefully
    pass



if __name__ == '__main__':
    # some code to test your functions

    str = "This is an example of a custom string that we want to transform into a " \
          "nltk text. To do this, we can call the function that is defined above. Using this function, we " \
          "can process wih nltk any string that we want (example: see next week's twitter stream analysis, " \
          "where we will use nltk to process twitter streams"
    text_new = get_nltk_text_from_string(str)
    print(metric2(text_new, [1]))
    print("\n")


    print(metric1(text1, [6]))
    print(metric1(text2, [6]))
    print("\n")

    print(metric2(text1, [6]))
    print(metric2(text2, [6]))
    print("\n")

    print(metric3(text2, [6, 6, 0.4, 0.6]))
    print(metric3(text2, [6, 6, 0.4, 0.7]))
    print("\n")


    print(rank_on_lex_complexity(text1, text2, text3, "1", [2]))
    sleep(0.2)
    print("\n")

    print(rank_on_lex_complexity(text1, text2, text3, "1", [2, 4]))
    sleep(0.2)
    print("\n")

    print(rank_on_lex_complexity(text1, text2, text3, "2", [2]))
    sleep(0.2)
    print("\n")

    print(rank_on_lex_complexity(text1, text2, text3, "2", [2, 4]))
    sleep(0.2)
    print("\n")

    print(rank_on_lex_complexity(text1, text2, text3, "3", [6, 6, 0.3, 0.7]))
    sleep(0.2)
    print("\n")

    print(rank_on_lex_complexity(text1, text2, text3, "3", [6, 6, 0.4, 2.6]))
    sleep(0.2)
    print("\n")

    print(rank_on_lex_complexity(text1, text2, text3, "3", [6, 0.4, 2.6]))

    print("\n")

