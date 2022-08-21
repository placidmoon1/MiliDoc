from flask import Blueprint, Flask, render_template, make_response, url_for, session, request
from flask_cors import cross_origin, CORS
import pyrebase, re

from mySecrets import firebaseConfig

firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()
db = firebase.database()

raw_text_morphs = []

bp = Blueprint("check", __name__, url_prefix="/check")
CORS(bp)

@bp.route('/text2', methods=["GET", "POST"])
def check_text2():
  """
  a sanitized query (s_query) should:
  (1) 
  """
  if request.method == "POST":
    #NOTE: split at, but preserve delimiter (tab, newline, space)
    raw_text = ''  
    #print('raw_text:', raw_text)
    import pandas as pd
    from mark_noun import mark_noun
    from mark_forbidden import mark_forbidden
    from mark_abandon import mark_abandon
    from mark_english import mark_english
    from mark_space import mark_space
    from make_output_list import output_list
    from pathlib import Path
    #NOTE: FREAKING AMAZING REGEX PATTERN! SPLIT & PRESERVE PATTERN!!!
    split_text = re.split('([\t|\n| |\r])',request.form["text"])
    #print('split_text', split_text)
    for i in split_text:
      if i == '' or i == '\r': 
        continue
      raw_text += i
    #print(raw_text)
    cur_path = str(Path(__file__).resolve().parent)

    df_abandon = pd.read_csv(cur_path + '/abandon_words.csv')
    df_forbidden = pd.read_csv(cur_path + '/forbidden_words.csv')
    from konlpy.tag import Mecab
    tokenizer = Mecab()

    global raw_text_morphs 
    raw_text_morphs = tokenizer.morphs(raw_text)
    #print("check() raw text morphs", raw_text_morphs)
    import time

    start = time.time()

    print_flag = True

    output_dict = {}
    mark_noun(raw_text, output_dict) # 1)word 2) noun: 고유어 여부 3) word_length: key해당하는 단어의 길이
    if print_flag:
      print("start1", time.time() - start) #0.03
      #print(output_dict)
    mark_forbidden(output_dict) # 1) forbidden_exists: 금칙어존재여부 2) forbidden: 금지어 존재한다면 바꿀수 있는 단어
    if print_flag:
      print("start2", time.time() - start) # 2.5
      #print(output_dict)
    mark_abandon(output_dict) # 1) abandon_exist: 금지어존재여부
    if print_flag:
      print("start3", time.time() - start) #5.86
    mark_english(output_dict) # 1) english_exist: 영문존재여부 2) english: 존재한다면 어떻게 바꿀 수 있는지
    if print_flag:
      print("start4", time.time() - start)
    mark_space(output_dict) #1) space: 단어 뛰어쓰기 여부 2) line_change: 줄바꾸는 함수 존재여부
    if print_flag:
      print("start5", time.time() - start)

    #순서가 뒤바껴도 되는 위 다른 함수들과 달리, 딕셔너리 리스트를 반환함. 무조건 마지막에 써야하는 함수.
    final_list = output_list(raw_text, output_dict) #1)jump: 단어간 띄어쓰기를 표시해줌 ) jump_change: 이전 단어를 기점으로 줄바꿈 일어남을 나타냄

    """if print_flag:
      print(final_list)"""
    print("time to process:", time.time() - start)
    return final_list, 200
  else:
    return "/check/test (POST) splits text input by space, and preserves Korean, English, and numbers", 200

@bp.route('/text', methods=["GET", "POST"])
def check_text():
  """
    a sanitized query (s_query) should:
    (1) 
  """
  if request.method == "POST":
    #NOTE: split at, but preserve delimiter (tab, newline, space)
    raw_text = request.form["text"]  
    import pandas as pd
    from mark_noun import mark_noun
    from mark_forbidden import mark_forbidden
    from mark_abandon import mark_abandon
    from mark_english import mark_english
    from mark_space import mark_space
    from make_output_list import output_list
    from pathlib import Path

    cur_path = str(Path(__file__).resolve().parent)

    df_abandon = pd.read_csv(cur_path + '/abandon_words.csv')
    df_forbidden = pd.read_csv(cur_path + '/forbidden_words.csv')
    from konlpy.tag import Mecab
    tokenizer = Mecab()

    global raw_text_morphs 
    raw_text_morphs = tokenizer.morphs(raw_text)
    #print("check() raw text morphs", raw_text_morphs)
    import time

    start = time.time()

    print_flag = True

    output_dict = {}
    mark_noun(raw_text, output_dict) # 1)word 2) noun: 고유어 여부 3) word_length: key해당하는 단어의 길이
    if print_flag:
      print("start1", time.time() - start) #0.03
      #print(output_dict)
    mark_forbidden(output_dict) # 1) forbidden_exists: 금칙어존재여부 2) forbidden: 금지어 존재한다면 바꿀수 있는 단어
    if print_flag:
      print("start2", time.time() - start) # 2.5
      #print(output_dict)
    mark_abandon(output_dict) # 1) abandon_exist: 금지어존재여부
    if print_flag:
      print("start3", time.time() - start) #5.86
    mark_english(output_dict) # 1) english_exist: 영문존재여부 2) english: 존재한다면 어떻게 바꿀 수 있는지
    if print_flag:
      print("start4", time.time() - start)
    mark_space(output_dict) #1) space: 단어 뛰어쓰기 여부 2) line_change: 줄바꾸는 함수 존재여부
    if print_flag:
      print("start5", time.time() - start)

    #순서가 뒤바껴도 되는 위 다른 함수들과 달리, 딕셔너리 리스트를 반환함. 무조건 마지막에 써야하는 함수.
    final_list = output_list(raw_text, output_dict) #1)jump: 단어간 띄어쓰기를 표시해줌 ) jump_change: 이전 단어를 기점으로 줄바꿈 일어남을 나타냄

    """if print_flag:
      print(final_list)"""
    print("time to process:", time.time() - start)
    return final_list, 200
  else:
    return "/check/test (POST) splits text input by space, and preserves Korean, English, and numbers", 200