from django.shortcuts import render
from django.shortcuts import redirect
from django.db.models import F
from.models import Media, Comment
from django.contrib.auth.decorators import login_required
from unchained.settings import REDIRECT_URI, APP_ID, APP_SECRET
from.instagram_graph_api import InstagramGraphAPI
import requests

# Create your views here.

class InstagramView:
    def __init__(self):
        self.instagram_api = InstagramGraphAPI(app_id=APP_ID, app_secret=APP_SECRET, redirect_uri=REDIRECT_URI)

    def get_user_media(self, request):
        user_media = self.instagram_api.get_user_media()
        if user_media is None:
            return render(request, "instagram_media.html", {"user_media": []})  
        for media in user_media:
            Media.objects.create(image_url=media["image_url"], caption=media["caption"], likes=media["likes"], comments=media["comments"])
        return render(request, "instagram_media.html", {"user_media": user_media})

    def monitor_comments(self, request):
        comments = self.instagram_api.monitor_comments()
        if comments is None:
            return None
        for comment in comments:
            # Monitor the comment and take action if necessary
            if keyword in comment["text"]:
                # Send DM using the AI agent
                ai_agent.send_dm(comment["from"]["id"], "Hey, I just saw the comment.")
                # Start conversation using the funnel
                funnel = "your_funnel"
                ai_agent.start_conversation(comment["from"]["id"], funnel)
        return None

@login_required
def home_view(request):
    instagram_view = InstagramView()
    user_media = instagram_view.get_user_media(request)
    instagram_view.monitor_comments(request)  # Monitor comments in the background
    return render(request, "home.html", {"user_media": user_media})

@login_required
def get_access_token(request):
    # Redirect the user to the Instagram authorization URL
    auth_url = f"https://api.instagram.com/oauth/authorize/?client_id={APP_ID}&redirect_uri={REDIRECT_URI}&scope=instagram_basic,pages_show_list"
    return redirect(auth_url)

@login_required
def get_token(request):
    # Handle the redirect from Instagram and obtain the access token
    code = request.GET.get("code")
    token_url = f"https://api.instagram.com/oauth/access_token/?client_id={APP_ID}&client_secret={APP_SECRET}&redirect_uri={REDIRECT_URI}&code={code}"
    response = requests.post(token_url)
    access_token = response.json()["access_token"]
    return access_token