from natto import MeCab
freq = {}

# �\�w�`�A�i���A���`�𒊏o
with MeCab('-F%m,%f[0],%f[6]') as mc: 
    with open('neko.txt', 'r') as f:
        for s in f:
            for w in mc.parse(s, as_nodes=True):
                # �\�w�`�A�i���A���`�����X�g�Ɋi�[
                flist = w.feature.split(',')
                if len(flist)>2:
                    pos = flist[1]
                    root = flist[2]
                    # �i����������������A���`�̕p�x��1���₷
                    if pos == '����': 
                        if root in freq:
                            freq[root]=freq[root]+1
                        else:
                            freq[root]=1

# ���ʂ�p�x���ɕ\��
sa = sorted(freq.items(), key=lambda x: x[1], reverse=True)
sa[:10] 
