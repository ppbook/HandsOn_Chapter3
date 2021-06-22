# numpy, tensorflow, keras���C���|�[�g
import numpy as np
import tensorflow as tf
from tensorflow import keras
# ��̃j���[�����l�b�g���[�N�𐶐�
mycnn = keras.Sequential()
# ���ߍ��ݑw��ǉ�
mycnn.add(keras.layers.Embedding(num_words, w2v_size, weights=[word_matrix], input_length=100, \
    mask_zero=True, trainable=False)) 
# ��ݍ��ݑw��ǉ�
mycnn.add(keras.layers.Conv1D(100,1, activation=tf.nn.relu))
# �v�[�����O�w��ǉ�
mycnn.add(keras.layers.GlobalMaxPooling1D())
# �S�����w��ǉ�
mycnn.add(keras.layers.Dense(1, activation=tf.nn.sigmoid)) 
# �w�K�̂��߂̃��f����ݒ�
mycnn.compile(optimizer=tf.optimizers.Adam(),
    loss='binary_crossentropy', metrics=['accuracy'])
