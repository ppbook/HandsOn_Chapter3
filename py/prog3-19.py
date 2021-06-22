from natto import MeCab
corpus = []
labels = []
with MeCab('-Owakati') as mc: 
    with open('neko.txt', 'r') as f:
        for s in f:
            s2 = mc.parse(s) # �P����X�y�[�X�ŋ�؂�@
            corpus.append(s2.split())

# gensim����Aword2vec�p���W���[�����C���|�[�g
from gensim.models import word2vec

# corpus�Ɋi�[���ꂽ�f�[�^����A���U�\���x�N�g�����w�K
model = word2vec.Word2Vec(sentences=corpus, sg=1, min_count=3,window=5)  
