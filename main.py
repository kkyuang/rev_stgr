import nltk
from nltk.corpus import wordnet as wn
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag
import random

# NLTK 데이터 다운로드 (최초 한 번만 실행)
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('wordnet')
nltk.download('omw-1.4')

# 품사 태그를 WordNet의 품사 태그로 변환하는 함수
def get_wordnet_pos(treebank_tag):
    if treebank_tag.startswith('J'):
        return wn.ADJ
    elif treebank_tag.startswith('V'):
        return wn.VERB
    elif treebank_tag.startswith('N'):
        return wn.NOUN
    elif treebank_tag.startswith('R'):
        return wn.ADV
    else:
        return None

# 단어의 유의어를 찾는 함수
def get_synonyms(word, pos):
    synonyms = set()
    for synset in wn.synsets(word, pos=pos):
        for lemma in synset.lemmas():
            synonyms.add(lemma.name())
    return synonyms

# 단어의 반의어를 찾는 함수
def get_antonyms(word, pos):
    antonyms = set()
    for synset in wn.synsets(word, pos=pos):
        for lemma in synset.lemmas():
            if synset.pos() == pos:
                for antonym in lemma.antonyms():
                    antonyms.add(antonym.name())
    return antonyms

# 문장의 단어별 품사와 유의어를 찾는 함수
def analyze_sentence(sentence):
    tokens = word_tokenize(sentence)
    tagged = pos_tag(tokens)
    result = {}
    for word, tag in tagged:
        wn_tag = get_wordnet_pos(tag)
        if wn_tag:
            synonyms = get_synonyms(word, wn_tag)
            result[word] = {'POS': tag, 'Synonyms': list(synonyms)}
        else:
            result[word] = {'POS': tag, 'Synonyms': []}
    return result

# 테스트 문장
sentence = ""
sentence = "I will declare a war on python and will not receive any rebuttal"
analysis = analyze_sentence(sentence)

new_sentence = ""
for r in analysis.keys():
    if len(analysis[r]['Synonyms']) > 0:
        new_sentence += analysis[r]['Synonyms'][random.randint(0, len(analysis[r]['Synonyms']) - 1)] + ' '
    else:
        new_sentence += r + ' '

print(analysis)
print(new_sentence)
