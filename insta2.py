from flask import Flask, request, render_template, redirect, url_for
import instaloader
import re
import subprocess

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
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
            return redirect(url_for('redirect_page'))
        
        except Exception as e:
            error_message = f'An error occurred: {e}'
            return render_template('main.html', error=error_message)


    return render_template('main.html')

@app.route('/redirect', methods=['GET'])
def redirect_page():
    return render_template('redirect.html')

if __name__ == '__main__':
    app.run(debug=True,port=8000)
