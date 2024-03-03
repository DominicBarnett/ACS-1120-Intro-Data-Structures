
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