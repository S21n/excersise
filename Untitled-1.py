import requests

# The client_id, client_secret, and tenant_id are all available in the Azure portal
client_id = 'your_client_id'
client_secret = 'your_client_secret'
tenant_id = 'your_tenant_id'

# Scopes for the permissions your app requires
scopes = ['User.Read', 'Mail.Read']

# The authorization endpoint
authorization_endpoint = f'https://login.microsoftonline.com/{tenant_id}/oauth2/v2.0/authorize'

# The token endpoint
token_endpoint = f'https://login.microsoftonline.com/{tenant_id}/oauth2/v2.0/token'

# The URL for the mail API
mail_api_url = 'https://graph.microsoft.com/v1.0/me/messages'

# Step 1: Get an authorization code
authorization_request_url = authorization_endpoint + '?' + '&'.join([
    'client_id=' + client_id,
    'response_type=code',
    'redirect_uri=http%3A%2F%2Flocalhost%2F',
    'scope=' + ' '.join(scopes),
    'state=12345'
])

# Step 2: Get an access token
def get_token(code):
    data = {
        'client_id': client_id,
        'scope': ' '.join(scopes),
        'code': code,
        'redirect_uri': 'http%3A%2F%2Flocalhost%2F',
        'grant_type': 'authorization_code',
        'client_secret': client_secret
    }
    response = requests.post(token_endpoint, data=data)
    return response.json()

# Step 3: Use the access token to call the Microsoft Graph API
def call_api(access_token):
    headers = {
        'Authorization': 'Bearer ' + access_token,
        'Content-Type': 'application/json'
    }
    response = requests.get(mail_api_url, headers=headers)
    return response.json()

# The user is redirected to the authorization request URL, logs in, and grants permissions
# The authorization server redirects the user back to your app, including an authorization code in the URL
# You extract the authorization code and use it to get an access token
# You use the access token to call the Microsoft Graph API