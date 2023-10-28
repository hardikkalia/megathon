from flask import Flask, request, render_template, redirect, url_for
import instaloader

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def instagram_profile():
    if request.method == 'POST':
        # Get the Instagram username from the HTML form
        username = request.form.get('instagram-username')
        
        # Create an Instaloader instance
        L = instaloader.Instaloader()
        
        try:
            # Fetch the user's profile information
            profile = instaloader.Profile.from_username(L.context, username)
            
            # Get the user's ID (needed to filter comments made by the user)
            user_id = profile.userid
            num_posts = profile.mediacount
            num_followers = profile.followers
            num_followings = profile.followees
            
            # Create a list to store post captions
            captions = []
            
            # Iterate through the user's posts and store captions
            for post in profile.get_posts():
                captions.append(post.caption)

            return redirect(url_for('redirect_page'))
        
        except Exception as e:
            error_message = f'An error occurred: {e}'
            return render_template('main.html', error=error_message)

    # Default response with the form
    return render_template('main.html')

@app.route('/redirect', methods=['GET'])
def redirect_page():
    return render_template('redirect.html')

if __name__ == '__main__':
    app.run(debug=True)
