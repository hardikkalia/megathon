import sqlite3

conn = sqlite3.connect("mydatabase.db")
cursor = conn.cursor()

with open('user.txt','r') as f:
    word = f.readline().strip().split(',')

word = word[4:16]
string = ''
if(word[0]=='1'):
    string+='E'
    string+=','
if(word[1]=='1'):
    string+='I'
    string+=','
if(word[2]=='1'):
    string+='S'
    string+=','

if(word[3]=='1'):
    string+='N'
    string+=','

if(word[4]=='1'):
    string+='TH'
    string+=','

if(word[5]=='1'):
    string+='F'
    string+=','

if(word[6]=='1'):
    string+='J'
    string+=','

if(word[7]=='1'):
    string+='P'
    string+=','

if(word[8]=='1'):
    string+='L'
    string+=','

if(word[9]=='1'):
    string+='TE'
    string+=','

if(word[10]=='1'):
    string+='C&C'
    string+=','

if(word[11]=='1'):
    string+='AX'
    string+=','

string= string[0:len(string)-1]

with open('cap.txt','r') as f:
    l = f.readlines()
    for i in range(len(l)):
        word2 = l[i]
        cursor.execute("SELECT keyword,value FROM mytable WHERE keyword = ?",(word2,))
        result = cursor.fetchone()
        if result is None:
            cursor.execute("INSERT INTO mytable (keyword,value) VALUES (?,?)",(word2,string))
            conn.commit()
        # else:
        #     cursor.execute("UPDATE mytable SET value = ? WHERE keyword = ?",(string,word2))

conn.close()



