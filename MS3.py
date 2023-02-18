import requests
from collections import Counter
import re

def tokenise(text):
    return re.sub(r'[^\w\s]','',text).lower()

def make_ngrams(words, n):
    ngrams = []
    for i in range(len(words) - n + 1):
        ngrams.append(tuple(words[i:i+n]))
    return ngrams 

page_content = requests.get('https://www.gutenberg.org/cache/epub/100/pg100.txt').text
words = re.split('\s+', tokenise(page_content))

for i in range(2,6):
    print("Mostest commmon{}-grams:".format(i))
    print(Counter(make_ngrams(words,i)).most_common(10))
