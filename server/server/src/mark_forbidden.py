from pydoc import cli
import pandas as pd
from konlpy.tag import Mecab
from check import raw_text_morphs
from new_ngram import ngram
tokenizer = Mecab()

from pathlib import Path
cur_path = str(Path(__file__).resolve().parent )
df_forbidden = pd.read_csv(cur_path + '/forbidden_words.csv')

def mark_forbidden_pre(dict):
    #print('in mark_forbidden_pre')
    df_old_list = df_forbidden['금칙어'].astype(str).tolist()
    df_list = []
    df_ind_list = []

    for i in range(len(df_old_list)):
        if df_old_list[i] != 'nan':
            if len(df_old_list[i].split(",")) > 1:
                li_add = df_old_list[i].split(",")
                len_li_add = len(li_add)
                df_list.extend(li_add)
                for j in range(len_li_add):
                    df_ind_list.append(i)
            else:
                df_list.append(df_old_list[i])
                df_ind_list.append(i)

    client_input_li = raw_text_morphs
    client_input_li_len = len(client_input_li)
    total_li = []
    #print(client_input_li_len)
    for i in range(client_input_li_len):
        total_li.append(i)

    for num in total_li:
        dict[num]["forbidden_exist"] = 0
        dict[num]["forbidden"] = ""

    return df_ind_list, df_list

def find_ngram(len_token):
    dict = {len_token : ngram(len_token, raw_text_morphs)}
    return dict

def mark_forbidden(dict):
    function_result = mark_forbidden_pre(dict)
    ind_li = function_result[0]
    forbid_li = function_result[1]
    is_forbidden_li = []

    tmp = []
    for i in forbid_li:
        tmp.append(tokenizer.morphs(i))

    len_li = []
    for word in forbid_li:
        token_word = word
        len_word_morphs = len(token_word)
        len_li.append(len_word_morphs)

    len_li = list(set(len_li))

    ngram_dict = {}
    for i in len_li:
        ngram_dict.update(find_ngram(i))

    for word in tmp:
        token_word = word
        token_word_sentence = "".join(token_word)
        len_word_morphs = len(token_word)
        li_ngram_token = ngram_dict.get(len_word_morphs)
        if token_word_sentence in li_ngram_token:
            find_location = ind_li[tmp.index(word)]
            right_word = df_forbidden['단어명'][find_location]
            word_location = li_ngram_token.index(token_word_sentence)
            for i in range(word_location, word_location + len_word_morphs):
                dict[i]["forbidden_exist"] = 1
                is_forbidden_li.append(i)
                dict[i]["forbidden"] = "see previous"
            dict[word_location]["forbidden"] = right_word

    return dict