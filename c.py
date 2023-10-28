import string
from flask import Flask, render_template, request
import sqlite3
import stanza
import datetime
import fasttext 
import numpy as np

model = fasttext.load_model('/Users/udaybindal/Downloads/cc.en.300.bin')
print(model.get_dimension())

app = Flask(__name__)
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
query = "SELECT Lastname FROM playertables "
cursor.execute(query)
results = cursor.fetchall()
newlist =[]
for row in results:
    col1 = row[0]
    newlist.append(col1)
conn.close()
print(newlist)

with open('stopwords.txt', 'r') as f:
    stopwords = f.read().splitlines()
    
rules = {
    'greet': {
        'keywords': ['#love','#instagood','#fashion ','#photooftheday','#photography ','#art','#beautiful','#nature','#picoftheday','#happy','#follow','#travel ','#cute','#style ','#instadaily ','#tbt ','#followme ','#summer I','#beauty','#fitness ','#like4like','#food','#instalike ','#photo ','#selfie ','#friends ','#music','#smile','#family ','#fun ','#girl ','#likeforlikes','#motivation','#fitness ','#gym ','#workout ','#health ','#fitnessmotivation ','#bodybuilding ','#healthy ','#yoga ','#running ','#body ','#run ','#fitnessmodel ','#gymmotivation ','#cardio ','#fitnessaddict ','#fitnessjourney ','#getfit ','#fitmom ','#workoutmotivation ','#gymrat ','#fitnesslifestyle ','#yogainspiration ','#sweat ','#strengthtraining ','#gymgirl ','#art ','#photography ','#artist ','#drawing ','#artwork ','#digitalart ','#artistsoninstagram ','#draw ','#instaart ','#artoftheday ','#contemporaryart ','#paint ','#abstractart ','#artgallery ','#artistic ','#artofinstagram ','#artcollector ','#modernart ','#tattooart ','#urbanart ','#picsart ','#artists ','#artlover ','#artdaily ','#artjournal '],
        'response': 'Hi there! How can I help you today?'
    }
}
nlp = stanza.Pipeline(lang='en', processors='tokenize,pos')
similarwords=[]
def process_input(input_text, db):
    k = 0

    
    maxsim =0
    wordafterchecking =""
    input_text = input_text.lower()
    input_text = input_text.translate(str.maketrans('', '', string.punctuation))
   
    words = input_text.split()
    words = [wording for wording in words if wording not in stopwords]
  
    for i in range(len(words)):
        wordafterchecking = wordafterchecking + " " + words[i]

    doc = nlp(wordafterchecking)
    
    user_input_tokens = [(word.text, word.upos) for sent in doc.sentences for word in sent.words]
    max_match =0
    best_keyword = None
    
    # for rule in rules.values():
    #     for keyword in rule['keywords']:
    #         doc2 = nlp(keyword)
    #         keyword_tokens = [(word.text, word.upos) for sent in doc2.sentences for word in sent.words]
    #         # keyword_pos_tags = [(token, "") for token in keyword_tokens]
    #         print(keyword_tokens)
    #         # print(keyword_pos_tags)
    #         # print(len(keyword_tokens))
    #         print(user_input_tokens)
            
            # print(len(user_input_tokens))
            # for t in user_input_tokens:
            #     for k in keyword
            # if all(tag in user_input_tokens for tag in keyword_pos_tags):
            #     if best_match is None or len(keyword_pos_tags) > len(best_match):
            #         best_match = keyword_pos_tags
            #         best_keyword = keyword
            # matches = sum(1 for token in user_input_tokens if token[1] in [kw_token[1] for kw_token in keyword_tokens])
            # print("matches = ",matches)
            # exists=0
            # for i in user_input_tokens[0]:
            #     if keyword == i:
            #         exists = 1
            # if exists == 0:
            #     matches = 0
                
            # if matches > max_match:
            #     max_match = matches
            #     best_keyword = keyword
            # print(best_keyword)
            # print("max = ",max_match)
            
            # if len(keyword_tokens) != len(user_input_tokens):
            #     continue
            
            # matches = all(token[1] == keyword_tokens[i] for i, token in enumerate(user_input_tokens))
   
    for i in range(len(words)):
        input_word = words[i]
        input_vector = model.get_word_vector(input_word)
      
        for rule in rules.values():
            for keyword in rule['keywords']:
              
                keyword_vector = model.get_word_vector(keyword)
                similarity = np.dot(input_vector, keyword_vector) / (np.linalg.norm(input_vector) * np.linalg.norm(keyword_vector))
                if similarity >= maxsim:
                    maxsim = similarity
                    similarwords = [keyword,maxsim]
                    print(similarwords[0],similarwords[1])
    
    for rule in rules.values():
        for keyword in rule['keywords']:
               
                if keyword == similarwords[0]:
                    
                    if rule.get('query'):
                        

                        for i in range(len(newlist)):
                            for j in range(len(words)):
                                if words[j] == newlist[i]:
                                    k = i
                                    break
                                
                        columns, result = db.execute(rule['query'].format(name=newlist[k]))
                        if len(result) == 0:
                            return "I'm sorry, I couldn't find any players with that name."
                        output = result
                        if rule['response']:
                            response = rule['response'].format(name=newlist[k])
                            return response + '\n' + '\n'.join(['\t'.join(map(str, row)) for row in output])
                        else:
                            return '\n'.join(['\t'.join(map(str, row)) for row in output])
                    else:
                        return rule['response']
    return "I'm sorry, I don't understand. Type 'help' for a list of available commands."
    
    nothing = {
        'here':{
            'query' :  "SELECT Lastname FROM playertables" 
        }        
    }
    x = nothing['here']
    columns,y = db.execute(x['query'])
    print(y)
    
    z = wordafterchecking.split()[-1]
    print(z.lower())
    # print(y[0][0],y[1],y[2])
    for i in range(len(y)):
        if z.lower() == y[i][0]:
            rule = rules['player_info']
            columns,result = db.execute(rule['query'].format(name=wordafterchecking.split()[-1]))
            output = result
            if rule['response']:
                    response = rule['response'].format(name=wordafterchecking.split()[-1])
                    return response + '\n' + '\n'.join(['\t'.join(map(str, row)) for row in output])
    # print(result)
    return "I'm sorry, I don't understand. Type 'help' for a list of available commands."

@app.route('/')
def index():
    return render_template('chat.html')

@app.route('/process_input', methods=['POST'])
def process_input_route():
    
    nlp = stanza.Pipeline(lang='en', processors='tokenize,mwt,pos')
    db = DBclass('players.db')
    current_time = datetime.datetime.now().time()
    start_time = datetime.time(22, 0)  # 10 PM
    end_time = datetime.time(3, 0)  # 3 AM

    if start_time <= current_time or current_time <= end_time:
        bot_response = "Go back and study # YOU ARE IN IIIT"
        return bot_response
    
   

    user_input = request.form['input_text']
    bot_response = process_input(user_input, db)
    
    return bot_response

if __name__ == '__main__':
    app.run(port= 8000)