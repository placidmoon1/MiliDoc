import pandas as pd
from konlpy.tag import Mecab
from new_ngram import ngram
tokenizer = Mecab()
from pathlib import Path

cur_path = str(Path(__file__).resolve().parent)
df_forbidden = pd.read_csv(cur_path + '/forbidden_words.csv')
def mark_english_pre(dict):
    df_old_list = df_forbidden['영문명'].astype(str).tolist()
    df_forbidden['단어명'] = df_forbidden['단어명'].astype(str)
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
    from check import raw_text_morphs
    client_input_li = raw_text_morphs
    client_input_li_len = len(client_input_li)
    total_li = []
    english_exist_li = []

    for i in df_ind_list:
        english_exist_li.append(tokenizer.morphs(df_forbidden['단어명'][i]))

    for i in range(client_input_li_len):
        total_li.append(i)

    for num in total_li:
        dict[num]["english_exist"] = 0
        dict[num]["english"] = ""
    return df_ind_list, english_exist_li

def find_ngram(len_token):
    from check import raw_text_morphs

    dict = {len_token : ngram(len_token, raw_text_morphs)}
    return dict

def mark_english(dict):
    function_result = mark_english_pre(dict)
    ind_li = function_result[0]
    eng_li = function_result[1]

    len_li = []
    for word in eng_li:
        token_word = word
        len_word_morphs = len(token_word)
        len_li.append(len_word_morphs)

    len_li = list(set(len_li))

    ngram_dict = {}
    for i in len_li:
        ngram_dict.update(find_ngram(i))

    char_morphs = ["NNG", "NNP", "VV", "VA", "MM", "IC", "XPN", "XR"]
    for word in eng_li:
        token_word = word
        token_word_sentence = "".join(token_word)
        len_word_morphs = len(token_word)
        li_ngram_token = ngram_dict.get(len_word_morphs)
        if token_word_sentence in li_ngram_token:
            ind = li_ngram_token.index(token_word_sentence)
            if dict[ind]['char_type'] in char_morphs:
                find_location = ind_li[eng_li.index(word)]
                english_word = df_forbidden['영문명'][find_location]
                word_location = li_ngram_token.index(token_word_sentence)
                for i in range(word_location, word_location + len_word_morphs):
                    dict[i]["english_exist"] = 1
                    dict[i]["english"] = "see previous"
                dict[word_location]["english"] = english_word

    return dict