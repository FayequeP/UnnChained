import os
import requests
from dotenv import load_dotenv

load_dotenv()

class InstagramGraphAPI:
    def __init__(self, app_id, app_secret, redirect_uri):
        self.app_id = str(os.getenv('APP_ID'))
        self.app_secret = str(os.getenv('APP_SECRET'))
        self.redirect_uri = str(os.getenv('REDIRECT_URI'))
        self.access_token = None
        self.refresh_token = None

    def get_access_token(self):
        auth_url = f"https://api.instagram.com/oauth/authorize/?client_id={self.app_id}&redirect_uri={self.redirect_uri}&scope=instagram_basic,pages_show_list"
        response = requests.get(auth_url)
        code = response.url.split("=")[1]
        token_url = f"https://api.instagram.com/oauth/access_token/"
        data = {
            "client_id": self.app_id,
            "client_secret": self.app_secret,
            "redirect_uri": self.redirect_uri,
            "code": code,
            "grant_type": "authorization_code"
        }
        response = requests.post(token_url, data=data)
        if response.status_code == 200:
            response_json = response.json()
            self.access_token = response_json["access_token"]
            self.refresh_token = response_json.get("refresh_token")
            return self.access_token
        else:
            print(f"Error getting access token: {response.text}")
            return None

    def refresh_access_token(self):
        # Implement token refresh logic here
        pass

    def authenticate(self):
        if not self.access_token:
            self.get_access_token()
        headers = {"Authorization": f"Bearer {self.access_token}"}
        response = requests.get("https://graph.instagram.com/me", headers=headers)
        if response.status_code == 401:  # Token is invalid or expired
            self.refresh_access_token()
            return self.authenticate()
        elif response.status_code == 200:
            return True
        else:
            return False

    def get_user_media(self):
        if not self.authenticate():
            return None
        api_url = "https://graph.instagram.com/me/media"
        headers = {"Authorization": f"Bearer {self.access_token}"}
        response = requests.get(api_url, headers=headers)
        return response.json()["data"]

    def monitor_comments(self):
        if not self.authenticate():
            return None
        api_url = "https://graph.instagram.com/me/comments"
        headers = {"Authorization": f"Bearer {self.access_token}"}
        response = requests.get(api_url, headers=headers)
        comments = response.json()["data"]
        for comment in comments:
            if keyword in comment["text"]:
                # Send DM using the AI agent
                ai_agent.send_dm(comment["from"]["id"], "Hello!")
                # Start conversation using the funnel
                funnel = "your_funnel"
                ai_agent.start_conversation(comment["from"]["id"], funnel)
        return None