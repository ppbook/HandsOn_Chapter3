from natto import MeCab	
# �\�w�`�A�i���A���`�𒊏o����feature�Ɋi�[
with MeCab('-F%m,%f[0],%f[6]') as mc:
    text = '����͂ƂĂ����������Ǝv���܂��B'
    for w in mc.parse(text, as_nodes=True):
        print(w.feature) 
