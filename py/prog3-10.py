from natto import MeCab
freq = {}
# �\�w�`�A�i���ו���(1)�𒊏o
with MeCab('-F%m,%f[1]') as mc: 
    with open('neko.txt', 'r') as f:
        for s in f:
            for w in mc.parse(s, as_nodes=True):
                # �\�w�`�A�i���ו���(1)�����X�g�Ɋi�[
                flist = w.feature.split(',')
                if len(flist)>1:
                    word = flist[0]
                    subpos = flist[1]
                    # �i���ו���(1)���ŗL�����Ȃ�A
                    # �p�x���J�E���g
                    if subpos == '�ŗL����': 
                        word = flist[0]
                        if word in freq:
                            freq[word]=freq[word]+1
                        else:
                            freq[word]=1

# ���ʂ�p�x���ɕ\��
sa = sorted(freq.items(), key=lambda x: x[1], reverse=True)
sa[:10]
