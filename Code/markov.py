import random
from cleanup import source_text
from dictogram import Dictogram

class markov_chain(dict):
    def __init__(self):
        self.chain = Dictogram()

    def add_word_pair(self, word_1, word_2):
        if word_1 in self.chain:
            if word_2 in self.chain[word_1]:
                self.chain[word_1][word_2] += 1
            else:
                self.chain[word_1][word_2] = 1
        else:
            self.chain[word_1] = {word_2: 1}

    def create_chain_from_text(self, corpus):
            for i in range(len(corpus) - 1):
                self.add_word_pair(corpus[i], corpus[i + 1])

    def walk(self, length=50):
        current_word = random.choice(list(self.chain.keys()))
        text = [current_word]
        for _ in range(length - 1):
            if current_word in self.chain:
                next_word = random.choices(list(self.chain[current_word].keys()), 
                                           weights=list(self.chain[current_word].values()))[0]
                text.append(next_word)
                current_word = next_word
            else:
                break
        return ' '.join(text)

if __name__ == '__main__':
    corpus = source_text

    mc = markov_chain()
    markov_chain = markov_chain()
    markov_chain.create_chain_from_text(corpus)  # Change this to your text file's path
    generated_text = markov_chain.walk()
    print(generated_text)

    