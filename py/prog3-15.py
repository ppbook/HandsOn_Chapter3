from natto import MeCab
import math
import numpy as np

# gensim���C���|�[�g
import gensim
# �O�����ɕK�v�ȃ��W���[�����Agensim����C���|�[�g
from gensim import corpora, models, similarities

docs=[]
stopwords ={'����','����','��','��','����','�悤','��','��','����','����'}

with MeCab('-F%m,%f[0]') as mc:
    with open('neko.txt', 'r') as f:
        for s in f:
            # �e����P�ꃊ�X�g�ɕϊ����A���X�gdocs�ɉ�����
            wordlist = []
            for w in mc.parse(s, as_nodes=True): 
                flist = w.feature.split(',');
                if len(flist)>1: 
                    word = flist[0] 
                    pos = flist[1]
                    if pos == '����':
                        if not word in stopwords:
                            wordlist.append(word)
            docs.append(wordlist)

# �������\�z
dictionary = corpora.Dictionary(docs) 
#dictionary.filter_extremes(no_below=2)
# �\�z���ꂽ�������g���A�P�ꃊ�X�g��Bag-of-Words�ɕϊ�
corpus = [dictionary.doc2bow(doc) for doc in docs] 
