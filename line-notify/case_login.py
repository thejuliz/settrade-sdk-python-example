# Import Settrade SDK
from settrade.openapi import Investor

# Import SDK Line Notify
from settrade_line_notify.notification import LineNotify

# Init LineNotify
token = 'line_notify_token'
notifier = LineNotify(token)

try:
    investor = Investor(
                app_id="Your App Id",                                 
                app_secret="Your App Secret",
                broker_id="Your Broker Id",                                           
                app_code="Your App Code",
                is_auto_queue = False)
except:
    notifier.notify('Login error, please investigate.')
