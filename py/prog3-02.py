import requests, io

# Shift_JIS�Ńt�@�C�����J���A�ŏ���30�s��\��
with open('wagahaiwa_nekodearu.txt', 'r', encoding='Shift_JIS') as f:
    lines = f.readlines()
    for s in lines[0:30]:
        print(s, end='')
