import requests

# Define the user's access token and the Facebook API version
access_token = 'EAAKBP0EPSasBO6uHGywA23ALpWQl2zhwWeYCZBPdcpL8cyj79hD3nZANHZAGvQXL3e03v4xhOS13ekx0WqhJOswZAKmoaBuaZCUBrTi6dVZAsOCipl8vtiJVCPftxTNRLlhZAx8FaWhEYuQA3fPIt0epoSaYZBZAsHidZCu3M54kTQeFoRAC81rLiW7MP6K4W7kI1NhtFQiUVrDITL3SMSn7DZBvOyQIduSiMK17zQ2AUgWh7bnOtSRZBs8oszjFfdU4YSOSXnAWKQZDZD'
api_version = 'v18.0'

# Make a request to get the user's liked posts
liked_posts_url = f'https://graph.facebook.com/{api_version}/me/likes?fields=id,created_time,message&access_token={access_token}'
response = requests.get(liked_posts_url)
if response.status_code == 200:
    liked_posts_data = response.json()
    liked_posts = liked_posts_data.get('data', [])

    # Iterate through the liked posts and print their information
    for post in liked_posts:
        post_id = post['id']
        created_time = post['created_time']
        message = post.get('message', 'No message available')
        
        print(f"Post ID: {post_id}")
        print(f"Created Time: {created_time}")
        print(f"Message: {message}\n")
else:
    print(f"Failed to retrieve liked posts. Status code: {response.status_code}")
