import sqlite3

conn = sqlite3.connect("mydatabase.db")
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS mytable (
                    keyword TEXT ,
                    value VARCHAR
                )''')

lis = [("#love","N"),("#instagood","E"),("#fashion","N"),("#photooftheday","E"),("#photography","E"),("#art","E"),("#beautiful","N"),("#nature","N"),("#picoftheday","N"),("#happy","E"),("#follow","E"),("#travel","I"),("#cute","F"),("#style","S"),("#instadaily","E"),("#tbt","E"),("#followme","E"),("#summer"," I"),("#beauty","F"),("#fitness","J"),("#like4like","N"),("#food","N"),("#instalike","N"),("#photo","N"),("#selfie","N"),("#friends","N"),("#music","T"),("#smile","I"),("#family","I"),("#fun","N"),("#girl","N"),("#likeforlikes","N"),("#motivation","N"),("#fitness","J"),("#gym","J"),("#workout","J"),("#health","J"),("#fitnessmotivation","J"),("#bodybuilding","J"),("#healthy","J"),("#yoga","J"),("#running","J"),("#body","J"),("#run","J"),("#fitnessmodel","J"),("#gymmotivation","J"),("#cardio","J"),("#fitnessaddict","J"),("#fitnessjourney","J"),("#getfit","J"),("#fitmom","J"),("#workoutmotivation","J"),("#gymrat","J"),("#fitnesslifestyle","J"),("#yogainspiration","J"),("#sweat","J"),("#strengthtraining","J"),("#gymgirl","J"),("#art","N"),("#photography","N"),("#artist","N"),("#drawing","N"),("#artwork","N"),("#digitalart","N"),("#artistsoninstagram","N"),("#draw","N"),("#instaart","N"),("#artoftheday","N"),("#contemporaryart","N"),("#paint","N"),("#abstractart","N"),("#artgallery","N"),("#artistic","N"),("#artofinstagram","N"),("#artcollector","N"),("#modernart","N"),("#tattooart","N"),("#urbanart","N"),("#picsart","N"),("#artists","N"),("#artlover","N"),("#artdaily","N"),("#artjournal","N")]

for i in lis:
    cursor.execute("INSERT INTO mytable (keyword, value) VALUES (?, ?)", i)

conn.commit()
conn.close()