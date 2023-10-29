from flask import Flask, request, render_template, redirect, url_for
import instaloader
import re
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
    word = ' '
    for i in range(len(words)-1):
        word=word+str(words[i])+','
    word = word + str(words[len(words)-1])
    with open('user.txt','w') as f:
        f.write(word)
    subprocess.run(["python3", "db2.py"])
    return render_template('redirect.html')



    

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

