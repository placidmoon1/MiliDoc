def output_list(dict):
    dict_li = []
    for key,value in dict.items():
        del(value['forbidden_exist'])
        del(value['english_exist'])
        if value['space'] == 1:
            dict_li.append(value)
            dict_li.append({"word": " "})
        else:
            dict_li.append(value)
        if value['line_change'] == 1:
            dict_li.append({"word": '\n'})

    return dict_li