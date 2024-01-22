
file_path = 'Great_Gatsby.txt'
def read_words_file(file_path):
    with open(file_path, 'r') as file:
        words = file.read().splitlines()
    return words

one_line_txt = read_words_file(file_path)

def string_txt_file(one_line_txt):
    string_txt_file = ' '.join(one_line_txt)
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

# word_count = histogram(source_text)
# print(word_count)

def unique_words(histogram):
    pass

def frequency(word, histogram):
    pass