import pandas as pd
from collections import Counter

with open('br-sem-acentos.txt', 'r') as arquivo:
    r = arquivo.read()
    conteudo = str(r).lower().split('\n')
    

df = pd.DataFrame()
for i in 'abcdefghijklmnopqrstuvwxyz':
    df[i] = []

for x in range(124000, len(conteudo)):
    i = conteudo[x]
    a = Counter(list(i))
    df.loc[i] = a
    if x % 1000 == 0:
        print(x)
        df = df.fillna(0)
        df = df.replace(0, -1)
        df = df.replace([i for i in range(20)], 1)
        df.to_csv('frequencia2.csv')
# print(df)