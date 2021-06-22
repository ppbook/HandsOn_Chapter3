from natto import MeCab
freq = {}

# �\�w�`�ƕi���𒊏o
with MeCab('-F%m,%f[0]') as mc: 
    with open('neko.txt', 'r') as f:
        for s in f:
            for w in mc.parse(s, as_nodes=True): 
                # �\�w�`�ƕi�������X�g�Ɋi�[
                flist = w.feature.split(',')
                if len(flist)>1:
                    word = flist[0]
                    pos = flist[1]
                    if pos == '����': 
                        # �P��̃J�E���g��1���₷
                        if word in freq: 
                            freq[word]=freq[word]+1
                        else:
                            freq[word]=1
 
# ���ʂ�p�x���ɕ\��
sa = sorted(freq.items(), key=lambda x: x[1], reverse=True)
sa[:10]
