import string

with open('new.txt', 'r') as f:
    stopwords = f.read().splitlines()

lis=[]
for i in stopwords:
    for x in range(len(i)):
        if i[x]=='#':
            lis.append("("+'''"'''+i[x:].split(',')[0].rstrip()+'''"'''+","+'''"'''+i[x:].split(',')[1].rstrip()+'''"'''+")"+",")

with open('output.txt','w') as f:
    for i in range(len(lis)):
        f.write(lis[i])