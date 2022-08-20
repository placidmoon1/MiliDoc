raw_text = """
 정부가 K2 전차, K9 자주포, FA_50 경공격기 등 20조원대 국산 무기 수출 본 계약을 앞두고 있는 폴란드 등 국산 무기 수입을 추진 중인 주요 8개국에서 방산 중점공관 운영을 추진한다.

 박진 외교부 장관은 18일 국회 외교통일위원회 전체회의에서 서면으로 제출한 업무보고에서 방산 세일즈 외교를 국가별 맞춤형으로 강화하겠다며 이같이 밝혔다.

 박 장관은 이날 언급한 방산 중점공관 운영 대상국은 폴란드를 비롯해 사우디 아라비아‧호주‧노르웨이‧미국‧말레이시아‧인도네시아 등이다.

 정부는 지난달 말 주폴란드 한국대사관에 국산 무기체계 수출입 계약 체결 관련 업무를 맡는 방산 전담 무관 파견 방침을 밝힌 바 있다.

 박 장관의 중점공관 운영 방침은 이를 확대해 상시 운영 체제로 바꾸겠다는 뜻으로 풀이된다.

 박 장관은 이어 윤석열 대통령이 지난 15일 북한에 제안한 ‘담대한 구상’ 이행을 위해 “한미 공조를 바탕으로 비핵화 협상을 재가동하고, 담대한 구상 이행과 관련해 국제사회와 긴밀 협력하겠다”고 말했다.

 윤 대통령은 지난 15일 광복절 경축사를 통해 북한이 진정성 있게 비핵화 협상에 임한다는 전제 아래 ‘북한에 대한 대규모 식량 공급 프로그램’, ‘발전과 송배전 인프라 지원’, ‘국제 교역을 위한 항만과 공항의 현대화 프로젝트’, ‘농업 생산성 제고를 위한 기술 지원 프로그램’, ‘병원과 의료 인프라의 현대화 지원’, ‘국제투자 및 금융 지원 프로그램’ 등의 내용을 담은 ‘담대한 구상’을 천명했다.

 그 중 대규모 식량 공급과 관련 ‘한반도 자원식량교환프로그램’(R-FEP)이 가동되려면 유엔 안보리 15개 이사국으로 구성된 대북제재위원회의 제재 면제 결정이 필수적이어서 미국 등 국제사회 협력은 불가피한 상황이다.

 박 장관은 “억제, 단념, 대화의 총체적, 균형적 접근법에 따라 북한이 비핵화의 길로 돌아올 수밖에 없는 환경 조성을 추진하겠다”며 “원칙 있는 대북 관여를 통해 국제사회와 함께 북한 주민의 인권과 인도적 상황 개선을 지속해서 모색하겠다”고 설명했다.

 그러면서도 “7차 핵실험 등 북한의 추가 중대 도발 시 미국과 일본 등 우방국과의 공조하에 신규 안보리 제재 결의, 독자 제재도 추진하겠다”고 경고했다.

 박 장관은 “내년 (한미)동맹 70주년을 맞아 한미 글로벌 포괄적 전략동맹 협력의 폭과 범위를 본격 심화하겠다”고 강조했다.

 아울러 분야별 한미 고위급 전략협의 추진 계획으로 외교 장·차관급 전략대화, 한미 고위급 확장억제전략협의체, 고위급 경제협의회, 경제안보대화 개최 등을 구체적으로 언급했다.

 외교부는 '글로벌 중추국가' 역할을 강화하기 위해 △정상·고위급 다자회의 참여를 확대하고, △국제기구 활동 강화 및 가치·규범 기반 다자·소다자협의체 참여를 계속 추진하겠다고 보고했다.

 외교부는 개발·공공외교 분야에선 △공적개발원조(ODA) 규모 확대 △대외 전략과 연계한 ODA 정책 추진 △글로벌 위기 대응 인도적 지원 강화 △미국·유럽연합(EU) 등 주요 공여국과의 협력 확대 등을 추진할 계획이라고 설명했다.

 박 장관은 이어 중국과의 새로운 외교 방향으로 “고위급 소통과 실질 협력 확대 등을 통해 한중 간 상생 발전을 도모하겠다”며 “(한국)국가안보실장-(중국)정치국원 전략대화, 올해 중국 왕이(王毅) 중국 외교부장 방한 추진, 차관 전략 대화 등을 가동하겠다”고 적극적 의지를 피력했다.

 박 장관은 윤석열 정부의 새로운 인도‧태평양전략에 대해서는 “기존 지역 전략들을 거시적 틀에서 관리하겠다”며며 아세안, 태평양 도서국, 인도 등과의 전략적 관계를 새롭게 수립하겠다는 구상도 내놨다.

 이와 함께 “인도·태평양 경제 프레임워크(IPEF) 협상에 주도적으로 참여하겠다”며 “다음 달 8일부터 이틀간 미국 로스앤젤레스(LA)에서 진행되는 IPEF 장관 회의 계기 각료선언문 발표로 IPEF 내 4개 분아별 본격 협상이 개시될 것”이라고 말했다.

 출처 : 국방신문(http://www.gukbangnews.com)
 """

from konlpy.tag import Mecab
tokenizer = Mecab()

raw_text_morphs = tokenizer.morphs(raw_text)
#print(raw_text_morphs)