from dotenv import load_dotenv
import os
import requests
import security.auth
import json
from oauthlib.oauth2 import WebApplicationClient

load_dotenv()
__GOOGLE_DISCOVERY_URL = "https://accounts.google.com/.well-known/openid-configuration"
__GOOGLE_CLIENT_ID = os.environ.get("GOOGLE_CLIENT_ID", None)
__GOOGLE_CLIENT_SECRET = os.environ.get("GOOGLE_CLIENT_SECRET", None)
__SITE_URL = os.environ.get("SITE_URL", None)

def login_user(code: str, request_url: str, base_url: str):
    google_provider_cfg = __get_google_provider_cfg()

    client = WebApplicationClient(__GOOGLE_CLIENT_ID)
    token_url, headers, body = client.prepare_token_request(
        google_provider_cfg["token_endpoint"],
        authorization_response=request_url,
        redirect_url=base_url + "login/callback",
        code=code
    )
    token_response = requests.post(
        token_url,
        headers=headers,
        data=body,
        auth=(__GOOGLE_CLIENT_ID, __GOOGLE_CLIENT_SECRET),
    )

    # Parse the tokens!
    json_response = json.dumps(token_response.json())
    client.parse_request_body_response(json_response)

    # Now that you have tokens (yay) let's find and hit the URL
    # from Google that gives you the user's profile information,
    # including their Google profile image and email
    userinfo_endpoint = google_provider_cfg["userinfo_endpoint"]
    uri, headers, body = client.add_token(userinfo_endpoint)
    userinfo_response = requests.get(uri, headers=headers, data=body)

    # You want to make sure their email is verified.
    # The user authenticated with Google
    if userinfo_response.json().get("email_verified"):
        unique_id = userinfo_response.json()["sub"]
        users_email = userinfo_response.json()["email"]
        picture = userinfo_response.json()["picture"]
        users_name = userinfo_response.json()["name"]
        return security.auth.login_user(username=users_email)
    else:
        return "User email not available or not verified by Google.", 400

def get_auth_endpoint(base_url: str):
    client = WebApplicationClient(__GOOGLE_CLIENT_ID)
    request_uri = client.prepare_request_uri(
        __get_authorization_endpoint(),
        redirect_uri=base_url + "login/callback",
        scope=["openid", "email", "profile"],
    )
    return request_uri;

def __get_google_provider_cfg():
    google_provider_cfg = requests.get(__GOOGLE_DISCOVERY_URL).json()
    return google_provider_cfg

# Find out what URL to hit for Google login
def __get_authorization_endpoint():
    google_provider_cfg = __get_google_provider_cfg()
    authorization_endpoint = google_provider_cfg["authorization_endpoint"]
    return authorization_endpoint
