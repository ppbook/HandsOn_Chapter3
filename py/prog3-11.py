from natto import MeCab
freq = {}
# ���̒P����󔒂ŋ�؂��ďo�͂���I�v�V����
with MeCab('-Owakati') as mc: 
    with open('neko.txt', 'r') as f:
        for s in f:
            wordlist = mc.parse(s).split()
            for i in range(len(wordlist)-1):
                # �ׂ荇��2�P���A��
                w1 = wordlist[i]
                w2 = wordlist[i+1]
                bigram = w1+'-'+w2
                if bigram in freq: 
                    freq[bigram]=freq[bigram]+1
                else:
                    freq[bigram]=1

# ���ʂ�p�x���ɕ\��
sa = sorted(freq.items(), key=lambda x: x[1], reverse=True)
for a in sa:
    if a[1]>=100:
        print(a[0],'(�p�x=',a[1],')')
