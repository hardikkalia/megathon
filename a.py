import string
import sqlite3

class DBclass:
    def __init__(self, path):
        self.path = path
        
    def execute(self, query):
        db = sqlite3.connect(self.path)
        cur = db.cursor()
        cur.execute(query)
        result = [i[0] for i in cur.description], cur.fetchall()
        db.close()
        return result
    

conn = sqlite3.connect('players.db')
cursor = conn.cursor()



with open('cap.txt', 'r') as f:
    stopwords = f.read().splitlines()

lis=[]
for i in stopwords:
    for x in range(len(i)):
        if i[x]=='#':
            lis.append("("+'''"'''+i[x:].split(',')[0].rstrip()+'''"'''+","+'''"'''+i[x:].split(',')[1].rstrip()+'''"'''+")"+",")

with open('output.txt','w') as f:
    for i in range(len(lis)):
        f.write(lis[i])