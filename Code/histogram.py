import random
from cleanup import source_text

def histogram(source_text):
    histogram = {}
    for i in source_text:
        if i in histogram:
            histogram[i] += 1
        else:
            histogram[i] = 1
    return histogram

histogram_test = histogram(source_text)
# print(histogram_test)

def unique_words(histogram):
    return len(histogram)

def frequency(word, histogram):
    return histogram[word]

