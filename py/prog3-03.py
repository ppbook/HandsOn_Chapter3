import io
# ���K�\���p���W���[�����C���|�[�g
import re
#(���̃t�@�C����,������̃t�@�C����)�̃��X�g�B
textlist = [
('wagahaiwa_nekodearu','neko'),
('kaijin_nijumenso','kaijin'),
]
for i in range(len(textlist)):
    text = textlist[i][0]
    text2 = textlist[i][1]
  
    # �e�O�����̌��ʂ��ꎞ�ۑ����郊�X�g
    tmplist = []
    tmplist2 = []
    tmplist3 = []

    # �t�@�C���`���̃��^�f�[�^�폜
    # n�͂���܂łɓǂ񂾋�؂�s�̐�
    n=0
    with open(text+'.txt', 'r', encoding='Shift_JIS') as f:
        for s in f:
            if n>=2: 
                tmplist.append(s)
            if s.find('--------')>=0:
                n=n+1

    # �t�@�C�������̃��^�f�[�^�폜
    # n�͘A�����ēǂ񂾋�s�̐�
    n=0
    for s in tmplist:
        # ���s�R�[�h��1������
        if len(s)==1:
            n=n+1
            if n>=3:
              break
        else:
            n=0
        tmplist2.append(s)
    
    # �{�����̒��߂��폜
    for s in tmplist2:
        s2 = re.sub(r'�s.*?�t', '', s) 
        s3 = re.sub(r'�m��.*?�n', '', s2)
        s4 = re.sub(r'�b','',s3)
        tmplist3.append(s4)

    # �e�s���A���ɕ������AUnicode�Ńt�@�C���ɏo��
    with open(text2+'.txt', 'w', encoding='utf-8') as f:
        for line in tmplist3:
            sentlist = line.split('�B')
            for i in range(len(sentlist)):
                s = sentlist[i] 
                s = re.sub(r'\n','',s)
                if len(s)>0:
                    f.write(s)
                    if i<len(sentlist)-1:
                        f.write('�B')
                    f.write('\n')
