# import random
# import sys

# words = open("/usr/share/dict/words", "r")


# def read_file(file_path):
#     with open(file_path, 'r') as file:
#         words = file.read().splitlines()
#     return words

# def random_words(num_of_words):
#     set_of_words = []
#     for i in num_of_words:
#         random_word = random.sample(words.read(), num_of_words)
#         set_of_words.append(random_word)
#         return set_of_words

    





# if __name__ == "__main__":
#     # Check if there are command-line arguments
#     if len(sys.argv) < 2:
#         print("Usage: python dictionary_words.py <number of words>")
#         sys.exit(1)

#     # Get the words from command-line arguments
#     num_of_words = sys.argv[1:]

#     # Rearrange the words
#     result = random_words(num_of_words)


#     # # Print the rearranged words
#     print(result)


# Chat GPT
# import random
# import sys

# def read_words_file(file_path):
#     with open(file_path, 'r') as file:
#         words = file.read().splitlines()
#     return words

# def generate_sentence(word_list, num_words):
#     selected_words = random.sample(word_list, num_words)
#     sentence = ' '.join(selected_words)
#     return sentence

# def main():
#     file_path = '/usr/share/dict/words'  # Replace with the actual path to your words file
#     num_words_requested = sys.argv[1:]  # Replace with the number of words you want in the sentence

#     words_list = read_words_file(file_path)

#     # if len(words_list) < num_words_requested:
#     #     print("Error: Not enough words in the file.")
#     #     return

#     sentence = generate_sentence(words_list, num_words_requested)
#     print("Generated Sentence:", sentence)

# if __name__ == "__main__":
#     main()

import random
import sys

def read_words_file(file_path):
    with open(file_path, 'r') as file:
        words = file.read().splitlines()
    return words

def generate_sentence(word_list, num_words):
    selected_words = random.sample(word_list, num_words)
    sentence = ' '.join(selected_words)
    return sentence

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 dictionary_words.py <num_words>")
        return

    file_path = '/usr/share/dict/words'
    num_words_requested = int(sys.argv[1])

    words_list = read_words_file(file_path)

    if len(words_list) < num_words_requested:
        print("Error: Not enough words in the file.")
        return

    sentence = generate_sentence(words_list, num_words_requested)
    print("Generated Sentence:", sentence)

if __name__ == "__main__":
    main()