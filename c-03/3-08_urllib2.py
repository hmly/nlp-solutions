import nltk
import urllib2
from urllib import urlopen


def URL_html_free(url):
    html = urlopen(url).read()
    raw = nltk.clean_html(html)
    tokens = nltk.word_tokenize(raw)
    contents = nltk.Text(tokens)
    
    return contents
