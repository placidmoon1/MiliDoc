from konlpy.tag import Mecab
tokenizer = Mecab()

def mark_space(dict):
    key_list = []
    for i in dict.keys():
        key_list.append(i)

        dict_li = []
        key_list = []
        for key in dict.keys():
            key_list.append(key)

        for key in range(len(key_list) - 1):
            end = dict[key]['end_index']
            start = dict[key + 1]['start_index']
            gap = start - end - 1
            dict_li.append(dict[key])
            if gap != 0:
                tmp = 0
                for i in range(gap):
                    tmp += 1
                    dict_li.append({'word': end + tmp, 'char_type': None, 'start_index': None, 'end_index': None,
                                    'forbidden_exist': 0, 'forbidden': '', 'abandon_exist': 0, 'english_exist': 0, 'english': ''})

        dict_li.append(dict[len(key_list) - 1])

        len_li = len(dict_li)

        for i in range(1,len_li):
            dict[i] = dict_li[i]
        return dict

