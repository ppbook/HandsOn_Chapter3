# word2vec�œǂݍ��񂾃��f�����A2������NumPy�z��ɕϊ�
# word_index�́A�P����L�[�Ƃ��ăx�N�g����Ԃ��A�z�z��
import numpy as np
from tensorflow import keras

word_index={}
for key in model.vocab:
    word_index[key]=len(word_index)

num_words = len(word_index)+2 # ��b�̐�
w2v_size = 100 # �x�N�g���̎�����

word_matrix = np.zeros((num_words, 100), dtype='float32')
# ID=0��[PAD]�AID=1��[UNK]�ɑΉ��B�ǂ�����[���x�N�g��
word_matrix[0] = np.zeros((100), dtype='float32')
word_matrix[1] = np.zeros((100), dtype='float32')
for key in word_index:
    # �ǂݍ��񂾎����̍ŏ��̒P�ꂪ�AID=2
    word_matrix[2+word_index[key]]=model[key]
# �e�L�X�g�W���̓ǂݍ���
docs2 = []
for s in docs: 
    sl = s.split()
    sl2 = []
    for w in sl:
        if w in word_index:
            sl2.append(2+word_index[w]) 
        else:
            sl2.append(1) # OOV�P��
    docs2.append(sl2)

# np.array�ōs��i2�����z��j�𐶐����邽�߂ɁA
# �e���i�P�ꃊ�X�g�j�̒��������낦��
# �f�t�H���g�ł́A���̍Ō��0���ǉ������
docs3 = keras.preprocessing.sequence.pad_sequences(\
    docs2, value=0, padding='post', maxlen=100)
docs4 = np.array(docs3) 
labels2 = np.array(labels)

from sklearn.model_selection import train_test_split

train_x, test_x, train_y, test_y, train_i, test_i = \
    train_test_split(docs4, labels2, inds, test_size=0.2) 
