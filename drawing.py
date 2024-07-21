import nltk
from nltk import word_tokenize, pos_tag
from nltk.chunk import RegexpParser

# NLTK 데이터 다운로드 (최초 한 번만 실행)
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

# 문장 토큰화 및 품사 태깅
sentence = "I will hold a war on python and non invite any rebutter "
tokens = word_tokenize(sentence)
tagged = pos_tag(tokens)

# 간단한 문법 정의
grammar = """
  NP: {<DT>?<JJ>*<NN.*>+}   # 명사구
  VP: {<VB.*><NP|PP|CLAUSE>+$}  # 동사구
  PP: {<IN><NP>}             # 전치사구
  CLAUSE: {<NP><VP>}         # 절
"""

# 문법을 바탕으로 파서 생성
parser = RegexpParser(grammar)

# 문장 파싱
tree = parser.parse(tagged)

# 트리 시각화
tree.draw()
