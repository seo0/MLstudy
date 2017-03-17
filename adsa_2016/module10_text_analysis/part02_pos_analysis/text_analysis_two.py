"""
Your task for this week is to implement some functions to understand the complexity of a text
based on the info provided by nltk PoS (Part-of-speech) tagging.

The function get_nltk_tagged_from_text() is GIVEN and it returns a pos-tagged nltk text from a
generic string. This function can be used to tag any generic text in a string variable.

Note that all functions are supposed to work on texts tagset with tagset='universal'
"""
from operator import itemgetter

import nltk
from nltk.book import *

from module10_text_analysis.part01_lexical_complexity.text_analysis_one import get_nltk_text_from_string



def get_nltk_tagged_from_text(str):
    """
    This function return a text tagged using the universal tagset from a string. This tagged text
    can be used to run more complex analysis, e.g., by looking at number of adjectives used etc.
    :param text_non_tagged:
    :return:
    """
    text_nt = get_nltk_text_from_string(str)
    text_tagged = nltk.pos_tag(text_nt, tagset='universal')
    return text_tagged

def fraction_pos(tagged_text):
    """
    This function calculates the fraction of nouns, adjectivs and verbs in a text tagged_text. In particular:
    (i) it prints a message on console, e.g.
    "the fraction of nouns is X, adjectives is Y and verbs is Z"
    (ii) it returns the 3 values X, Y, and Z

    """
    #sentence_tokenized = nltk.word_tokenize(sentence)
    #sentence_tagged = nltk.pos_tag(sentence_tokenized,tagset='universal')
    pass

def compare_adj_count(text_a, text_b):
    """
    This function compares 2 texts text_a and text_b based on the number of adjectives used.
    In particular, it should print a message like:
    "Text <...> used more adjectives that Text <....>
    Relative number of adjectives in Text<....> is X
    Relative number of adjectives in Text<....> is Y
    """
    pass


def get_sorted_list(dictionary):
    return sorted(dictionary.items(), key=itemgetter(1), reverse=True)


def rank_on_pos_count(text_list, pos):
    """
    Given a list of texts and a part-of-speech identifier (e.g. 'NOUN', 'ADJ', etc.), this function
    ranks the texts in the list based on their value of the fraction of pos (from high to low)

    To implement this function, you may want to use the function get_sorted_list() above, which, given
    a dictionary, returns a list whose element are sorted based on the values in the dictionary (see exampled in the main)

    :param text_list:
    :param pos can be 'ADJ', 'NOUN', 'VERB' etc.
    :return:
    """
    # build a dictionary storing the fraction value for each text
    pass




if __name__ == '__main__':

    """ Demonstrating use of get_sorted_list()"""
    dict = {"A" : 987, "B" : 56, "C" : 55, "W" : 988, "P" : 89}
    print(dict)
    sorted_list = get_sorted_list(dict)
    print(sorted_list)
    print("\t")



    """ =======  Testing faction_pos() """
    tagged_t1 = get_nltk_tagged_from_text("Today is a beautiful day")
    tagged_t2 = get_nltk_tagged_from_text("Today is a beautiful, shiny, solar, exceptional, important and gorgeous day")
    fraction_pos(tagged_t1)
    fraction_pos(tagged_t2)

    """ =======  Testing compare_adj_count() """
    #compare_adj_count(text1, text2)
    #compare_adj_count(text2, text3)
    #compare_adj_count(text3, text4)

    """ ======= testing ranking ==========="""
    text_list = [text1, text2, text3, text4, text6, text7]
    rank_on_pos_count(text_list, 'ADJ')