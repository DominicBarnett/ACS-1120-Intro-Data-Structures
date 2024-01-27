import random

file_path = 'Code/Great_Gatsby.txt'
def read_words_file(file_path):
    with open(file_path, 'r') as file:
        words = file.read().splitlines()
    return words

# LOOK AT MAKING ALL WORDS LOWERCASE AND TAKING OUT ALL PUNCTUATION
# LOOK AT FROM COLLECTIONS IMPORT COUNTER (Don't do keep the written out code)


one_line_txt = read_words_file(file_path)

def string_txt_file(one_line_txt):
    base_string_txt_file = ' '.join(one_line_txt)
    string_txt_file = base_string_txt_file.lower()
    return string_txt_file

source_text = string_txt_file(one_line_txt).split()

# print(source_text)


def histogram(source_text):
    histogram = {}
    for i in source_text:
        if i in histogram:
            histogram[i] += 1
        else:
            histogram[i] = 1
    return histogram

word_count = histogram(source_text)
# print(word_count)

def unique_words(histogram):
    return len(histogram)

def frequency(word, histogram):
    return histogram[word]

word = random.choice(source_text)
word_frequency = frequency(word, word_count)
print(f'"{word}" appears {word_frequency} times')