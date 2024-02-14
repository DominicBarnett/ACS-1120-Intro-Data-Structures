import random
from cleanup import source_text


class markov_chain(dict):
    
    
    def __init__(self, corpus, order=1):
        self.word_dict = {}

        for i in range(len(corpus)-order):
            word_1, word_2 = corpus[i], corpus[i+1]
            if word_1 in self.word_dict:
                self.word_dict[word_1].append(word_2)
            else:
                self.word_dict[word_1] = [word_2]

        
    def walk(self):
        first_word = random.choice(list(self.word_dict.keys()))
        while first_word.islower():
            first_word = random.choice(list(self.word_dict.keys()))
        chain = [first_word]

        sentence_length = 10

        for i in range(sentence_length):
            if chain[-1] not in self.word_dict:
                next_word = random.choice(list(self.word_dict.keys()))
            else:
                next_word = random.choice(self.word_dict[chain[-1]])
            chain.append(next_word)
        
        return ' '.join(chain)



if __name__ == '__main__':
    corpus = source_text
    mc = markov_chain(corpus)
    print(mc.walk())