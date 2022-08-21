from konlpy.tag import Okt
from konlpy.tag import Mecab
okt = Okt()
tokenizer = Mecab()

def find_space(text):
    len_text = len(text)

    li = []
    li_new_line = []
    li_new_space = []

    if text[0] != ' ' or text[0] != '\n':
        li.append(-1)

    for ind, word in enumerate(text):
        if word == "\n" or word == " ":
            li.append(ind)
            if word == "\n":
                li_new_line.append(ind)
            else:
                li_new_space.append(ind)

    if li[-1] != len_text:
        li.append(len_text)

    li_answ = []
    li_q = []
    li_real = []

    tmp = 0
    for i in range(len(li) - 1):
        if li[i + 1] - li[i] != 1:
            tmp += li[i + 1] - li[i] - 1
            li_q.append(li[i + 1] - li[i] - 1)
            li_answ.append(tmp)
            li_real.append(li[i] + 1)

    return li_q, li_real, li_new_line, li_new_space

def mark_noun(text, dict):
    li_gap = find_space(text)[0]
    li_location_= find_space(text)[1]
    token_len = 0
    tmp_start = 0

    for ind, word in enumerate(tokenizer.pos(text)):
        token = word[0]
        gap = len(token)
        token_len += len(token)
        start = li_location_[0]+tmp_start

        if li_gap[0] == token_len:
            token_len = len(token)
            dict[ind] = {'word': word[0], 'char_type': word[1], 'start_index': start, 'end_index': start+token_len-1}
            del li_gap[0]
            del li_location_[0]
            token_len = 0
            tmp_start = 0

        else:
            dict[ind] = {'word': word[0], 'char_type': word[1], 'start_index': start, 'end_index': start + gap - 1}
            tmp_start = token_len

    return dict