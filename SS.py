from bs4 import BeautifulSoup
from selenium import webdriver
import re
import json
import string
import urllib.request

import nltk
from nltk.corpus import stopwords

from wordcloud import WordCloud
import matplotlib.pyplot as plt



def get_author_id(author_name):
    author_id_list=[]

    if ' 'in author_name:
        Author_name = author_name.replace(' ','%20')
    url = "https://www.semanticscholar.org/search?q=%22"+Author_name+"%22&sort=relevance"
    browser = webdriver.Firefox(executable_path='/Users/richie/Downloads/geckodriver')  # Get local session of firefox
    browser.get(url)  # Load page

    soup = BeautifulSoup(browser.page_source,'lxml')
    author_list = soup.find_all(class_='matched-author-list__author-name')
    for i in author_list:
        i = str(i)
        author_id_list.append(re.split('/|"',i)[6])
    return author_id_list

# end def


def get_author_paper(author_id):
    paper_title = []
    paper_info = []
    url = 'http://api.semanticscholar.org/v1/author/' + author_id
    with urllib.request.urlopen(url) as f:
        data = json.loads(f.read().decode())
        for i in data['papers']:
            paper_info.append(i['title'])
            paper_title.append(i['title'])

    return paper_title,paper_info

#end def


def preprocess(author_paper):
    toks_list = []
    stop = stopwords.words('english')
    snowball = nltk.SnowballStemmer('english')
    for i in author_paper:
        words = i.split()
        toks = [t.lower() for t in words if t not in string.punctuation]
        toks = [t for t in toks if t not in stop]
        toks = [snowball.stem(t) for t in toks]
        #toks = [ wnl.lemmatize(t) for t in toks ]
        toks_clean = [t for t in toks if len(t) >= 3]
        for t in toks_clean:
            toks_list.append(t)
    return toks_list

#end def



