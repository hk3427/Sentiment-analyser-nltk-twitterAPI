from nltk.corpus import gutenberg
from nltk.tokenize import sent_tokenize


sample = gutenberg.raw("bible-kjv.txt")
###Check out the corpora folder in nltk_data

tok = sent_tokenize(sample)
for x in range(5):
    print(tok[x])