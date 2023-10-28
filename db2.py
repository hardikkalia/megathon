import sqlite3

conn = sqlite3.connect("userdatabase.db")
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS mytable (
                    name TEXT,
                    flag1 int,
                    flag2 int,
                    flag3 int,
                    flag4 int,
                    flag5 int,
                    flag6 int,
                    flag7 int,
                    flag8 int,
                    flag9 int,
                    flag10 int,
                    flag11 int,
                    flag12 int,
                    testscore int,
                    assess TEXT
                )''')


conn.commit()
conn.close()