from mark_noun import find_space

def output_list(text, dict):
    #print(dict)
    dict_li = []
    line = find_space(text)[2]
    space = find_space(text)[3]
    #print('line', line)
    #print('space', space)
    for key,value in dict.items():
        del value['forbidden_exist']
        del value['english_exist']
        del value['char_type']
        del value['start_index']
        del value['end_index']
        word = value['word']
        if type(word) == int:
            if word in line:
                value['word'] = "\n"
                dict_li.append(value)
                #print(key, value, dict_li)
            elif word in space:
                value['word'] = " "
                dict_li.append(value)
                #print(key, value, dict_li)
        else:
            dict_li.append(value)
    #print(dict)
    #print(dict_li)

    return dict_li