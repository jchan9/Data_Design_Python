import matplotlib.pyplot as plt
import requests
from bs4 import BeautifulSoup
from nltk.tokenize import RegexpTokenizer
import nltk
from nltk.corpus import stopwords
import re

def gutenberg_plot(url):
    response = requests.get(url)
    christmas = BeautifulSoup(response.content, 'html.parser')
    christmas_carol = christmas.get_text()
    christmas_words = re.findall ('\w+', christmas_carol)
    tokenizer = RegexpTokenizer('\w+')
    christmas_tokens = tokenizer.tokenize(christmas_carol)
    lowered = []
    for word in christmas_tokens:
        lowered.append(word.lower())
    stop_words = set (stopwords.words('english'))
    no_stop_words = [w for w in lowered if not w in stop_words]
    text = nltk.Text(no_stop_words)
    freq_text = nltk.FreqDist(text)
    top_words = freq_text.most_common(30)
    freq_text.plot(20)