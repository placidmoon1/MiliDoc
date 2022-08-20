# from konlpy.tag import Mecab
#
# tokenizer = Mecab()
#
# def one_sentence(list_word):
#     one_sentence_li = []
#     for i in range(len(list_word)):
#         one_sentence_li.append("".join(list_word[i]))
#     return one_sentence_li
#
# def ngram(numbers, sentence_li):
#     ngram_li = []
#     for ind in range(len(sentence_li)-numbers+1):
#         ngram_li.append(sentence_li[ind:ind+numbers])
#     return one_sentence(ngram_li)
#
import time

start = time.time()
start1 = time.time()
start2 = time.time()

from konlpy.tag import Mecab

tokenizer = Mecab()

def one_sentence(list_word):
    one_sentence_li = []
    for i in range(len(list_word)):
        one_sentence_li.append("".join(list_word[i]))
    # print("start2", time.time() - start2)
    return one_sentence_li

def ngram(numbers, sentence_li):
    ngram_li = []
    for ind in range(len(sentence_li)-numbers+1):
        ngram_li.append(sentence_li[ind:ind+numbers])
    # print("start1", time.time() - start1)
    return one_sentence(ngram_li)

