import instaloader


# Replace 'your_username' with the target Instagram username
username = 'aniketv2003'

# Create an Instaloader instance
L = instaloader.Instaloader()

try:
    # Fetch the user's profile information
    profile = instaloader.Profile.from_username(L.context, username)

    # Get the user's ID (needed to filter comments made by the user)
    user_id = profile.userid
    num_posts = profile.mediacount

    print(f'Number of posts: {num_posts}')

    num_followers = profile.followers
    num_followings = profile.followees

    print(f'Followers: {num_followers}')
    print(f'Followings: {num_followings}')
    # Iterate through the user's posts
    for post in profile.get_posts():
        print(f'Caption: {post.caption}')
        
        # Iterate through the post's comments
        # Introduce a delay between requests (e.g., 2 seconds)
        # time.sleep(2)  # You can adjust the delay duration as needed
        
except Exception as e:
    print(f'An error occurred: {e}')
