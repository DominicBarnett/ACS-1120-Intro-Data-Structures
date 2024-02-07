import random
from histogram import histogram_test
from word_count import word_count


dict_values = histogram_test.values()

def calculate_word_weight(dict_values):
    word_weight = []
    for i in dict_values:
        word_weight.append(i/word_count)
    return word_weight

word_weight = calculate_word_weight(dict_values)

def generate_word():
    word = random.choices(list(histogram_test.keys()), weights=word_weight, k=1)[0]
    return word
