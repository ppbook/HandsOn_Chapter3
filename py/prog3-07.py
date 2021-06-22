from natto import MeCab	
# 表層形、品詞、原形を抽出してfeatureに格納
with MeCab('-F%m,%f[0],%f[6]') as mc:
    text = '昨日はとても暑かったと思います。'
    for w in mc.parse(text, as_nodes=True):
        print(w.feature) 
