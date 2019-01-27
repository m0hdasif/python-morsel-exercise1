from collections import Counter
import re

def count_words(text):
    return Counter([word.lower() for word in re.findall("[A-z'-]*", text) if word])
