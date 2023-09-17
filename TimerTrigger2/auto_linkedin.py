import requests
from decouple import config

# Constants
ACCESS_TOKEN = config('ACCESS_TOKEN')

API_URL = 'https://api.linkedin.com/v2/ugcPosts'

def create_main_post_text(access_token, text):
    # Set up headers for the request
    post_request = {
        "author": "urn:li:person:QuVa1wSAAP",
        "lifecycleState": "PUBLISHED",
        "specificContent": {
            "com.linkedin.ugc.ShareContent": {
                "shareCommentary": {
                    "text": text
                },
                "shareMediaCategory": "NONE"
            }
        },
        "visibility": {
            "com.linkedin.ugc.MemberNetworkVisibility": "PUBLIC"
        }
    }
    
    headers = {
        'Authorization': f'Bearer {access_token}',
        'Connection': 'Keep-Alive',
        'Content-Type': 'application/json',
    }

    # Send the POST request
    response = requests.post(API_URL, headers=headers, json=post_request)
    return response

def main(message):

    # Create the post
    response = create_main_post_text(ACCESS_TOKEN, message)

    # Check the response status code and provide a clear message
    if response.status_code == 201:
        print('Post successfully created!')
    else:
        print(f'Post creation failed with status code {response.status_code}: {response.text}')

if __name__ == "__main__":
    main()

