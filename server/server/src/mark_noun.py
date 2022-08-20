from konlpy.tag import Okt
from konlpy.tag import Mecab
okt = Okt()
tokenizer = Mecab()

def mark_noun(text, dict):
    len_word = 0
    for word in enumerate(tokenizer.pos(text)):
        len_word += len(word[1][0])
        if word[1][1][0] == 'N':
            dict[word[0]] = {'word': word[1][0], 'noun': 1, 'word_length': len_word}
        else:
            dict[word[0]] = {'word': word[1][0], 'noun': 0, 'word_length': len_word}

    return dict
