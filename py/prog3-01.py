# �_�E�����[�h�A�t�@�C���������ݗp���W���[���̃C���|�[�g
import requests, io

# �K�v��URL�̃��X�g����������
urllist = [
'000148/files/789_ruby_5639.zip',#��y�͔L�ł���
'001779/files/57228_ruby_58697.zip'#���l��\�ʑ�
] 

# URL�̃��X�g�����ƂɁA�t�@�C�����_�E�����[�h����
for i in range(len(urllist)):
    url = 'https://www.aozora.gr.jp/cards/'+urllist[i]
    fn = 'text-'+str(i)
    res = requests.get(url, stream=True) 
    with open(fn+'.zip', 'wb') as handle:
        for chunk in res.iter_content(chunk_size=512):
          if chunk:
              handle.write(chunk)

# �_�E�����[�h�����t�@�C�����𓀂���
!unzip '*.zip'
