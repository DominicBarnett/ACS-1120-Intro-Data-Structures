# import random

# list_of_words = ["how", "now", "brown", "cow"]

# print("____TYPE_______")
# print(type(list_of_words))
# print("_____LIST_____")
# print(list_of_words)
# print("_____REARRANGE____")

# for i in list_of_words:
# rearrange = random.sample(list_of_words, len(list_of_words))
# rearrange_string = ' '.join(rearrange)

# print(rearrange_string)
# print("________________")
# print("please input 4 words to rearrange, please type one word followed by the enter key until all four words are inputted")
# word_1 = input()
# word_2 = input()
# word_3 = input()
# word_4 = input()

# input_words = []
# input_words.append(word_1)
# input_words.append(word_2)
# input_words.append(word_3)
# input_words.append(word_4)


# rearrange_input = random.sample(input_words, len(input_words))
# input_string = ' '.join(rearrange_input)
# print('______INPUT REARRANGE______')
# print(input_string)

import sys
import random

def rearrange_words(words):
    shuffled_words = random.sample(words, len(words))
    return ' '.join(shuffled_words)

if __name__ == "__main__":
    # Check if there are command-line arguments
    if len(sys.argv) < 2:
        print("Usage: python rearrange.py <word1> <word2> ...")
        sys.exit(1)

    # Get the words from command-line arguments
    input_words = sys.argv[1:]

    # Rearrange the words
    result = rearrange_words(input_words)

    # Print the rearranged words
    print(result)