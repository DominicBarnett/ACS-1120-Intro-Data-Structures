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
# def total_words_function(source_text):
#     total_words = 0
#     for i in source_text:
#         total_words += 1
#     return total_words



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

total_words = unique_words(histogram(source_text))

def calculate_word_weight(dict_values):
    word_weight = []
    for i in dict_values:
        word_weight.append(i/total_words)
    return word_weight

def generate_word():
    word = random.choices(list(word_count.keys()), weights=word_weight, k=1)[0]
    return word


# word = random.choice(source_text)
dict_values = word_count.values()
word_weight = calculate_word_weight(dict_values)
# word = random.choices(list(word_count.keys()), weights=word_weight, k=1)[0]
# generated_word = generate_word()
# word_frequency = frequency(generated_word, word_count)
# print(f'"{generated_word}" appears {word_frequency} times')