import sqlite3

# Open a connection to the SQLite database
conn = sqlite3.connect('mydatabase.db')
cursor = conn.cursor()

lis = ['E','I','S','N','TH','F','J','P','L','TE','C&C','AX']
flags = len(lis)*[0]
with open('cap.txt', 'r') as file:
    file_content = file.read()
words = file_content.split()
keyword_values = {}

for word in words:
    cursor.execute("SELECT keyword, value FROM mytable WHERE keyword = ?", (word,))
    results = cursor.fetchall()
    for result in results:
        if result:
            keyword, value = result
            keyword_values[keyword] = value
            for a in value.split(','):
                for i in range(len(lis)):
        
                    if lis[i]==a:
                        flags[i]=1



conn.close()

    
    # print(f"Keyword: {keyword}, Value: {value}")
print(flags)
with open('user.txt','a') as f:
    for j in range (len(flags)):
        f.write(str(flags[j]))
        f.write(',')
