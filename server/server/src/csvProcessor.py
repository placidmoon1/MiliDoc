import pyrebase, csv, re, json

from mySecrets import firebaseConfig
firebase = pyrebase.initialize_app(firebaseConfig)
db = firebase.database()

def check_csv(filepath):
  """
  NOTE: 한국어 인코딩이 깨지면 파일일 csv-utf8 형식으로 재저장 필요!
  """
  csv_rdr = csv.reader(open(filepath, 'r'))
  for row in csv_rdr:
    print(row)

def process_limitWords (filepath, data_type):
  """
  data_type:
  1 = 오픈데이터 (expected schema: 단어 명|물리 명|영문 명|금칙어)
  2 = 행정데이터 (expected schema: 현행|변경)
  5 = 정부데이터 (expected schema: NO|공통표준단어명|공통표준단어영문약어명|공통표준단어영문명|
                  공통표준단어설명|이음동의어목록|금칙어목록)

  """
  limitWord_dict = {}
  csv_rdr = csv.reader(open(filepath, 'r'))
  if data_type == 1:
    for row in csv_rdr:
      if row[3] != '': #there exists a limitWord for the src
        splitted_limitWords = row[3].split(',')
        for limitWord in splitted_limitWords:
          limitWord_data = {'src': 'mil_opendata', 'sugg_word': row[0], 'limit_word': limitWord}
          limitWord_dict[db.generate_key()] = limitWord_data
    #end of for loop
  if data_type == 2:
    row_num = 0
    for row in csv_rdr:
      if row_num == 0:
        row_num = 1
        continue
      if row[1] != '': #there exists a limitWord for the src
        limitWord_data = {'src': 'mil_haengjung', 'sugg_word': row[0], 'limit_word': row[1]}
        db.child("limitWords").push(limitWord_data)
  if data_type == 2:
    row_num = 0
    for row in csv_rdr:
      if row_num == 0:
        row_num = 1
        continue
      if row[1] != '': #there exists a limitWord for the src
        limitWord_data = {'src': 'mil_haengjung', 'sugg_word': row[0], 'limit_word': row[1]}
        db.child("limitWords").push(limitWord_data)
  if data_type == 5:
    row_num = 0
    for row in csv_rdr:
      if row_num == 0:
        row_num = 1
        continue
      if row[6]!= '': 
        splitted_limitWords = row[6].split(',')
        for limitWord in splitted_limitWords:
          limitWord_data = {'src': 'goverment_words', 
                            'sugg_word': row[1], 
                            'limit_word': limitWord.split()[0]}
          db.child("limitWords").push(limitWord_data)
    limitWord_json = json.dumps(limitWord_dict)
    with open("data.json", "w") as f:
      f.write(limitWord_json)
      f.close()
  #option 1 done 

def process_restrictedWords(filepath, data_type):
  restricted_dict = {}
  data_num = 0
  for fp in filepath:
    csv_rdr = csv.reader(open(fp, 'r'))
    row_num = 0
    for row in csv_rdr:
      if row_num == 0:
        row_num += 1
        continue
      if row[1] != '': #there exists a limitWord for the src
        src = ''
        if data_num == 0:
          src = 'naver_restricted'
        if data_num == 1:
          src = 'jyp_bubble_restricted'
        restricted_data = {'src': src, 'restricted_word': row[1]}
        restricted_dict[db.generate_key()] = restricted_data
    data_num += 1

  #processing csv data done
  restricted_words = json.dumps(restricted_dict)
  with open("restricted_words.json", "w") as f:
    f.write(restricted_words)
    f.close()

if __name__ == '__main__':
  fp1 = "/home/placid/competitions/MiliDoc/server/server/src/raw_data/mil_opendata.csv" 
  fp2 = "/home/placid/competitions/MiliDoc/server/server/src/raw_data/mil_haengjung.csv" 
  fp3 = "/home/placid/competitions/MiliDoc/server/server/src/raw_data/naver_restricted.csv" 
  fp4 = "/home/placid/competitions/MiliDoc/server/server/src/raw_data/jyp_bubble_restricted.csv" 
  fp5 = "/home/placid/competitions/MiliDoc/server/server/src/raw_data/government_words.csv" 
  #check_csv(fp)
  #process_limitWords(fp1, 1)
  #process_limitWords(fp2, 2)
  #process_restrictedWords([fp3, fp4], [3, 4])
  process_limitWords(fp5, 5)
