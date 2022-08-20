def output_list(dict):
    dict_li = []
    for key,value in dict.items():
        if value['space'] == 1:
            dict_li.append(value)
            dict_li.append({
                "word": " ",
                "abandon_exist": 0,
                "english": "",
                "forbidden": "",
                "line_change": 0,
                "noun": 0,
                "space": 0,
                "word_length": 0
            })
        else:
            dict_li.append(value)
        if value['line_change'] == 1:
            dict_li.append({
                "word": "\n",
                "abandon_exist": 0,
                "english": "",
                "forbidden": "",
                "line_change": 0,
                "noun": 0,
                "space": 0,
                "word_length": 0
            })

    return dict_li