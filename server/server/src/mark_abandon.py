# import pandas as pd
# from konlpy.tag import Mecab
# from client_input import raw_text_morphs
# from new_ngram import ngram
# tokenizer = Mecab()
#
# df_abandon = pd.read_csv('/Users/choejaehyeog/Documents/대회/국방부데이터경진대회/data/abandon_words.csv')
#
# def mark_abandon(dict):
#     df_old_list = df_abandon['금지어'].astype(str).tolist()
#     df_list = []
#     df_ind_list = []
#
#     for i in range(len(df_old_list)):
#         if df_old_list[i] != 'nan':
#             if len(df_old_list[i].split(",")) > 1:
#                 li_add = df_old_list[i].split(",")
#                 len_li_add = len(li_add)
#                 df_list.extend(li_add)
#                 for j in range(len_li_add):
#                     df_ind_list.append(i)
#             else:
#                 df_list.append(df_old_list[i])
#                 df_ind_list.append(i)
#
#     client_input_li = raw_text_morphs
#     client_input_li_len = len(client_input_li)
#     total_li = []
#
#     for i in range(client_input_li_len):
#         total_li.append(i)
#
#     for num in total_li:
#         dict[num]['abandon_exist'] = 0
#
#     for word in df_list: #휴대폰을 챙겨오는 징병관은 못됏어
#         token_word = tokenizer.morphs(word)
#         token_word_sentence = "".join(token_word)
#         len_word_morphs = len(token_word)
#         li_ngram_token = ngram(len_word_morphs, client_input_li)
#         if token_word_sentence in li_ngram_token:
#             #지금부터 선소집을 sex 금지한다 우선 소집원 출원자들 섹스 징병관님 명령이야
#             word_location = li_ngram_token.index(token_word_sentence)
#             for i in range(word_location, word_location+len_word_morphs):
#                 dict[i]['abandon_exist'] = 1
#
#     return dict
import pandas as pd
from konlpy.tag import Mecab
from new_ngram import ngram
tokenizer = Mecab()

from pathlib import Path

cur_path = str(Path(__file__).resolve().parent)
df_abandon = pd.read_csv(cur_path + '/abandon_words.csv')

def find_ngram(len_token):
    from check import raw_text_morphs
    dict = {len_token : ngram(len_token, raw_text_morphs)}
    return dict

def mark_abandon(dict):
    df_old_list = df_abandon['금지어'].astype(str).tolist()
    df_list = []

    for word in df_old_list:
        df_list.append(tokenizer.morphs(word))
        
    from check import raw_text_morphs
    client_input_li = raw_text_morphs
    client_input_li_len = len(client_input_li)
    total_li = []

    for i in range(client_input_li_len):
        total_li.append(i)

    for num in total_li:
        dict[num]['abandon_exist'] = 0

    len_li = []
    for word in df_list:
        token_word = word
        len_word_morphs = len(token_word)
        len_li.append(len_word_morphs)

    len_li = list(set(len_li))

    ngram_dict = {}
    for i in len_li:
        ngram_dict.update(find_ngram(i))

    char_morphs = ["NNG", "NNP", "VV", "VA", "MM", "IC", "XPN", "XR", "SL"]
    for word in df_list: #휴대폰을 챙겨오는 징병관은 못됏어
        token_word = word
        token_word_sentence = "".join(token_word)
        len_word_morphs = len(token_word)
        li_ngram_token = ngram_dict.get(len_word_morphs)
        if token_word_sentence in li_ngram_token:
            ind = li_ngram_token.index(token_word_sentence)
            if dict[ind]['char_type'] in char_morphs:
                #지금부터 선소집을 sex 금지한다 우선 소집원 출원자들 섹스 징병관님 명령이야
                word_location = li_ngram_token.index(token_word_sentence)
                for i in range(word_location, word_location+len_word_morphs):
                    dict[i]['abandon_exist'] = 1

    return dict