import nltk
from bs4 import BeautifulSoup

import urllib.request
from nltk.corpus import PlaintextCorpusReader
from nltk.corpus import BracketParseCorpusReader

import sys

from urllib.request import urlopen

# IDEA: work only with texts (no corpora)
# text analysis part 2: create some statistics using tagged texts
# assignment: do the scraping of at least 10 articles per type of news and do some statistics, compare the result
# analysis: lexical complexity (using all indicators), number of adjectives, other new indicators (which ones???)



def bad_html_news_scraper(url):
    with urllib.request.urlopen(url) as response:
        html = response.read()


    #html = urllib.urlopen(url).read()
    soup = BeautifulSoup(html, "html.parser")

    # kill all script and style elements
    for script in soup(["script", "style"]):
        script.extract()    # rip it out

    # get text
    text = soup.get_text()

    # break into lines and remove leading and trailing space on each
    lines = (line.strip() for line in text.splitlines())
    # break multi-headlines into a line each
    chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
    # drop blank lines
    text = '\n'.join(chunk for chunk in chunks if chunk)

    #print(text)

    #f=open('my-file.txt','rU')
    #raw=f.read()

    return text

if __name__ == '__main__':
    #url = "https://www.theguardian.com/sport/2016/sep/26/anthony-joshua-wladimir-klitschko-heavyweight-unification-fight-barry-hearns"
    url = "https://www.theguardian.com/commentisfree/2016/nov/09/rise-of-the-davos-class-sealed-americas-fate"
    url_korea = "http://www.koreatimes.co.kr/www/news/nation/2016/09/281_214854.html"

    #second_html_news_scraper(url)

    #if input():
    #    sys.exit()

    # SCRAPE ENGLISH NEWS
    text_eng = bad_html_news_scraper(url)

    print(text_eng)




    # SCRAPE KOREAN NEWS
    text_kor = bad_html_news_scraper(url_korea)

    print(text_kor)


    # EXAMPLES OF HOW TO TOKENIZE AND TAG THE SCRAPED TEXTS AND PRINT THEM ON FILE
    text_eng = nltk.word_tokenize(text_eng)
    text_eng = nltk.Text(text_eng)
    text_eng = nltk.pos_tag(text_eng, tagset='universal')

    text_kor = nltk.word_tokenize(text_kor)
    text_kor_tagged_words = nltk.pos_tag(text_kor, tagset='universal')

    file_eng = open("./texts/eng_new.txt","w", encoding='utf8', errors='ignore')
    file_eng.write(str(text_eng))
    file_eng.close()

    file_kor = open("./texts/kor_new.txt", "w", encoding='utf8', errors='ignore')
    file_kor.write(str(text_kor))
    file_kor.close()



    #text = news.raw('eng_new.txt')
    #print(text)

    # unedrstand how to tag an existing text or corpus
    # get some statistics







#page = requests.get('http://econpy.pythonanywhere.com/ex/001.html')
#page = requests.get('http://www.latimes.com/nation/politics/trailguide/la-na-trump-clinton-debate-updates-1474947924-htmlstory.html')
#tree = html.fromstring(page.content)
#print()


#print(html2text("<p>Hello, world.</p>"))