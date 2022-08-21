# from client_input import raw_text
# import pandas as pd
# from mark_noun import mark_noun
# from mark_forbidden import mark_forbidden
# from mark_abandon import mark_abandon
# from mark_english import mark_english
# from mark_space import mark_space
# from make_output_list import output_list
#
# from pathlib import Path
# cur_path = str(Path(__file__).resolve().parent)
# df_forbidden = pd.read_csv(cur_path + '/forbidden_words.csv')
# df_abandon = pd.read_csv(cur_path + '/abandon_words.csv')
#
# # df_abandon = pd.read_csv('/Users/choejaehyeog/Documents/대회/국방부데이터경진대회/data/abandon_words.csv')
# # df_forbidden = pd.read_csv('/Users/choejaehyeog/Documents/대회/국방부데이터경진대회/data/forbidden_words.csv')
#
# import time
#
# start = time.time()
# start1 = time.time()
# start2 = time.time()
# start3 = time.time()
# start4 = time.time()
# start5 = time.time()
#
# print(raw_text)
# output_dict = {}
# mark_noun(raw_text, output_dict) # 1)word 2) noun: 고유어 여부 3) word_length: key해당하는 단어의 길이
# # print("start1", time.time() - start1) #0.03
# mark_forbidden(output_dict) # 1) forbidden_exists: 금칙어존재여부 2) forbidden: 금지어 존재한다면 바꿀수 있는 단어
# # print("start2", time.time() - start2) # 2.5
# mark_abandon(output_dict) # 1) abandon_exist: 금지어존재여부
# # print("start3", time.time() - start3) #5.86
# mark_english(output_dict) # 1) english_exist: 영문존재여부 2) english: 존재한다면 어떻게 바꿀 수 있는지
# # print("start4", time.time() - start4)
# mark_space(raw_text, output_dict) #1) space: 단어 뛰어쓰기 여부 2) line_change: 줄바꾸는 함수 존재여부
# # print("start5", time.time() - start5)
#
# #순서가 뒤바껴도 되는 위 다른 함수들과 달리, 딕셔너리 리스트를 반환함. 무조건 마지막에 써야하는 함수.
# final_list = output_list(output_dict) #1)jump: 단어간 띄어쓰기를 표시해줌 ) jump_change: 이전 단어를 기점으로 줄바꿈 일어남을 나타냄
#
# print(final_list)
# print(time.time() - start)

from client_input import raw_text
import pandas as pd
from mark_noun import mark_noun
from mark_forbidden import mark_forbidden
from mark_abandon import mark_abandon
from mark_english import mark_english
from mark_space import mark_space
from make_output_list import output_list
from mark_acronym import mark_acronym

from pathlib import Path
cur_path = str(Path(__file__).resolve().parent)
df_forbidden = pd.read_csv(cur_path + '/forbidden_words.csv')
df_abandon = pd.read_csv(cur_path + '/abandon_words.csv')

# df_abandon = pd.read_csv('/Users/choejaehyeog/Documents/대회/국방부데이터경진대회/data/abandon_words.csv')
# df_forbidden = pd.read_csv('/Users/choejaehyeog/Documents/대회/국방부데이터경진대회/data/forbidden_words.csv')

import time

start = time.time()
start1 = time.time()
start2 = time.time()
start3 = time.time()
start4 = time.time()
start5 = time.time()

print(raw_text)
output_dict = {}
mark_noun(raw_text, output_dict) # 1)word 2) noun: 고유어 여부 3) word_length: key해당하는 단어의 길이
# print("start1", time.time() - start1) #0.03
mark_forbidden(output_dict) # 1) forbidden_exists: 금칙어존재여부 2) forbidden: 금지어 존재한다면 바꿀수 있는 단어
# print("start2", time.time() - start2) # 2.5
mark_abandon(output_dict) # 1) abandon_exist: 금지어존재여부
# print("start3", time.time() - start3) #5.86
mark_english(output_dict) # 1) english_exist: 영문존재여부 2) english: 존재한다면 어떻게 바꿀 수 있는지
# print("start4", time.time() - start4)
mark_acronym(output_dict)
# extract_space(raw_text, output_dict)
mark_space(output_dict) #1) space: 단어 뛰어쓰기 여부 2) line_change: 줄바꾸는 함수 존재여부
# # print("start5", time.time() - start5)
#
# #순서가 뒤바껴도 되는 위 다른 함수들과 달리, 딕셔너리 리스트를 반환함. 무조건 마지막에 써야하는 함수.
final_list = output_list(raw_text, output_dict) #1)jump: 단어간 띄어쓰기를 표시해줌 ) jump_change: 이전 단어를 기점으로 줄바꿈 일어남을 나타냄
#
print(final_list)
print(time.time() - start)
