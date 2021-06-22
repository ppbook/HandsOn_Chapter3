from natto import MeCab
# scikitlearn����Atf-idf�x�N�g���p���W���[�����C���|�[�g
from sklearn.feature_extraction.text import TfidfVectorizer

docs = []
labels = []
inds = []
with MeCab('-Owakati') as mc:
    with open('neko.txt', 'r') as f:
        for s in f:
            s2 = mc.parse(s)#�P����X�y�[�X�ŋ�؂�
            docs.append(s2)
            labels.append(1) 
            inds.append(len(inds)) 
    with open('kaijin.txt', 'r') as f:
        for s in f:
            s2 = mc.parse(s)#�P����X�y�[�X�ŋ�؂�
            docs.append(s2)
            labels.append(0)
            inds.append(len(inds))

vectorizer = TfidfVectorizer(use_idf=True) 
vecs = vectorizer.fit_transform(docs)

docs2 = vecs.toarray()
