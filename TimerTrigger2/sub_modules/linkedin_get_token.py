import requests

url = 'https://www.linkedin.com/oauth/v2/accessToken'
params = {
 'grant_type': 'authorization_code',
 'code': 'your_authorization_code',
 'redirect_uri': 'https://yourwebsite.com/callback',
 'client_id': 'your_client_id',
 'client_secret': 'your_client_secret'
 }

response = requests.post(url, data=params)

if response.status_code == 200:
    access_token = response.json()['access_token']
    print('Access token:', access_token)
else:
    print('Error:', response.status_code, response.text)


curl -X GET "https://www.linkedin.com/oauth/v2/authorization?response_type=code&client_id=77fn19edcg40p1&redirect_uri=https://irfan-ahmad.com/auth/linkedin/callback&state=12345&scope=r_emailaddress, r_liteprofile, w_member_social"

