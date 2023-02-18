import requests
from collections import Counter
import re 


page_content = requests.get('https://www.gutenberg.org/cache/epub/100/pg100.txt').text
words = re.split('\W+', page_content)
print(Counter(words).most_common(100))
