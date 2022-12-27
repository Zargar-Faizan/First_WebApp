#created by faizan
import operator


def count(article):
    words = article.split()
    word_count = len(words)
    dict_words = {}
    for i in words:
        if i in dict_words:
            dict_words[i] = dict_words[i] + 1
        else:
            dict_words[i] = 1

    dic_words_sorted = sorted(dict_words.items(), key=operator.itemgetter(1), reverse=True)
    return dic_words_sorted, word_count