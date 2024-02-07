from cleanup import source_text

def total_words(source_text):
    word_count = 0
    for i in source_text:
        word_count += 1
    return word_count

word_count = total_words(source_text)
# print (word_count)