# LdaMallet�̃C���|�[�g
from gensim.models.wrappers import LdaMallet

# LDA�̊w�K
model = LdaMallet('Mallet/bin/mallet',
    corpus=corpus, num_topics=100, 
    id2word=dictionary, alpha=3.0, iterations=1000) 

# ���ʂ̕\��
model.print_topics(100, num_words=5)
