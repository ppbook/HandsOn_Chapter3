from natto import MeCab
import math
import numpy as np
freq = {}
dfreq = {}
# docs��(��, �P�ꃊ�X�g)�̃y�A���i�[
docs = []
with MeCab('-F%m,%f[0]') as mc:
    with open('neko.txt', 'r') as f:
        for s in f:
            wordlist = []
            # �����ɏo�������P��̏W��
            wordset = set()
            for w in mc.parse(s, as_nodes=True):
                flist = w.feature.split(',')
                if len(flist)>1:
                    word = flist[0]
                    pos = flist[1]
                    if pos == '����':
                        wordset.add(word)
                        wordlist.append(word)
                        if word in freq:
                            freq[word]=freq[word]+1
                        else:
                            freq[word]=1
            docs.append((s,wordlist))
            # wordset���̊e�P��̃J�E���g��1���₷
            for w in wordset: 
                if w in dfreq:
                    dfreq[w]=dfreq[w]+1
                else:
                    dfreq[w]=1


# �P��ID�������\�z
word2id = {}
for s in freq:
    if not s in word2id:
        if freq[s]>=10:
            word2id[s]=len(word2id)

# ������
dim = len(word2id)
docnum = len(docs)


# docs2�Ɂi��, ���x�N�g���j�̃y�A���i�[
docs2 = []
for doc in docs:
    vec = np.zeros(dim)
    wordlist = doc[1]
    for w in wordlist:
        if w in word2id: 
            id = word2id[w] 
            df = dfreq[w]
            # IDF�l�̌v�Z
            idf = math.log(docnum/df)
            # tf-idf�x�N�g�������
            # +idf�� +1�ɕς���ƁABag-of-Words�ɂȂ�
            vec[id]=vec[id]+idf
    # �x�N�g���𒷂�1�ɂȂ�悤�ɐ��K��
    norm = np.linalg.norm(vec, ord=2) 
    if norm>0: 
        vec = vec/norm
    docs2.append((doc[0], vec))

# �{������1�����N�G�����Ƃ��Đݒ�
query = docs2[6]
print('�N�G�����F'+query[0])
print()
queryvec = query[1]




simlist = {}
# �{�����̊e���ƃN�G�����̗ގ��x��simlist�ɓo�^
for id in range(len(docs2)): 
    doc = docs2[id]
    vec = doc[1]
    sim = np.inner(vec, queryvec)
    simlist[id] = sim

# �ގ��x���ɕ����\�[�g
sa = sorted(simlist.items(), key=lambda x: x[1], reverse=True)

# �ގ��x�̑傫�����ɏ��10����\��
for i in range(10):
    ida = sa[i]
    id = ida[0]
    doc = docs2[id]
    print('�ގ��x�F'+str(ida[1]))
    print('�ގ����F'+doc[0])
