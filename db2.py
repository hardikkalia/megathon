import sqlite3

conn = sqlite3.connect("userdatabase.db")
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS mytable (
                    name TEXT,
                    insta_post INT,
                    insta_following INT,
                    insta_followers INT,
                    flag1 INT,
                    flag2 INT,
                    flag3 INT,
                    flag4 INT,
                    flag5 INT,
                    flag6 INT,
                    flag7 INT,
                    flag8 INT,
                    flag9 INT,
                    flag10 INT,
                    flag11 INT,
                    flag12 INT,
                    testscore INT,
                    summary VARCHAR
                )''')

with open('user.txt', 'r') as f:
    file_contents = f.read().strip()
    words = file_contents.split(',')
    print(len(words))
    if len(words) == 18:
        cursor.execute("INSERT INTO mytable (name, insta_post, insta_following, insta_followers, flag1, flag2, flag3, flag4, flag5, flag6, flag7, flag8, flag9, flag10, flag11, flag12, testscore, summary) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", words)
        conn.commit()
    
conn.close()
