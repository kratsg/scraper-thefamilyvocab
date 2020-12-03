from instagram_basic_display.InstagramBasicDisplay import InstagramBasicDisplay
import os
from flask import Flask, request

app_id = os.getenv('IG_APP_ID')
app_secret = os.getenv('IG_APP_SECRET')
app_url = os.getenv('IG_APP_URL')

instagram_basic_display = InstagramBasicDisplay(app_id=app_id, app_secret=app_secret, redirect_url=app_url)

print(instagram_basic_display.get_login_url()) # Returns login URL you need to follow

app = Flask(__name__)
@app.route('/')
def redirect_url():
    breakpoint()
    # Get the OAuth callback code
    code = request.args.get('code')

    # Get the short lived access token (valid for 1 hour)
    short_lived_token = instagram_basic_display.get_o_auth_token(code)

    # Exchange this token for a long lived token (valid for 60 days)
    long_lived_token = instagram_basic_display.get_long_lived_token(short_lived_token.get('access_token'))

    print('Your token is: {}' .format(long_lived_token.get('access_token')))

if __name__ == "__main__":
    app.run(ssl_context='adhoc', host='0.0.0.0', port=3000)
