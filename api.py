from project_secrets import API_KEY, SECRET_KEY
import requests

auth_token = None

@app.before_first_request
def refresh_credentials():
    """Just once, get token and store it globally."""
    global auth_token
    auth_token = update_auth_token_string()


def update_auth_token_string():
    """ makes request to authenticate with petfinder api
        returns Oauth token 
    """
    resp = requests.get('https://api.petfinder.com/v2/animals?limit=100',
                        headers={Authorization: f"Bearer {API_KEY}"})

    return resp.json()['access_token']



def get_rand_pet():
    """ gets a random pet and returns the name, age, and a photo URL. """

