import nltk

'''
This function returns a list of tuples of (word, PoS) from a document.
'''
def create_word_pos_list(message):
    tokenized_txt = nltk.word_tokenize(message)
    return nltk.pos_tag(tokenized_txt)
