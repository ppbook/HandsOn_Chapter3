from google.colab import drive 
drive.mount('/content/drive')
%cd /content/drive/MyDrive

# word2vec�̃x�N�g���ǂݍ��݂̂��߂̃��W���[�����C���|�[�g
from gensim.models import Word2Vec
from gensim.models import KeyedVectors

# �w�K�ς݃x�N�g����ǂݍ���
model = KeyedVectors.load_word2vec_format(\
    'jawiki.word_vectors.100d.txt', binary=False) 
