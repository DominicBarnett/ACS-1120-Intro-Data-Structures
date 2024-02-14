
file_path = '/Users/dominic/Desktop/Applied Computer Science/ACS-1120/ACS-1120-Intro-Data-Structures/Code/Great_Gatsby.txt'
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