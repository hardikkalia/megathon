from flask import Flask, request, render_template, redirect, url_for
import instaloader
import re
import subprocess

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

    return render_template('result.html', score=score, assessment=assessment)


@app.route('/scenario_test', methods=['GET','POST'])
def stest_page():
    return render_template('redirect.html')

if __name__ == '__main__':
    app.run(debug=True,port=8000)
