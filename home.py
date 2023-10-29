from flask import Flask, request, render_template, redirect, url_for
import instaloader
import re
import time
import subprocess
idx=4


app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        user_name = request.form['name']  # Get the user's name from the form
        print(user_name)
        with open('user.txt','w') as f:
            f.write(user_name+',')
        return render_template('main.html', user_name=user_name)
    return render_template('home.html')

@app.route('/form', methods=['GET', 'POST'])
def instagram_profile():
    if request.method == 'POST':

        username = request.form.get('instagram-username')
        
        # Create an Instaloader instance
        L = instaloader.Instaloader()
        
        try:

            profile = instaloader.Profile.from_username(L.context, username)
        
            user_id = profile.userid
            num_posts = profile.mediacount
            num_followers = profile.followers
            num_followings = profile.followees

            with open('user.txt','a') as f:
                f.write(str(num_posts)+','+str(num_followings)+','+str(num_followers)+',')
            
            captions = []
            hashtags = []
            
            # flags = [0,0,0,0,0,0,0,0]

            for post in profile.get_posts():
                if post.caption is not None:
                    captions.append(post.caption)

                    found_hashtags = re.findall(r'#\w+', post.caption)
                    hashtags.extend(found_hashtags)
            

            with open('cap.txt', 'w') as f:
                for hashtag in hashtags:
                    f.write(hashtag + '\n')

            subprocess.run(["python3", "sub.py"])
            return render_template('comprehensive_puzzle.html')
        
        except Exception as e:
            error_message = f'An error occurred: {e}'
            return render_template('main.html', error=error_message)


    return render_template('main.html')


@app.route('/submit', methods=['POST'])
def submit():
    score = 0

    response1 = request.form.get('response1')
    response2 = request.form.get('response2')
    response3 = request.form.get('response3')

    if response1 == '1':
        score += 2
    elif response1 == '2':
        score += 1

    if response2 == '1':
        score += 2
    elif response2 == '2':
        score += 1

    if response3 == '1':
        score += 2
    elif response3 == '2':
        score += 1

    if score >= 5:
        assessment = "Your decisions indicate strong leadership qualities and a willingness to take calculated risks."
    elif score >= 3:
        assessment = "You demonstrate a balanced approach, considering both safety and initiative."
    else:
        assessment = "You tend to prioritize caution and safety in decision-making."
    with open('user.txt','a') as f:
        f.write(str(score))
    # subprocess.run(["python3", "db2.py"])
    return render_template('psyco.html')


@app.route('/scenario_test', methods=['GET','POST'])
def stest_page():
    return render_template('redirect.html')

l=[0,0,0,0,0,0,0,0,0,0,0,0]
@app.route('/lol', methods=['GET','POST'])
def dummy():
    global idx
    if idx==6:
        aa= request.form.get('E')

        if aa=='1':
            l[0]=1
        else:
            l[1]=1
    if idx==8:
        aa= request.form.get('S')

        if aa=='1':
            l[2]=1
        else:
            l[3]=1
    if idx==10:
        aa= request.form.get('TH')

        if aa=='1':
            l[4]=1
        else:
            l[5]=1
    if idx==12:
        aa= request.form.get('J')

        if aa=='1':
            l[6]=1
        else:
            l[7]=1
    if idx==14:
        aa= request.form.get('L')

        if aa=='1':
            l[8]=1
        else:
            l[9]=1
    if idx==16:
        aa= request.form.get('C&C')

        if aa=='1':
            l[10]=1
        else:
            l[11]=1 

    with open('user.txt','r') as f:
        words = f.readline().strip().split(',')
        while(1):
            if idx==16:
                # for i in range(len(l)):
                #     print(l[i],end=' ')
                break
            if words[idx]=='1' or words[idx+1]=='1':
                if words[idx]=='1':
                    l[idx-4]=1
                else:
                    l[idx-3]=1
                idx=idx+2
                
            else:
                s='p'+str(idx)+'.html'
                idx=idx+2
                # print(s)
                return render_template(s)
    with open('user.txt','r') as f:
        words = f.readline().strip().split(',')
        a = 0
        for i in range(4,16):
            words[i]=l[a]
            a=a+1
    word = ''
    for i in range(len(words)):
        word=word+str(words[i])+','
    # word = word + str(words[len(words)-1])
    with open('user.txt','w') as f:
        f.write(word)
    return render_template('index.html')



@app.route('/process_choice', methods=['POST'])
def process_choice():
    selected_option = request.form.get('choice')
    
    # Perform an action based on the selected option
    if selected_option == 'option1':
        result = "'You are careful with everyone around you. You are responsible reliable and detail-oriented. You take your decisions after thinking carefully about everything. You will not rush into anything. You are highly observant and take notice of everyones body language and behavior.You are meticulous systematic analytical and attentive to details. You may be a forward-thinking and assertive kind of person. You may not take decisions based entirely on emotions. You look for meaning and significance in life. You have a need to care encourage and contribute to your surroundings and relations. You are a natural visionary non-conformist and problem-solver kind of individual.'"
    elif selected_option == 'option2':
        result = "'You are good at understanding people and not leaving their side during their troubled times. You may not judge or conclude opinions about people right away. You will try to know them first. You are a very conscientious person. You understand that people are not perfect and mistakes can happen to anyone.You value integrity and unity in relationships. You are a natural romantic and nurturer. You enjoy connections that encourage expressions and acceptance. You may be one of those extremely helpful individuals who give more importance to relationships than other aspects of life. You are likely to make decisions based on emotions. You want to be understood and appreciated.'"
    elif selected_option == 'option3':
        result = "'You tend to possess exceptional confidence and leadership skills. You are able to recognize problems and the most apt solutions. You may be skilled at turning around situations and opportunities to your advantage. Under negative circumstances you can also be pretentious snobbish and arrogant.You love living in the present. You enjoy every moment to the fullest. You love spontaneity in your work. You love creating new ideas. You have a strong independent streak. You may highly ambitious. You may like to be the center of attention. You may be highly competitive and may have learned to keep a good grip on your emotions.'"
    elif selected_option == 'option4':
        result = "'You may trust others easily. You may be sensitive and emotional. You want to be understood and appreciated. You may always try to be a better person. You prefer to lead by a head over heart approach. You are easy to talk to and a good listener. However you become uneasy if you feel controlled too much by your emotions.You like to work on yourself and your goals to achieve success. You love to learn new things and concepts. You abide by high morals while working also. In your adult life also you may find yourself on a quest to discover yourself. You may seek outer validation a lot to feel good about yourself. You may be needed to be reminded about your uniqueness and abilities.'"
    else:
        result = "'Invalid option selected.'"

    with open('user.txt','a') as f:
        f.write(result)
    subprocess.run(["python3", "db2.py"])
    subprocess.run(["python3","final.py"])
    # time.sleep(3)
    return render_template('thankyou.html')




    

    # Your MBTI test logic here, using the 'questions' dictionary

    # Determine the MBTI result based on the responses
    # mbti_result = ''

    # Example: Combine responses for each dimension
    # for dimension, response in questions.items():
    #     if response == 'A':
    #         mbti_result += dimension+' '
    #     elif response == 'D':
    #         mbti_result += dimension+' '

    # Render the result
    # return f"Your MBTI Personality Type: {mbti_result}"

if __name__ == '__main__':
    app.run(debug=True)

