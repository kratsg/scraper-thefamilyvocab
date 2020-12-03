from instagram_basic_display.InstagramBasicDisplay import InstagramBasicDisplay
import os

app_id = os.getenv('IG_APP_ID')
app_secret = os.getenv('IG_APP_SECRET')
app_url = os.getenv('IG_APP_URL')
access_token = os.getenv('IG_ACCESS_TOKEN')

instagram_basic_display = InstagramBasicDisplay(app_id=app_id, app_secret=app_secret, redirect_url=app_url)
instagram_basic_display.set_access_token(access_token)

user_id='24285630983' # thefamilyvocab
instagram_basic_display.get_user_profile(user_id=user_id)
