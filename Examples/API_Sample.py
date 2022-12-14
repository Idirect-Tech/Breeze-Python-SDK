### Enter your API Keys

api_key = "INSERT_YOUR_APP_KEY_HERE"
api_secret = "INSERT_YOUR_SECRET_KEY_HERE"
api_session = 'INSERT_YOUR_API_SESSION_HERE'

### Import Libraries

import json
import http.client
import base64 
import socketio


######################################################################################################################################################################################################

### Customer Details API

conn = http.client.HTTPSConnection("api.icicidirect.com")

payload = {
    'SessionToken': api_session,
    'AppKey': api_key
}

headers = {"Content-Type": "application/json"}

conn.request("GET", "/breezeapi/api/v1/customerdetails", str(payload), headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))


#### Store Session Token

session_token = json.loads(data.decode("utf-8"))
session_token = session_token['Success']['session_token']


######################################################################################################################################################################################################

### One Sec OHLC API

conn = http.client.HTTPSConnection("breezeapi.icicidirect.com")
payload = None

headers = {
    'X-SessionToken': session_token,
    'apikey': api_key
}

conn.request("GET", "/api/v2/historicalcharts?stock_code=NIFTY&exch_code=NFO&from_date=2022-11-10T00:00:00.000Z&to_date=2022-11-11T00:00:00.000Z&interval=1day&product_type=Options&expiry_date=2022-11-24T00:00:00.000Z&right=Call&strike_price=18000", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))

historical_data = json.loads(data.decode("utf-8"))['Success']



######################################################################################################################################################################################################

### Streaming Candles Live Feed (Websocket)

#Get User ID and Decode Session Token
user_id, decoded_session_token = base64.b64decode(session_token.encode('ascii')).decode('ascii').split(":")

# Python Socket IO Client
sio = socketio.Client()
auth = {"user": user_id, "token": decoded_session_token}
sio.connect("https://breezeapi.icicidirect.com/", socketio_path='ohlcvstream', headers={"User-Agent":"python-socketio[client]/socket"}, 
                auth=auth, transports="websocket", wait_timeout=3)

# Script Code of Stock or Instrument  e.g 4.1!1594, 1.1!500209 , 13.1!5023, 6.1!247457. 
script_code = ["4.1!2885"] #Subscribe more than one stock at a time

#Channel name i.e 1SEC,1MIN,5MIN,30MIN
channel_name = "1SEC"

#CallBack functions to receive feeds
def on_ticks(ticks):
    print(ticks)
    
#Connect to receive feeds
sio.emit('join', script_code)
sio.on(channel_name, on_ticks)

#Leave to stop receiving feeds
sio.emit("leave", script_code)

#Disconnect from the server
sio.emit("disconnect", "transport close")
