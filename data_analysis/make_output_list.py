from mark_noun import find_space

def output_list(text, dict):
    dict_li = []
    # print(dict.keys())
    line = find_space(text)[2]
    space = find_space(text)[3]
    for key, value in dict.items():
        del value['forbidden_exist']
        del value['english_exist']
        del value['char_type']
        del value['start_index']
        del value['end_index']
        del value['acronym_exist']
        word = value['word']
        if type(word) == int:
            if word in line:
                value['word'] = "\n"
                dict_li.append(value)
            elif word in space:
                value['word'] = " "
                dict_li.append(value)
        else:
            dict_li.append(value)
    return dict_li
