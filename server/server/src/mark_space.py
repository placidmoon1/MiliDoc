from konlpy.tag import Mecab
tokenizer = Mecab()

def find_space(sentence):
    space_li = [-1]
    new_line_li = [] #글자씩 끊은 경우, 줄 바꿈의 위치
    for ind,i in enumerate(sentence): #"나는 그렇게 왕이 되었다.\n나는 왕이로소이다 \n 알겟 느냐"
        if len(sentence) > 1:
            if i == "\n":
                new_line_li.append(ind)
                space_li.append(ind)
            elif i == " ":
                space_li.append(ind)
        else:
            print("다시 입력해주세요")

    word_gap_li = []
    for i in range(len(space_li)-1):
        word_gap = space_li[i+1] - space_li[i] - 1
        word_gap_li.append(word_gap)

    token_gap_li = []
    token_gap = 0
    for i in range(len(word_gap_li)):
        token_gap += word_gap_li[i]
        token_gap_li.append(token_gap)

    line_gap_li = []
    for i in new_line_li:
        string = sentence[:i].replace("\n", "")
        string = string.replace(" ", "")
        len_string = len(string)
        line_gap_li.append(len_string)

    token_gap_li = list(set(token_gap_li))
    return token_gap_li,line_gap_li

def mark_space(text, dict):
    for ind, i in dict.items():
        if i['word_length'] in find_space(text)[1]:
            dict[ind]['space'] = 0
            dict[ind]['line_change'] = 1 #줄바꾸기
        elif i['word_length'] in find_space(text)[0]:
            dict[ind]['space'] = 1
            dict[ind]['line_change'] = 0
        else:
            dict[ind]['space'] = 0
            dict[ind]['line_change'] = 0

    return dict