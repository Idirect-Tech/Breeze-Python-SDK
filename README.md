# Table Of Content

<ul>
 <li><a href="#client">Breeze API Python Client</a></li>
 <li><a href="#docslink">API Documentation</a></li>
 <li><a href="#virtualenv">Set Up Virtual Environment</a></li>
 <li><a href="#clientinstall">Installing Client</a></li>
 <li><a href="#websocket">Websocket Usage</a></li>
 <li><a href="#apiusage">API Usage</a></li>
 <li><a href="#index_title">List Of APIs</a></li>
</ul>

<h3 id="client"><b>Breeze API Python Client</b></h3>

breezeapi@icicisecurities.com

The official Python client library for the ICICI Securities trading APIs. BreezeConnect is a set of REST-like APIs that allows one to build a complete investment and trading platform. Following are some notable features of Breeze APIs:

1. Execute orders in real time
2. Manage Portfolio
3. Access to 10 years of historical market data including 1 sec OHLCV
4. Streaming live OHLC (websockets)
5. Option Chain API

To install breeze strategies :<a href="https://pypi.org/project/breeze-strategies/"> Click here </a>

<h3 id="docslink"><b>API Documentation</b></h3>

<div class="sticky" >
<ul>
 <li><a href="https://api.icicidirect.com/breezeapi/documents/index.html">Breeze HTTP API Documentation</a></li>
 <li><a href="https://pypi.org/project/breeze-connect/">Python client documentation</a></li>
</ul>
</div>

<h3 id="virtualenv"><b>Setup virtual environment in your Machine</b></h3>

You must install the virtualenv package via pip
```
pip install virtualenv
```

You should create breeze virtual environment via virtualenv
```
virtualenv -p python3 breeze_venv
```

And then, You can activate virtual environment via source
```
source breeze_venv/bin/activate
```

<h3 id="clientinstall"><b>Installing the client</b></h3>

You can install the latest release via pip

```
pip install --upgrade breeze-connect
```

Or, You can also install the specific release version via pip

```
pip install breeze-connect==1.0.62
```


<h3 id="websocket"><b> Websocket Usage </b></h3>

```python
from breeze_connect import BreezeConnect

# Initialize SDK
breeze = BreezeConnect(api_key="your_api_key")

# Obtain your session key from https://api.icicidirect.com/apiuser/login?api_key=YOUR_API_KEY
# Incase your api-key has special characters(like +,=,!) then encode the api key before using in the url as shown below.
import urllib
print("https://api.icicidirect.com/apiuser/login?api_key="+urllib.parse.quote_plus("your_api_key"))

# Generate Session
breeze.generate_session(api_secret="your_secret_key",
                        session_token="your_api_session")

# Connect to websocket(it will connect to tick-by-tick data server)
breeze.ws_connect()

# Callback to receive ticks.
def on_ticks(ticks):
    print("Ticks: {}".format(ticks))

# Assign the callbacks.
breeze.on_ticks = on_ticks

# ws_disconnect (it will disconnect from all actively connected servers)
breeze.ws_disconnect()
```
<hr>

<h2>Subscribing to Real Time Streaming OHLCV Data of stocks by stock-token</h2>

```python
breeze.subscribe_feeds(stock_token="4.1!2885", 
                      interval="1minute")
```
<br>
<details>
  <summary><b>View Response</b></summary>

```json
{'message': 'Stock 4.1!2885 subscribed successfully'}
Ticks: {'interval': '1minute', 'exchange_code': 'NSE', 'stock_code': 'RELIND', 'low': '1199.5', 'high': '1200.15', 'open': '1199.95', 'close': '1200.0', 'volume': '40752', 'datetime': '2025-02-12 10:04:00'}
Ticks: {'interval': '1minute', 'exchange_code': 'NSE', 'stock_code': 'RELIND', 'low': '1199.3', 'high': '1201.0', 'open': '1200.0', 'close': '1200.2', 'volume': '113253', 'datetime': '2025-02-12 10:05:00'}

```
</details>
<h4> NOTE : </h4>
<p>For unsubscribe : breeze.unsubscribe_feeds(stock_token="4.1!2885", 
                      interval="1minute")</p>

<h2>Subscribe equity stocks by stock-token (Exchange Quotes)</h2>

```python 
    breeze.subscribe_feeds(stock_token="4.1!2885")
```
<br>

<details>
  <summary><b>View Response</b></summary>

```json
{'message': 'Stock 4.1!2885 subscribed successfully'}
Ticks: {'symbol': '4.1!2885', 'open': 1219.45, 'last': 1209.05, 'high': 1226.9, 'low': 1193.35, 'change': -2.09, 'bPrice': 1209.05, 'bQty': 13, 'sPrice': 1209.35, 'sQty': 34, 'ltq': 1, 'avgPrice': 1208.86, 'quotes': 'Quotes Data', 'ttq': 10991550, 'totalBuyQt': 762919, 'totalSellQ': 619405, 'ttv': '1328.72C', 'trend': '', 'lowerCktLm': 1111.4, 'upperCktLm': 1358.3, 'ltt': 'Wed Feb 12 11:12:20 2025', 'close': 1234.85, 'exchange': 'NSE Equity', 'stock_name': 'RELIANCE INDUSTRIES'}
Ticks: {'symbol': '4.1!2885', 'open': 1219.45, 'last': 1209.05, 'high': 1226.9, 'low': 1193.35, 'change': -2.09, 'bPrice': 1209.05, 'bQty': 13, 'sPrice': 1209.35, 'sQty': 34, 'ltq': 1, 'avgPrice': 1208.86, 'quotes': 'Quotes Data', 'ttq': 10991550, 'totalBuyQt': 762919, 'totalSellQ': 619405, 'ttv': '1328.72C', 'trend': '', 'lowerCktLm': 1111.4, 'upperCktLm': 1358.3, 'ltt': 'Wed Feb 12 11:12:20 2025', 'close': 1234.85, 'exchange': 'NSE Equity', 'stock_name': 'RELIANCE INDUSTRIES'}

```
</details>
<h4> NOTE : </h4>
<p>For unsubscribe : breeze.subscribe_feeds(stock_token="4.1!2885")</p>
<h2>Subscribe to Real Time Streaming OHLCV Data of NFO stocks</h2>

```python 
breeze.subscribe_feeds(exchange_code= "NFO", 
                  stock_code="NIFTY", 
                  expiry_date="13-Feb-2025", 
                  strike_price="23550", 
                  right="call", 
                  product_type="options", 
                  get_market_depth=False ,
                  get_exchange_quotes=True,
                  interval="1minute")
```
<br>

<details>
  <summary><b>View Response</b></summary>

```json
{'message': 'Stock NIFTY subscribed successfully'}
Ticks: {'interval': '1minute', 'exchange_code': 'NFO', 'stock_code': 'NIFTY', 'expiry_date': '13-Feb-2025', 'strike_price': '23550.0', 'right_type': 'CE', 'low': '7.4', 'high': '8.25', 'open': '7.55', 'close': '8.2', 'volume': '354975', 'oi': '4763100', 'datetime': '2025-02-12 12:10:00'}
Ticks: {'interval': '1minute', 'exchange_code': 'NFO', 'stock_code': 'NIFTY', 'expiry_date': '13-Feb-2025', 'strike_price': '23550.0', 'right_type': 'CE', 'low': '7.75', 'high': '8.85', 'open': '8.2', 'close': '7.8', 'volume': '412950', 'oi': '4763100', 'datetime': '2025-02-12 12:11:00'}

```
</details>
<h4> NOTE : </h4>
<p>For unsubscribe : breeze.unsubscribe_feeds(exchange_code= "NFO", 
                  stock_code="NIFTY", 
                  expiry_date="13-Feb-2025", 
                  strike_price="23550", 
                  right="call", 
                  product_type="options", 
                  get_market_depth=False ,
                  get_exchange_quotes=True,
                  interval="1minute")</p>

<h2>Subscribe stocks feeds (NFO Exchange Quotes)</h2>

```python 
breeze.subscribe_feeds(exchange_code= "NFO", 
                  stock_code="NIFTY", 
                  expiry_date="13-Feb-2025", 
                  strike_price="23550", 
                  right="call", 
                  product_type="options", 
                  get_market_depth=False ,
                  get_exchange_quotes=True)
```
<br>

<details>
  <summary><b>View Response</b></summary>

```json
{'message': 'Stock NIFTY subscribed successfully'}
Ticks: {'symbol': '4.1!51219', 'open': 11.4, 'last': 8.5, 'high': 11.4, 'low': 3.1, 'change': -28.27, 'bPrice': 8.5, 'bQty': 9300, 'sPrice': 8.6, 'sQty': 8700, 'ltq': 75, 'avgPrice': 5.41, 'quotes': 'Quotes Data', 'OI': 4763100, 'CHNGOI': None, 'ttq': 70816125, 'totalBuyQt': 1974300, 'totalSellQ': 548625, 'ttv': '38.31C', 'trend': '', 'lowerCktLm': 0.05, 'upperCktLm': 39.15, 'ltt': 'Wed Feb 12 12:12:55 2025', 'close': 11.85, 'exchange': 'NSE Futures & Options', 'stock_name': 'NIFTY 50', 'product_type': 'Options', 'expiry_date': '13-Feb-2025', 'strike_price': '23550', 'right': 'Call'}
Ticks: {'symbol': '4.1!51219', 'open': 11.4, 'last': 8.5, 'high': 11.4, 'low': 3.1, 'change': -28.27, 'bPrice': 8.4, 'bQty': 14475, 'sPrice': 8.5, 'sQty': 6750, 'ltq': 75, 'avgPrice': 5.41, 'quotes': 'Quotes Data', 'OI': 4763100, 'CHNGOI': None, 'ttq': 70818150, 'totalBuyQt': 1962375, 'totalSellQ': 558750, 'ttv': '38.31C', 'trend': '', 'lowerCktLm': 0.05, 'upperCktLm': 39.15, 'ltt': 'Wed Feb 12 12:12:54 2025', 'close': 11.85, 'exchange': 'NSE Futures & Options', 'stock_name': 'NIFTY 50', 'product_type': 'Options', 'expiry_date': '13-Feb-2025', 'strike_price': '23550', 'right': 'Call'}

```
</details>
<h4> NOTE : </h4>
<p>For unsubscribe : breeze.unsubscribe_feeds(exchange_code= "NFO", 
                  stock_code="NIFTY", 
                  expiry_date="13-Feb-2025", 
                  strike_price="23550", 
                  right="call", 
                  product_type="options", 
                  get_market_depth=False ,
                  get_exchange_quotes=True)</p>


<h2>Subscribe stocks feeds (NFO Market Depth)</h2>

```python 
breeze.subscribe_feeds(exchange_code= "NFO", 
                  stock_code="NIFTY", 
                  expiry_date="13-Feb-2025", 
                  strike_price="23550", 
                  right="call", 
                  product_type="options", 
                  get_market_depth=True ,
                  get_exchange_quotes=False)
```
<br>

<details>
  <summary><b>View Response</b></summary>

```json
{'message': 'Stock NIFTY subscribed successfully'}
Ticks: {'symbol': '4.2!51219', 'time': 'Wed Feb 12 12:16:18 2025', 'depth': [{'BestBuyRate-1': 7.25, 'BestBuyQty-1': 8475, 'BuyNoOfOrders-1': 17, 'BuyFlag-1': '', 'BestSellRate-1': 7.3, 'BestSellQty-1': 4350, 'SellNoOfOrders-1': 7, 'SellFlag-1': ''}, {'BestBuyRate-2': 7.2, 'BestBuyQty-2': 9675, 'BuyNoOfOrders-2': 17, 'BuyFlag-2': '', 'BestSellRate-2': 7.35, 'BestSellQty-2': 6900, 'SellNoOfOrders-2': 13, 'SellFlag-2': ''}, {'BestBuyRate-3': 7.15, 'BestBuyQty-3': 4800, 'BuyNoOfOrders-3': 10, 'BuyFlag-3': '', 'BestSellRate-3': 7.4, 'BestSellQty-3': 11700, 'SellNoOfOrders-3': 21, 'SellFlag-3': ''}, {'BestBuyRate-4': 7.1, 'BestBuyQty-4': 12825, 'BuyNoOfOrders-4': 19, 'BuyFlag-4': '', 'BestSellRate-4': 7.45, 'BestSellQty-4': 9300, 'SellNoOfOrders-4': 15, 'SellFlag-4': ''}, {'BestBuyRate-5': 7.05, 'BestBuyQty-5': 6300, 'BuyNoOfOrders-5': 9, 'BuyFlag-5': '', 'BestSellRate-5': 7.5, 'BestSellQty-5': 13200, 'SellNoOfOrders-5': 20, 'SellFlag-5': ''}], 'quotes': 'Market Depth', 'stock_name': 'NIFTY 50', 'product_type': 'Options', 'expiry_date': '13-Feb-2025', 'strike_price': '23550', 'right': 'Call'}
Ticks: {'symbol': '4.2!51219', 'time': 'Wed Feb 12 12:16:19 2025', 'depth': [{'BestBuyRate-1': 7.3, 'BestBuyQty-1': 10950, 'BuyNoOfOrders-1': 22, 'BuyFlag-1': '', 'BestSellRate-1': 7.35, 'BestSellQty-1': 3150, 'SellNoOfOrders-1': 3, 'SellFlag-1': ''}, {'BestBuyRate-2': 7.25, 'BestBuyQty-2': 9675, 'BuyNoOfOrders-2': 17, 'BuyFlag-2': '', 'BestSellRate-2': 7.4, 'BestSellQty-2': 10050, 'SellNoOfOrders-2': 18, 'SellFlag-2': ''}, {'BestBuyRate-3': 7.2, 'BestBuyQty-3': 7275, 'BuyNoOfOrders-3': 14, 'BuyFlag-3': '', 'BestSellRate-3': 7.45, 'BestSellQty-3': 12300, 'SellNoOfOrders-3': 19, 'SellFlag-3': ''}, {'BestBuyRate-4': 7.15, 'BestBuyQty-4': 4050, 'BuyNoOfOrders-4': 8, 'BuyFlag-4': '', 'BestSellRate-4': 7.5, 'BestSellQty-4': 15000, 'SellNoOfOrders-4': 21, 'SellFlag-4': ''}, {'BestBuyRate-5': 7.1, 'BestBuyQty-5': 12975, 'BuyNoOfOrders-5': 20, 'BuyFlag-5': '', 'BestSellRate-5': 7.55, 'BestSellQty-5': 6150, 'SellNoOfOrders-5': 12, 'SellFlag-5': ''}], 'quotes': 'Market Depth', 'stock_name': 'NIFTY 50', 'product_type': 'Options', 'expiry_date': '13-Feb-2025', 'strike_price': '23550', 'right': 'Call'}

```
</details>
<h4> NOTE : </h4>
<p>For unsubscribe : breeze.unsubscribe_feeds(exchange_code= "NFO", 
                  stock_code="NIFTY", 
                  expiry_date="13-Feb-2025", 
                  strike_price="23550", 
                  right="call", 
                  product_type="options", 
                  get_market_depth=True ,
                  get_exchange_quotes=False)</p> 


<h2>Subscribe to Real Time Streaming OHLCV Data of BFO stocks</h2>

```python 
breeze.subscribe_feeds(exchange_code= "BFO", 
                  stock_code="BSESEN", 
                  expiry_date="18-Feb-2025", 
                  strike_price="78200", 
                  right="call", 
                  product_type="options", 
                  get_market_depth=False,
                  get_exchange_quotes=True,
                  interval="1minute")
```
<br>

<details>
  <summary><b>View Response</b></summary>

```json
{'message': 'Stock BSESEN subscribed successfully'}
Ticks: {'interval': '1minute', 'exchange_code': 'BFO', 'stock_code': 'BSESEN', 'expiry_date': '18-Feb-2025', 'strike_price': '78200.0', 'right_type': 'CE', 'low': '83.6', 'high': '89.6', 'open': '89.6', 'close': '83.8', 'volume': '4420', 'oi': '0', 'datetime': '2025-02-12 12:54:00'}
Ticks: {'interval': '1minute', 'exchange_code': 'BFO', 'stock_code': 'BSESEN', 'expiry_date': '18-Feb-2025', 'strike_price': '78200.0', 'right_type': 'CE', 'low': '82.0', 'high': '86.0', 'open': '82.0', 'close': '84.2', 'volume': '3200', 'oi': '0', 'datetime': '2025-02-12 12:55:00'}

```
</details>
<h4> NOTE : </h4>
<p>For unsubscribe : breeze.unsubscribe_feeds(exchange_code= "BFO", 
                  stock_code="BSESEN", 
                  expiry_date="18-Feb-2025", 
                  strike_price="78200", 
                  right="call", 
                  product_type="options", 
                  get_market_depth=False,
                  get_exchange_quotes=True,
                  interval="1minute)
                  </p>

<h2>Subscribe stocks feeds (BFO Exchange Quotes)</h2>

```python 
breeze.subscribe_feeds(exchange_code= "BFO", 
                  stock_code="BSESEN", 
                  expiry_date="18-Feb-2025", 
                  strike_price="78200", 
                  right="call", 
                  product_type="options", 
                  get_market_depth=False,
                  get_exchange_quotes=True)
```
<br>

<details>
  <summary><b>View Response</b></summary>

```json
{'message': 'Stock BSESEN subscribed successfully'}
Ticks: {'symbol': '8.1!844663', 'open': 96, 'last': 98, 'high': 105.8, 'low': 35.25, 'change': -2.05, 'bPrice': 96.8, 'bQty': 40, 'sPrice': 97.25, 'sQty': 120, 'ltq': 20, 'avgPrice': 61.87, 'quotes': 'Quotes Data', 'OI': 37020, 'CHNGOI': 12880, 'ttq': 809940, 'totalBuyQt': 30800, 'totalSellQ': 12360, 'ttv': 6338.74, 'trend': '', 'lowerCktLm': 0.05, 'upperCktLm': 505.8, 'ltt': 'Wed Feb 12 12:53:33 2025', 'close': 100.05}
Ticks: {'symbol': '8.1!844663', 'open': 96, 'last': 98, 'high': 105.8, 'low': 35.25, 'change': -2.05, 'bPrice': 96.8, 'bQty': 40, 'sPrice': 97.25, 'sQty': 120, 'ltq': 20, 'avgPrice': 61.87, 'quotes': 'Quotes Data', 'OI': 37020, 'CHNGOI': 12880, 'ttq': 809940, 'totalBuyQt': 30800, 'totalSellQ': 12360, 'ttv': 6338.74, 'trend': '', 'lowerCktLm': 0.05, 'upperCktLm': 505.8, 'ltt': 'Wed Feb 12 12:53:33 2025', 'close': 100.05}

```
</details>
<h4> NOTE : </h4>
<p>For unsubscribe : breeze.unsubscribe_feeds(exchange_code= "BFO", 
                  stock_code="BSESEN", 
                  expiry_date="18-Feb-2025", 
                  strike_price="78200", 
                  right="call", 
                  product_type="options", 
                  get_market_depth=False,
                  get_exchange_quotes=True)</p>

<h2>Subscribe stocks feeds (BFO Market Depth)</h2>

```python 
breeze.subscribe_feeds(exchange_code= "BFO", 
                  stock_code="BSESEN", 
                  expiry_date="18-Feb-2025", 
                  strike_price="78200", 
                  right="call", 
                  product_type="options", 
                  get_market_depth=True ,
                  get_exchange_quotes=False )
```
<br>

<details>
  <summary><b>View Response</b></summary>

```json
{'message': 'Stock BSESEN subscribed successfully'}
Ticks: {'symbol': '8.2!844663', 'time': 'Wed Feb 12 12:49:50 2025', 'depth': [{'BestBuyRate-1': 87.3, 'BestBuyQty-1': 20, 'BuyNoOfOrders-1': 1, 'BestSellRate-1': 87.8, 'BestSellQty-1': 20, 'SellNoOfOrders-1': 1}, {'BestBuyRate-2': 87.25, 'BestBuyQty-2': 480, 'BuyNoOfOrders-2': 4, 'BestSellRate-2': 87.85, 'BestSellQty-2': 100, 'SellNoOfOrders-2': 2}, {'BestBuyRate-3': 87.2, 'BestBuyQty-3': 520, 'BuyNoOfOrders-3': 2, 'BestSellRate-3': 87.9, 'BestSellQty-3': 500, 'SellNoOfOrders-3': 3}, {'BestBuyRate-4': 87.05, 'BestBuyQty-4': 20, 'BuyNoOfOrders-4': 1, 'BestSellRate-4': 88, 'BestSellQty-4': 100, 'SellNoOfOrders-4': 2}, {'BestBuyRate-5': 86.9, 'BestBuyQty-5': 80, 'BuyNoOfOrders-5': 1, 'BestSellRate-5': 88.1, 'BestSellQty-5': 200, 'SellNoOfOrders-5': 2}], 'quotes': 'Market Depth'}
Ticks: {'symbol': '8.2!844663', 'time': 'Wed Feb 12 12:49:50 2025', 'depth': [{'BestBuyRate-1': 87.3, 'BestBuyQty-1': 20, 'BuyNoOfOrders-1': 1, 'BestSellRate-1': 87.8, 'BestSellQty-1': 20, 'SellNoOfOrders-1': 1}, {'BestBuyRate-2': 87.25, 'BestBuyQty-2': 480, 'BuyNoOfOrders-2': 4, 'BestSellRate-2': 87.85, 'BestSellQty-2': 100, 'SellNoOfOrders-2': 2}, {'BestBuyRate-3': 87.2, 'BestBuyQty-3': 520, 'BuyNoOfOrders-3': 2, 'BestSellRate-3': 87.9, 'BestSellQty-3': 500, 'SellNoOfOrders-3': 3}, {'BestBuyRate-4': 87.05, 'BestBuyQty-4': 20, 'BuyNoOfOrders-4': 1, 'BestSellRate-4': 88, 'BestSellQty-4': 100, 'SellNoOfOrders-4': 2}, {'BestBuyRate-5': 86.9, 'BestBuyQty-5': 80, 'BuyNoOfOrders-5': 1, 'BestSellRate-5': 88.1, 'BestSellQty-5': 200, 'SellNoOfOrders-5': 2}], 'quotes': 'Market Depth'}

```
</details>
<h4> NOTE : </h4>
<p>For unsubscribe : breeze.unsubscribe_feeds(exchange_code= "BFO", 
                  stock_code="BSESEN", 
                  expiry_date="18-Feb-2025", 
                  strike_price="78200", 
                  right="call", 
                  product_type="options", 
                  get_market_depth=True ,
                  get_exchange_quotes=False )</p>

<h2>Subscribe oneclick strategy stream</h2>

```python 
breeze.subscribe_feeds(stock_token="one_click_fno")
```
<br>

<details>
  <summary><b>View Response</b></summary>

```json
Ticks: {'strategy_date': '2025-02-07 14:29:29', 'modification_date': '2025-02-07 14:29:29', 'portfolio_id': '133444', 'call_action': 'Call Initiated', 'portfolio_name': 'Index Long Call', 'exchange_code': 'NFO', 'product_type': 'options', 'underlying': 'NIFTY ', 'expiry_date': '2025-02-13 00:00:00', 'option_type': 'call', 'strike_price': '23450', 'action': 'buy', 'recommended_price_from': '175', 'recommended_price_to': '178', 'minimum_lot_quantity': '75', 'last_traded_price': '181.45', 'best_bid_price': '181.5', 'best_offer_price': '181.9', 'last_traded_quantity': '23461.65', 'target_price': '240', 'expected_profit_per_lot': '4762.5', 'stop_loss_price': '144.9', 'expected_loss_per_lot': '2370', 'total_margin': '13350', 'leg_no': '1', 'status': 'active'}
Ticks: {'strategy_date': '2025-02-07 14:43:07', 'modification_date': '2025-02-07 14:43:07', 'portfolio_id': '133451', 'call_action': 'Call Initiated', 'portfolio_name': 'Weekly Future Short', 'exchange_code': 'NFO', 'product_type': 'futures', 'underlying': 'INFEDG', 'expiry_date': '2025-02-27 00:00:00', 'option_type': 'others', 'strike_price': '0', 'action': 'sell', 'recommended_price_from': '7830', 'recommended_price_to': '7860', 'minimum_lot_quantity': '75', 'last_traded_price': '7826.45', 'best_bid_price': '7825.4', 'best_offer_price': '7831', 'last_traded_quantity': '7806.65', 'target_price': '7400', 'expected_profit_per_lot': '33375', 'stop_loss_price': '8100.1', 'expected_loss_per_lot': '19132.5', 'total_margin': '133131.2', 'leg_no': '1', 'status': 'active'}

```
</details>
<h4> NOTE : </h4>
<p>For unsubscribe : breeze.unsubscribe_feeds(stock_token = "one_click_fno")</p>

<h2>Subscribe oneclick equity strategy stream(i_click_2_gain)</h2>

```python
breeze.subscribe_feeds(stock_token="i_click_2_gain") 
```
<br>

<details>
  <summary><b>View Response</b></summary>

```json
{'message': 'i_click_2_gain streaming subscribed successfully.'}
Tick Data: {'stock_name': 'MAHINDRA & MAHINDRA LIMITED(MAHMAH)Margin-Buy', 'stock_code': 'MAHMAH', 'action_type': 'buy', 'expiry_date': '', 'strike_price': '', 'option_type': '', 'stock_description': 'Margin', 'recommended_price_and_date': '3065-3068,2025-01-02 08:55:02', 'recommended_price_from': '3065', 'recommended_price_to': '3068', 'recommended_date': '2025-01-02 08:55:02', 'target_price': '3098', 'sltp_price': '3050', 'part_profit_percentage': '0,0', 'profit_price': '0', 'exit_price': '0', 'recommended_update': '     ', 'iclick_status': 'open', 'subscription_type': 'iclick_2_gain                 '}
Tick Data: {'stock_name': 'POWER FINANCE CORPORATION LTD(POWFIN)Margin-Buy', 'stock_code': 'POWFIN', 'action_type': 'buy', 'expiry_date': '', 'strike_price': '', 'option_type': '', 'stock_description': 'Margin', 'recommended_price_and_date': '450-451,2025-01-02 09:37:01', 'recommended_price_from': '450', 'recommended_price_to': '451', 'recommended_date': '2025-01-02 09:37:01', 'target_price': '456', 'sltp_price': '447', 'part_profit_percentage': '0,0', 'profit_price': '0', 'exit_price': '0', 'recommended_update': '     ', 'iclick_status': 'open', 'subscription_type': 'iclick_2_gain'}

```
</details>
<h4> NOTE : </h4>
<p>For unsubscribe : breeze.unsubscribe_feeds(stock_token = "i_click_2_gain")</p>

<br>
<hr>
<h3> ADDITIONAL NOTES </h3>
<hr>
<ol>
<li>Examples for stock_token are "4.1!38071" or "1.1!500780".</li>
<li>Template for stock_token : X.Y! 
    <ul>
    <li>X : exchange code </li>
    <li>Y : Market Level data </li>
    <li>Token : ISEC stock code</li>
    </ul>
        
<li>Value of X can be : 
    <ul>
        <li> 1 for BSE </li>
        <li> 4 for NSE</li> 
        <li> 13 for NDX </li>
        <li> 6 for MCX </li>
        <li> 4 for NFO </li></ul>
</li>      
<li>Value of Y can be : 
    <ul>
        <li> 1 for Exchange Quote data </li>
        <li> 2 for Market Depth data </li></ul></li>
<li>Token number can be obtained via get_names() function or downloading master security file via 
    https://api.icicidirect.com/breezeapi/documents/index.html#instruments</li>
<li>Exchange_code must be 
    <ul>
        <li>BSE </li>
        <li>NSE</li> 
        <li>NDX </li>
        <li>MCX </li>
        <li>NFO </li>
      </ul>
</li>
<li>Stock Code Validation: The stock_code field cannot be left empty. Valid examples include "WIPRO" or "ZEEENT".</li>
<li>Product_type Requirements: Acceptable values are 'Futures', 'Options', or a non-empty string. For exchanges NDX, MCX, and NFO, this field must not be left empty.
</li>
<li>Expiry_date Format: Should be in DD-MMM-YYYY format (e.g., 01-Jan-2022), and cannot be empty for NDX, MCX, or NFO exchanges.</li>
<li>Strike_price Format: Must be a float value represented as a string or remain empty. For Options under product_type, this field must not be empty.</li>
<li>Right Field Requirements: Acceptable values are 'Put', 'Call', or an empty string. For Options, this field cannot be left empty.</li>
<li>get_exchange_quotes and get_market_depth Validation: At least one must be set to True. Both can be True, but both cannot be False.
</li>
<li>OHLCV Streaming Interval: The interval field cannot be empty and must be one of the following values: "1second", "1minute", "5minute", or "30minute".</li>

</ol>
<br>
<hr>

<h4 id="apiusage"> API Usage</h4>

```python
from breeze_connect import BreezeConnect

# Initialize SDK
breeze = BreezeConnect(api_key="your_api_key")

# Obtain your session key from https://api.icicidirect.com/apiuser/login?api_key=YOUR_API_KEY
# Incase your api-key has special characters(like +,=,!) then encode the api key before using in the url as shown below.
import urllib
print("https://api.icicidirect.com/apiuser/login?api_key="+urllib.parse.quote_plus("your_api_key"))

# Generate Session
breeze.generate_session(api_secret="your_secret_key",
                        session_token="your_api_session")

# Generate ISO8601 Date/DateTime String
import datetime
iso_date_string = datetime.datetime.strptime("28/02/2021","%d/%m/%Y").isoformat()[:10] + 'T05:30:00.000Z'
iso_date_time_string = datetime.datetime.strptime("28/02/2021 23:59:59","%d/%m/%Y %H:%M:%S").isoformat()[:19] + '.000Z'
```
<br>

<hr>
<h2> List of other APIs:</h2>

<h3 id="index_title" >Index</h3>

<div class="sticky" id="index">
<ul>
 <li><a href="#customer_detail">get_customer_details</a></li>
 <li><a href="#demat_holding">get_demat_holdings</a></li>
 <li><a href="#get_funds">get_funds</a></li>
 <li><a href="#set_funds">set_funds</a></li>
 <li><a href="#historical_data1">get_historical_data</a></li>
 <li><a href="#historical_data_v21">get_historical_data_v2</a></li>
 <li><a href="#add_margin">add_margin</a></li>
 <li><a href="#get_margin">get_margin</a></li>
 <li><a href="#place_order">place_order</a></li>
 <li><a href="#order_detail">order_detail</a></li>
 <li><a href="#order_list">order_list</a></li>
 <li><a href="#cancel_order">cancel_order</a></li>
 <li><a href="#modify_order">modify_order</a></li>
 <li><a href="#portfolio_holding">get_portfolio_holding</a></li>
 <li><a href="#portfolio_position">get_portfolio_position</a></li>
 <li><a href="#get_quotes">get_quotes</a></li>
 <li><a href="#get_option_chain">get_option_chain_quotes</a></li>
 <li><a href="#square_off2">square_off</a></li>
 <li><a href="#trade_list">get_trade_list</a></li>
 <li><a href="#trade_detail">get_trade_detail</a></li>
 <li><a href="#get_names"> get_names </a></li>
 <li><a href="#preview_order"> preview_order </a></li>
 <li><a href="#limit_calculator"> limit_calculator </a></li>
 <li><a href="#margin_calculator"> margin_calculator </a></li>
 <li><a href="#gtt_three_leg_place_order"> gtt_three_leg_place_order </a></li>
 <li><a href="#gtt_three_leg_modify_order"> gtt_three_leg_modify_order </a></li>
 <li><a href="#gtt_three_leg_cancel_order"> gtt_three_leg_cancel_order </a></li>
 <li><a href="#gtt_order_book"> gtt_order_book </a></li>
 <li><a href="#gtt_single_leg_place_order"> gtt_single_leg_place_order </a></li>
 <li><a href="#gtt_single_leg_modify_order"> gtt_single_leg_modify_order </a></li>
 <li><a href="#gtt_single_leg_cancel_order"> gtt_single_leg_cancel_order </a></li>

 <!--<li><a href="#limit_calculator"> limit calculator </a></li>-->
</ul>
</div>

<br>
<h3 id="customer_detail" >Get Customer details by api-session value</h3>

```python
breeze.get_customer_details(api_session="your_api_session") 
```
<br>

<!-- ### API Response: -->
<details>
  <summary><b>View API Response</b></summary>

  ```json
  {'Success': 
      {'exg_trade_date': {'NSE': '04-Feb-2025',
                          'BSE': '04-Feb-2025',
                          'FNO': '04-Feb-2025',
                          'NDX': '04-Feb-2025'},
    'exg_status': {'NSE': 'C', 'BSE': 'C', 'FNO': 'Y', 'NDX': 'C'},
    'segments_allowed': {'Trading': 'Y',
                        'Equity': 'Y',
                        'Derivatives': 'Y',
                        'Currency': 'N'},
    'idirect_userid': 'XY123456',
    'idirect_user_name': 'John Smith',
    'idirect_ORD_TYP': 'N',
    'idirect_lastlogin_time': '04-Feb-2025 08:52:03',
    'mf_holding_mode_popup_flg': 'N',
    'commodity_exchange_status': 'N',
    'commodity_trade_date': '04-Feb-2025',
    'commodity_allowed': 'C'},
  'Status': 200,
  'Error': None
 }

  ```
</details>

<br>
<a href="#index">Back to Index</a> 
<hr>


<h3 id="demat_holding">Get Demat Holding details</h3>

```python
breeze.get_demat_holdings()
```
<br>

<details>
  <summary><b>View API Response</b></summary>

  ```json
  {'Success': 
    [{'stock_code': 'UNITEC',
    'stock_ISIN': 'INE694A01020',
    'quantity': '1',
    'demat_total_bulk_quantity': '1',
    'demat_avail_quantity': '0',
    'blocked_quantity': '0',
    'demat_allocated_quantity': '1'
    }],
 'Status': 200,
 'Error': None}

  ```
</details>

<br>
<a href="#index">Back to Index</a>
<hr>


<h3 id="get_funds">Get Funds</h3>


```python
breeze.get_funds()
```
<br>

<details>
  <summary><b>View API Response</b></summary>

  ```json
  {'Success': 
    {'bank_account': '123456789012',
    'total_bank_balance': 800000000.0,
    'allocated_equity': 200000000.0,
    'allocated_fno': 200000000.0,
    'allocated_commodity': 200000000.0,
    'allocated_currency': 200000000.0,
    'block_by_trade_equity': 0.0,
    'block_by_trade_fno': 12500000.53,
    'block_by_trade_commodity': 0.0,
    'block_by_trade_currency': 0.0,
    'block_by_trade_balance': 15500000,
    'unallocated_balance': '87500000'},
 'Status': 200,
 'Error': None}

  ```
</details>

<br>
<a href="#index">Back to Index</a>
<hr>

<h3 id="set_funds">Set Funds</h3>

```python
breeze.set_funds(transaction_type="debit", 
                    amount="200",
                    segment="Equity")
```
<br>

<details>
  <summary><b>View API Response</b></summary>

  ```json
  {'Success': {'status': 'Success'},
         'Status': 200, 'Error': None}

  ```
</details>

<h4> NOTE: </h4>
<p> <ol> <li>For adding fund, transaction_type="credit", amount="200", segment="Equity".</li>
       <li>Segment can be Equity, FNO, Commodity </li> </ol></p>
<a href="#index">Back to Index</a>
<hr>


<h3 id="historical_data1">Historical Data : Futures</h3>


```python
breeze.get_historical_data(interval="1minute",
                  from_date= "2025-02-03T09:21:00.000Z",
                  to_date= "2025-02-03T09:21:00.000Z",
                  stock_code="NIFTY",
                  exchange_code="NFO",
                  product_type="futures",
                  expiry_date="2025-02-27T07:00:00.000Z",
                  right="others",
                  strike_price="0")                    
```
<br>

<details>
  <summary><b>View API Response</b></summary>

  ```json
  {'Success': [
    {'datetime': '2025-02-03 09:21:00',
     'stock_code': 'NIFTY',
     'exchange_code': 'NFO',
     'product_type': 'Futures',
     'expiry_date': '27-FEB-25',
     'right': 'Others',
     'strike_price': '0',
     'open': '23346.6',
     'high': '23350.9',
     'low': '23338.6',
     'close': '23338.6',
     'volume': '81600',
     'open_interest': '17543475',
     'count': 6},
    {'datetime': '2025-02-03 09:22:00',
     'stock_code': 'NIFTY',
     'exchange_code': 'NFO',
     'product_type': 'Futures',
     'expiry_date': '27-FEB-25',
     'right': 'Others',
     'strike_price': '0',
     'open': '23338.3',
     'high': '23347.95',
     'low': '23337.1',
     'close': '23342',
     'volume': '56025',
     'open_interest': '17543475',
     'count': 7}],
 'Status': 200,
 'Error': None}

  ```
</details>
<br>
<a href="#index">Back to Index</a>
<hr>

<h3 id="historical_data2">Historical Data : Equity</h3>

```python
breeze.get_historical_data(interval="1minute",
                  from_date= "2025-02-03T09:20:00.000Z",
                  to_date= "2025-02-03T09:22:00.000Z",
                  stock_code="RELIND",
                  exchange_code="NSE",
                  product_type="cash")
```
<br>

<details>
  <summary><b>View API Response</b></summary>

  ```json
  {'Success': [
    {'datetime': '2025-02-03 09:21:00',
   'stock_code': 'RELIND',
   'exchange_code': 'NSE',
   'product_type': None,
   'expiry_date': None,
   'right': None,
   'strike_price': None,
   'open': '1249.85',
   'high': '1250.75',
   'low': '1248.95',
   'close': '1249.95',
   'volume': '1951',
   'open_interest': None,
   'count': 7},
  {'datetime': '2025-02-03 09:22:00',
   'stock_code': 'RELIND',
   'exchange_code': 'NSE',
   'product_type': None,
   'expiry_date': None,
   'right': None,
   'strike_price': None,
   'open': '1249.75',
   'high': '1250.5',
   'low': '1247.95',
   'close': '1249',
   'volume': '1810',
   'open_interest': None,
   'count': 8}],
 'Status': 200,
 'Error': None}

  ```
</details>

<br>
<a href="#index">Back to Index</a>

<hr>

<h3 id="historical_data3">Historical Data : Options</h3>

```python
breeze.get_historical_data(interval="1minute",
                  from_date= "2025-02-03T09:20:00.000Z",
                  to_date= "2025-02-03T09:22:00.000Z",
                  stock_code="NIFTY",
                  exchange_code="NFO",
                  product_type="options",
                  expiry_date="2025-02-06T07:00:00.000Z",
                  right="call",
                  strike_price="23200")
```
<br>

<details>
  <summary><b>View API Response</b></summary>

  ```json
  {'Success': [
    {'datetime': '2025-02-03 09:21:00',
      'stock_code': 'NIFTY',
      'exchange_code': 'NFO',
      'product_type': 'Options',
      'expiry_date': '06-FEB-25',
      'right': 'Call',
      'strike_price': '23200',
      'open': '201.15',
      'high': '203.9',
      'low': '195.5',
      'close': '197.55',
      'volume': '304575',
      'open_interest': '2435175',
      'count': 6},
    {'datetime': '2025-02-03 09:22:00',
      'stock_code': 'NIFTY',
      'exchange_code': 'NFO',
      'product_type': 'Options',
      'expiry_date': '06-FEB-25',
      'right': 'Call',
      'strike_price': '23200',
      'open': '196.85',
      'high': '201.8',
      'low': '196.5',
      'close': '200.3',
      'volume': '249000',
      'open_interest': '2435175',
      'count': 7}],
 'Status': 200,
 'Error': None}

  ```
</details>
<h4> NOTE: </h4>
<p>  Get Historical Data for specific stock-code by mentioned interval either as "1minute", "5minute", "30minute" or as "1day"</p>
<a href="#index">Back to Index</a>
<hr>

<h3 id="historical_data_v21">Historical Data V2 : FUTURES</h3>


```python
breeze.get_historical_data_v2(interval="1minute",
                  from_date= "2025-02-03T09:21:00.000Z",
                  to_date= "2025-02-03T09:21:00.000Z",
                  stock_code="NIFTY",
                  exchange_code="NFO",
                  product_type="futures",
                  expiry_date="2025-02-27T07:00:00.000Z",
                  right="others",
                  strike_price="0")                      
```
<br>

<details>
  <summary><b>View API Response</b></summary>

  ```json
  {'Error': None,
 'Status': 200,
 'Success': [{'close': 23338.6,
   'datetime': '2025-02-03 09:21:00',
   'exchange_code': 'NFO',
   'expiry_date': '27-FEB-2025',
   'high': 23352.15,
   'low': 23337.95,
   'open': 23348.0,
   'open_interest': 17543475,
   'product_type': 'Futures',
   'stock_code': 'NIFTY',
   'volume': 88800}]}

  ```
</details>

<h4> NOTE: </h4>
<ol><li>Product Type historical data v2 should be "futures", "options","cash"</li>
                 <li>Interval should be "1minute", "5minute", "30minute" or "1day"</li></ol>

<a href="#index">Back to Index</a>

<hr>

<h3 id="historical_data_v22">Histroical Data V2 : EQUITY</h3>


```python
breeze.get_historical_data_v2(interval="1minute",
                    from_date= "2025-02-03T09:20:00.000Z",
                    to_date= "2025-02-03T09:22:00.000Z",
                    stock_code="RELIND",
                    exchange_code="NSE",
                    product_type="cash")
```
<br>

<details>
  <summary><b>View API Response</b></summary>

  ```json
  {'Error': None,
 'Status': 200,
 'Success': [{'close': 1250.0,
   'datetime': '2025-02-03 09:20:00',
   'exchange_code': 'NSE',
   'high': 1250.9,
   'low': 1248.2,
   'open': 1248.2,
   'stock_code': 'RELIND',
   'volume': 47317},
  {'close': 1249.15,
   'datetime': '2025-02-03 09:21:00',
   'exchange_code': 'NSE',
   'high': 1250.5,
   'low': 1248.95,
   'open': 1250.0,
   'stock_code': 'RELIND',
   'volume': 54277},
  {'close': 1248.9,
   'datetime': '2025-02-03 09:22:00',
   'exchange_code': 'NSE',
   'high': 1249.7,
   'low': 1247.95,
   'open': 1248.95,
   'stock_code': 'RELIND',
   'volume': 38527}]}

  ```
</details>
<br>
<a href="#index">Back to Index</a>

<hr>

<h3 id="historical_data_v23">Histroical Data V2 : OPTIONS</h3>


```python

breeze.get_historical_data_v2(interval="1minute",
                    from_date= "2025-02-03T09:20:00.000Z",
                    to_date= "2025-02-03T09:21:00.000Z",
                    stock_code="NIFTY",
                    exchange_code="NFO",
                    product_type="options",
                    expiry_date="2025-02-06T07:00:00.000Z",
                    right="call",
                    strike_price="23200")
```
<br>
<details>
  <summary><b>View API Response</b></summary>

  ```json
  {'Error': None,
 'Status': 200,
 'Success': [{'close': 201.85,
   'datetime': '2025-02-03 09:20:00',
   'exchange_code': 'NFO',
   'expiry_date': '06-FEB-2025',
   'high': 208.1,
   'low': 201.8,
   'open': 206.75,
   'open_interest': 2203575,
   'product_type': 'Options',
   'right': 'Call',
   'stock_code': 'NIFTY',
   'strike_price': 23200.0,
   'volume': 207825},
  {'close': 197.55,
   'datetime': '2025-02-03 09:21:00',
   'exchange_code': 'NFO',
   'expiry_date': '06-FEB-2025',
   'high': 203.9,
   'low': 195.5,
   'open': 200.45,
   'open_interest': 2435175,
   'product_type': 'Options',
   'right': 'Call',
   'stock_code': 'NIFTY',
   'strike_price': 23200.0,
   'volume': 342450}]}

  ```
</details>

<h4> NOTE: </h4>
<p>
<ol> <li>Get Historical Data (version 2) for specific stock-code by mentioning interval either as "1second","1minute", "5minute", "30minute" or as "1day".</li>
       <li>Maximum candle intervals in one single request is 1000 </li> </ol>
 </p>
<br>
<a href="#index">Back to Index</a>
<hr>


<h3 id="add_margin">Add Margin</h3>


```python
breeze.add_margin(product_type="margin", 
                    stock_code="ICIBAN", 
                    exchange_code="BSE", 
                    settlement_id="2021220", 
                    add_amount="100", 
                    margin_amount="3817.10", 
                    open_quantity="10", 
                    cover_quantity="0", 
                    category_index_per_stock="", 
                    expiry_date="", 
                    right="", 
                    contract_tag="", 
                    strike_price="", 
                    segment_code="")
```
<!-- <details>
  <summary><b>View API Response</b></summary>

  ```json

  ```
</details> -->

<br>
<a href="#index">Back to Index</a>
<hr>

<h3 id="get_margin">Get Margin of your account.</h3>


```python
breeze.get_margin(exchange_code="NSE")
```
<br>

<details>
  <summary><b>View API Response</b></summary>

  ```json
  {'Success': {'limit_list': [],
  'cash_limit': 1000000.00,
  'amount_allocated': 100000.00,
  'block_by_trade': 0.0,
  'isec_margin': 0.0},
 'Status': 200,
 'Error': None}

  ```
</details>

<h4> NOTE: </h4>
<p> <ol><li>  Please change exchange_code=“NFO” to get F&O margin details </ol></li></p>
<br>
<a href="#index">Back to Index</a>
<hr>

<h3 id="place_order">Place Order : FUTURES</h3>


```python
breeze.place_order(stock_code="NIFTY",
                  exchange_code="NFO",
                  product="futures",
                  action="buy",
                  order_type="limit",
                  stoploss="0",
                  quantity="75",
                  price="23700",
                  validity="day",
                  validity_date="2022-08-22T06:00:00.000Z",
                  disclosed_quantity="0",
                  expiry_date="2025-02-27T06:00:00.000Z",
                  right="others",
                  strike_price="0",
                  user_remark="Test")
```    
<br>

<details>
  <summary><b>View API Response</b></summary>

  ```json
  {'Success': 
 {'order_id': '202502051400001234',
  'message': 'Successfully Placed the order',
  'user_remark': ''},
 'Status': 200,
 'Error': None}

  ```
</details>

<h4> NOTE: </h4>
<p><ol><li>Order Type should be either "limit" or "market"</li></ol></p>
<a href="#index">Back to Index</a>

<hr>

<h3 id="place_order2">Place Order : OPTIONS</h3>


```python 
breeze.place_order(stock_code="NIFTY",
                  exchange_code="NFO",
                  product="options",
                  action="buy",
                  order_type="limit",
                  stoploss="",
                  quantity="75",
                  price="0.20",
                  validity="day",
                  validity_date="2025-02-05T06:00:00.000Z",
                  disclosed_quantity="0",
                  expiry_date="2025-02-27T06:00:00.000Z",
                  right="call",
                  strike_price="24800")
```
<br>

<details>
  <summary><b>View API Response</b></summary>

  ```json
  {'Success': {'order_id': '202502051400001234',
  'message': 'Successfully Placed the order',
  'user_remark': ''},
 'Status': 200,
 'Error': None}

  ```
</details>

<h4> NOTE: </h4>
<p><ol><li>Order Type should be either "limit" or "market"</li></ol></p>

<br>
<a href="#index">Back to Index</a>

<hr>

<h3 id="place_order3">Place Order : EQUITY</h3>


```python
breeze.place_order(stock_code="ITC",
                    exchange_code="NSE",
                    product="cash",
                    action="buy",
                    order_type="limit",
                    stoploss="",
                    quantity="1",
                    price="420",
                    validity="day"
                )
```  

<br>
<details>
  <summary><b>View API Response</b></summary>

  ```json
  {'Success': 
 {'order_id': '20250205N30001234',
  'message': 'Equity CASH Order placed successfully through RI reference no 20250205N300001234',
  'user_remark': None},
 'Status': 200,
 'Error': None}

  ```
</details>

<br>
<a href="#index">Back to Index</a>

<!-- <h3 id="place_order4">Place an optionplus order</h3>

```python

breeze.place_order(stock_code="NIFTY",
                    exchange_code="NFO",
                    product="optionplus",
                    action="buy",
                    order_type="limit",
                    stoploss="15",
                    quantity="50",
                    price="11.25",
                    validity="day",
                    validity_date="2022-12-02T06:00:00.000Z",
                    disclosed_quantity="0",
                    expiry_date="2022-12-08T06:00:00.000Z",
                    right="call",
                    strike_price="19000",
                    order_type_fresh = "Limit",
                    order_rate_fresh = "20",
                    user_remark="Test")
```                
<br>
<details>
  <summary><b>View API Response</b></summary>

  ```json

  ```
</details>

<br>
<a href="#index">Back to Index</a>

<h3> Place btst order </h3>

```python

breeze.place_order(stock_code = "RELIND",
    exchange_code= "NSE",
    product = "btst",
    action = "buy",
    order_type = "limit",
    quantity = "1",
    price = "2450",
    validity = "day",
    stoploss  = "",
    order_type_fresh = "",
    order_rate_fresh = "",
    validity_date = "",
    disclosed_quantity = "",
    expiry_date =  "",
    right = "",
    strike_price = "",
    user_remark = "",
    settlement_id = "2023008",
    order_segment_code = "N")

```
<br>
<details>
  <summary><b>View API Response</b></summary>

  ```json

  ```
</details>

<br> -->
<!-- <a href="#index">Back to Index</a> -->

<hr>

<h3 id="order_detail">Get order detail</h3>

```python
breeze.get_order_detail(exchange_code="NSE",
                        order_id="20250205N300001234")
```
<br>

<details>
  <summary><b>View API Response</b></summary>

  ```json
  {'Success': [
    {'order_id': '20250205N300001234',
   'exchange_order_id': None,
   'exchange_code': 'NSE',
   'stock_code': 'ITC',
   'product_type': 'Cash',
   'action': 'Buy',
   'order_type': 'Limit',
   'stoploss': '0.00',
   'quantity': '1',
   'price': '420.00',
   'validity': 'Day',
   'disclosed_quantity': '0',
   'expiry_date': None,
   'right': None,
   'strike_price': 0.0,
   'average_price': '0',
   'cancelled_quantity': '0',
   'pending_quantity': '1',
   'status': 'Ordered',
   'user_remark': '',
   'order_datetime': '05-Feb-2025 09:26',
   'parent_order_id': None,
   'modification_number': None,
   'exchange_acknowledgement_date': None,
   'SLTP_price': None,
   'exchange_acknowledge_number': None,
   'initial_limit': None,
   'intial_sltp': None,
   'LTP': None,
   'limit_offset': None,
   'mbc_flag': None,
   'cutoff_price': None,
   'validity_date': ''}],
 'Status': 200,
 'Error': None}

  ```
</details>

<h4> NOTE: </h4>
<p> <ol><li> Please change exchange_code=“NFO” to get details about F&O </li></ol></p>
<a href="#index">Back to Index</a>
<hr>

<h3 id="order_list">Get order list</h3>


```python
breeze.get_order_list(exchange_code="NSE",
                      from_date="2025-02-05T10:00:00.000Z",
                      to_date="2025-02-05T10:00:00.000Z")
```
<br>

<details>
  <summary><b>View API Response</b></summary>

  ```json
  {'Success': [
    {'order_id': '20250205N300001234',
   'exchange_order_id': None,
   'exchange_code': 'NSE',
   'stock_code': 'ITC',
   'product_type': 'Cash',
   'action': 'Buy',
   'order_type': 'Limit',
   'stoploss': '0.00',
   'quantity': '1',
   'price': '420.00',
   'validity': 'Day',
   'disclosed_quantity': '0',
   'expiry_date': None,
   'right': None,
   'strike_price': 0.0,
   'average_price': '0',
   'cancelled_quantity': '0',
   'pending_quantity': '1',
   'status': 'Ordered',
   'user_remark': '',
   'order_datetime': '05-Feb-2025 09:26',
   'parent_order_id': None,
   'modification_number': None,
   'exchange_acknowledgement_date': None,
   'SLTP_price': None,
   'exchange_acknowledge_number': None,
   'initial_limit': None,
   'intial_sltp': None,
   'LTP': None,
   'limit_offset': None,
   'mbc_flag': None,
   'cutoff_price': None,
   'validity_date': ''}],
 'Status': 200,
 'Error': None}

  ```
</details>

<h4> NOTE: </h4>
<p> <ol><li> Please change exchange_code=“NFO” to get details about F&O </li></ol></p>

<a href="#index">Back to Index</a>
<hr>


<h3 id="cancel_order">Cancel order</h3> 


```python
breeze.cancel_order(exchange_code="NSE",
                    order_id="20250205N300001234")
```  
<br>

<details>
  <summary><b>View API Response</b></summary>

  ```json
  {'Success': 
{'order_id': '20250205N300001234',
'message': 'Your Order Canceled successfully.'},
'Status': 200,
'Error': None}

  ```
</details>

<br>
<a href="#index">Back to Index</a>
<hr>

<h3 id="modify_order">Modify order</h3> 


```python
breeze.modify_order(order_id="202502051400012345",
                    exchange_code="NFO",
                    order_type="limit",
                    stoploss="0",
                    quantity="75",
                    price="0.30",
                    validity="day",
                    disclosed_quantity="0",
                    validity_date="2025-08-22T06:00:00.000Z")
```
<br>

<details>
  <summary><b>View API Response</b></summary>

  ```json
  {'Success': 
 {'message': 'Successfully Modified the order',
  'order_id': '202502051400012345'},
 'Status': 200,
 'Error': None}

  ```
</details>

<br>
<a href="#index">Back to Index</a>
<hr>

<h3 id="portfolio_holding">Get Portfolio Holdings</h3>


```python
breeze.get_portfolio_holdings(exchange_code="NFO",
                    from_date="2024-08-01T06:00:00.000Z", 
                    to_date="2024-09-19T06:00:00.000Z", 
                    stock_code="", 
                    portfolio_type="")
```
<br>

<details>
  <summary><b>View API Response</b></summary>

  ```json
  {'Success':[
{'stock_code': 'NIFTY',
'exchange_code': 'NFO',
'quantity': '0',
'average_price': '0',
'booked_profit_loss': None,
'current_market_price': '0',
'change_percentage': None,
'answer_flag': None,
'product_type': 'Options',
'expiry_date': '01-Aug-2024',
'strike_price': '25200',
'right': 'Call',
'category_index_per_stock':'I',
'action': 'NA',
'realized_profit': '-349.26',
'unrealized_profit': '0',
'open_position_value': '0',
'portfolio_charges': '5.51'}],
'Status': 200,
'Error': None}
  ```
</details>

<h4> NOTE: </h4>
<p> <ol><li>Please change exchange_code=“NSE” to get Equity Portfolio Holdings</li></ol></p>
<a href="#index">Back to Index</a>
<hr>

<h3 id="portfolio_position">Get Portfolio Positions</h3>


```python
breeze.get_portfolio_positions()
```
<br>

<details>
  <summary><b>View API Response</b></summary>

  ```json
  {'Success': [{'segment': 'fno',
   'product_type': 'Options',
   'exchange_code': 'NFO',
   'stock_code': 'NIFTY',
   'expiry_date': '27-Feb-2025',
   'strike_price': '24800',
   'right': 'Call',
   'action': 'NA',
   'quantity': '0',
   'average_price': '0',
   'settlement_id': None,
   'margin_amount': None,
   'ltp': '29.95',
   'price': '28.85',
   'stock_index_indicator': 'Index',
   'cover_quantity': '0',
   'stoploss_trigger': '0',
   'stoploss': None,
   'take_profit': None,
   'available_margin': None,
   'squareoff_mode': None,
   'mtf_sell_quantity': None,
   'mtf_net_amount_payable': None,
   'mtf_expiry_date': None,
   'order_id': '',
   'cover_order_flow': None,
   'cover_order_executed_quantity': None,
   'pledge_status': None,
   'pnl': None,
   'underlying': 'NIFTY',
   'order_segment_code': None}],
 'Status': 200,
 'Error': None}

  ```
</details>

<br>
<a href="#index">Back to Index</a>
<hr>

<h3 id="get_quotes">Get quotes</h3>


```python
breeze.get_quotes(stock_code="NIFTY",
                    exchange_code="NFO",
                    expiry_date="2025-02-27T06:00:00.000Z",
                    product_type="futures",
                    right="others",
                    strike_price="0")
```

<br>
<details>
  <summary><b>View API Response</b></summary>

  ```json
  {'Success': [{'exchange_code': 'NFO',
   'product_type': 'Future',
   'stock_code': 'NIFTY',
   'expiry_date': '27-Feb-2025',
   'right': '*',
   'strike_price': 0.0,
   'ltp': 23832.85,
   'ltt': '05-Feb-2025 09:36:56',
   'best_bid_price': 23832.0,
   'best_bid_quantity': '1500',
   'best_offer_price': 23833.8,
   'best_offer_quantity': '150',
   'open': 23825.0,
   'high': 23840.6,
   'low': 23808.0,
   'previous_close': 23785.4,
   'ltp_percent_change': 0.2,
   'upper_circuit': 26163.95,
   'lower_circuit': 21406.9,
   'total_quantity_traded': '623325',
   'spot_price': '23783.7'}],
 'Status': 200,
 'Error': None}

  ```
</details>

<h4> NOTE: </h4>
<p><ol><li>For equity, 
exchange_code = "NSE", expiry_date = "", product_type = "cash", right="", 
strike_price=""</li>
       <li>For options, 
exchange_code = "NFO", expiry_date = "27-Feb-2025", 
product_type = "options", right="call/put", strike_price="24000" </li> </ol>
</p>
<a href="#index">Back to Index</a>
<hr>

<h3 id="get_option_chain">Get option chain quotes</h3>


```python
breeze.get_option_chain_quotes(stock_code="ICIBAN",
                    exchange_code="NFO",
                    product_type="futures",
                    expiry_date="2025-01-25T06:00:00.000Z")
```                    

<br>
<details>
  <summary><b>View API Response</b></summary>

  ```json
  {'Success': [{'exchange_code': 'NFO',
   'product_type': 'Options',
   'stock_code': 'NIFTY',
   'expiry_date': '06-Feb-2025',
   'right': 'Call',
   'strike_price': 17600.0,
   'ltp': 0.0,
   'ltt': '',
   'best_bid_price': 0.0,
   'best_bid_quantity': '0',
   'best_offer_price': 0.0,
   'best_offer_quantity': '0',
   'open': 0.0,
   'high': 0.0,
   'low': 0.0,
   'previous_close': 0.0,
   'ltp_percent_change': 0.0,
   'upper_circuit': 6750.4,
   'lower_circuit': 5541.8,
   'total_quantity_traded': '0',
   'spot_price': '23787',
   'ltq': '0',
   'open_interest': 0.0,
   'chnge_oi': 0.0,
   'total_buy_qty': '0',
   'total_sell_qty': '0'},
  {'exchange_code': 'NFO',
   'product_type': 'Options',
   'stock_code': 'NIFTY',
   'expiry_date': '06-Feb-2025',
   'right': 'Call',
   'strike_price': 17650.0,
   'ltp': 0.0,
   'ltt': '',
   'best_bid_price': 0.0,
   'best_bid_quantity': '0',
   'best_offer_price': 0.0,
   'best_offer_quantity': '0',
   'open': 0.0,
   'high': 0.0,
   'low': 0.0,
   'previous_close': 0.0,
   'ltp_percent_change': 0.0,
   'upper_circuit': 6700.45,
   'lower_circuit': 5491.85,
   'total_quantity_traded': '0',
   'spot_price': '23787',
   'ltq': '0',
   'open_interest': 0.0,
   'chnge_oi': 0.0,
   'total_buy_qty': '0',
   'total_sell_qty': '0'}],
 'Status': 200,
 'Error': None}

  ```
</details>

<h4> NOTE: </h4>
<p><ol><li>Get option-chain of mentioned stock-code for product-type Options where atleast 2 input is required out of expiry-date, right and strike-price</li>
    <li>Get option-chain of mentioned stock-code for product-type Futures where input of expiry-date is not compulsory</li></ol></p>


<a href="#index">Back to Index</a>

<!-- <h3 id="get_option_chain2">Get option-chain of mentioned stock-code for product-type Options where atleast 2 input is required out of expiry-date, right and strike-price</h3>


```python
breeze.get_option_chain_quotes(stock_code="ICIBAN",
                    exchange_code="NFO",
                    product_type="options",
                    expiry_date="2022-08-25T06:00:00.000Z",
                    right="call")
```

<br>
<details>
  <summary><b>View API Response</b></summary>

  ```json

  ```
</details>

<br> -->
<!-- <a href="#index">Back to Index</a> -->
<hr>

<!-- <h3 id="square_off1">Square off an Equity Margin Order</h3>

```python
breeze.square_off(exchange_code="NSE",
                    product="margin",
                    stock_code="NIFTY",
                    quantity="10",
                    price="0",
                    action="sell",
                    order_type="market",
                    validity="day",
                    stoploss="0",
                    disclosed_quantity="0",
                    protection_percentage="",
                    settlement_id="",
                    cover_quantity="",
                    open_quantity="",
                    margin_amount="")
```
<br>
<details>
  <summary><b>View API Response</b></summary>

  ```json

  ```
</details>

<br>
<p> Note: Please refer get_portfolio_positions() for settlement id and margin_amount</p> -->
<!-- <br> -->
<!-- <a href="#index">Back to Index</a> -->

<h3 id="square_off2">Sqaure Off: OPTIONS </h3>


```python
breeze.square_off(exchange_code="NFO",
                  product="options",
                  stock_code="NIFTY",
                  expiry_date="2025-02-27T06:00:00.000Z",
                  right="Call",
                  strike_price="24000",
                  action="sell",
                  order_type="market",
                  validity="day",
                  stoploss="0",
                  quantity="75",
                  price="0",
                  validity_date="2025-02-05T06:00:00.000Z",
                  trade_password="",
                  disclosed_quantity="0")
```
<br>
<details>
  <summary><b>View API Response</b></summary>

  ```json
  {'Success': 
 {'order_id': '202502052500001234',
  'message': 'Successfully Placed the order',
  'indicator': '0'},
 'Status': 200,
 'Error': None}

  ```
</details>

<br>
<!-- <h5> NOTE : </h5>
<p> <ol><li> Please refer get_portfolio_positions() for settlement id and margin_amount </li></ol></p> -->
<a href="#index">Back to Index</a>

<hr>

<h3 id="square_off3">Sqaure Off: FUTURES</h3>

```python
breeze.square_off(exchange_code="NFO",
                  product="futures",
                  stock_code="NIFTY",
                  expiry_date="2025-02-27T06:00:00.000Z",
                  action="sell",
                  order_type="market",
                  validity="day",
                  stoploss="0",
                  quantity="75",
                  price="0",
                  validity_date="2025-02-27T06:00:00.000Z",
                  trade_password="",
                  disclosed_quantity="0")
```                
<br>
<details>
  <summary><b>View API Response</b></summary>

  ```json
  {'Success': {'order_id': '202502052500001234',
  'message': 'Successfully Placed the order',
  'indicator': '0'},
 'Status': 200,
 'Error': None}

  ```
</details>

<br>
<a href="#index">Back to Index</a>
<hr>

<h3 id="trade_list">Get trade list</h3>


```python
breeze.get_trade_list(from_date="2025-02-05T06:00:00.000Z",
                        to_date="2025-02-05T06:00:00.000Z",
                        exchange_code="NSE",
                        product_type="",
                        action="",
                        stock_code="")
``` 
<br>
<details>
  <summary><b>View API Response</b></summary>

  ```json
  {'Success': [{'book_type': 'Trade-Book',
   'trade_date': '05-Feb-2025',
   'stock_code': 'ITC',
   'action': 'Buy',
   'quantity': '1',
   'average_cost': '452.20',
   'brokerage_amount': '0.00',
   'product_type': 'Margin',
   'exchange_code': 'NSE',
   'order_id': '20250205N300012345',
   'segment': 'M',
   'settlement_code': '2025027',
   'dp_id': 'IN1234566',
   'client_id': '12345678',
   'ltp': '451.95',
   'eatm_withheld_amount': '0.00',
   'cash_withheld_amount': '0.00',
   'total_taxes': '0.00',
   'order_type': 'Market',
   'expiry_date': None,
   'right': None,
   'strike_price': None},
  {'book_type': 'Trade-Book',
   'trade_date': '05-Feb-2025',
   'stock_code': 'ITC',
   'action': 'Sell',
   'quantity': '1',
   'average_cost': '452.55',
   'brokerage_amount': '0.00',
   'product_type': 'Margin',
   'exchange_code': 'NSE',
   'order_id': '20250205N300012345',
   'segment': 'M',
   'settlement_code': '2025012',
   'dp_id': 'IN1234566',
   'client_id': '12345678',
   'ltp': '451.95',
   'eatm_withheld_amount': '0.00',
   'cash_withheld_amount': '0.00',
   'total_taxes': '0.00',
   'order_type': 'Market',
   'expiry_date': None,
   'right': None,
   'strike_price': None}],
 'Status': 200,
 'Error': None}

  ```
</details>

<h4> NOTE: </h4>
<p> <ol><li> Please change exchange_code=“NFO” to get details about F&O </li></ol></p>
<a href="#index">Back to Index</a>
<hr>

<h3 id="trade_detail">Get trade detail</h3>


```python
breeze.get_trade_detail(exchange_code="NSE",
                        order_id="20250205N300012345")
```
<br>

<details>
  <summary><b>View API Response</b></summary>

  ```json
  {'Success': [{'settlement_id': '1234567',
   'exchange_trade_id': '123456789',
   'executed_quantity': '1',
   'action': 'B',
   'total_transaction_cost': '0',
   'brokerage_amount': '0',
   'taxes': '0',
   'eatm_withheld_amount': '0',
   'cash_withheld_amount': '0',
   'execution_price': '452.2',
   'stock_code': 'ITC',
   'exchange_code': 'NSE',
   'trade_id': '2025/1234/12345678',
   'exchange_trade_time': '05-Feb-2025 10:41:24'}],
 'Status': 200,
 'Error': None}

  ```
</details>

<h4> NOTE: </h4>
<p> <ol><li> Please change exchange_code=“NFO” to get details about F&O </li></ol></p>
<a href="#index">Back to Index</a>
<hr>

<!--
<h3 id = "limit_calculator"> Get Limit Value. </h3>
```python
breeze.limit_calculator(strike_price =  "19200",                                    
    product_type = "optionplus",                 
    expiry_date  = "06-JUL-2023",
    underlying = "NIFTY",
    exchange_code = "NFO",
    order_flow = "Buy",
    stop_loss_trigger = "200.00",
    option_type = "Call",
    source_flag = "P",
    limit_rate = "",
    order_reference = "",
    available_quantity = "",
    market_type = "limit",
    fresh_order_limit = "177.70")
```

<br>
<a href="#index">Back to Index</a>
<hr>
-->

<h3 id = "get_names">Get Names</h3>


```python
breeze.get_names(exchange_code = 'NSE',stock_code = 'TATASTEEL')
```
<br>

<details>
  <summary><b>View API Response</b></summary>

  ```json
  {'exchange_code': 'NSE',
 'exchange_stock_code': 'TATASTEEL',
 'isec_stock_code': 'TATSTE',
 'isec_token': '3499',
 'company name': 'TATA STEEL LIMITED',
 'isec_token_level1': '4.1!3499',
 'isec_token_level2': '4.2!3499'}

  ```
</details>

<h4> NOTE: </h4>
<p> <ol><li> Use this method to find ICICI specific stock codes / token </li></ol></p>

<a href="#index">Back to Index</a>

<hr>

<h3 id="preview_order">Preview Order</h3>


```python

breeze.preview_order(stock_code = "ITC",
            exchange_code = "NSE",
            product = "margin",
            order_type = "limit",
            price = "440",
            action = "buy",
            quantity = "1",
            specialflag = "N")
```

<br>
<details>
  <summary><b>View API Response</b></summary>

  ```json
  {'Success': {'brokerage': 0.31,
  'exchange_turnover_charges': 0.01,
  'stamp_duty': 0.07,
  'stt': 0.44,
  'sebi_charges': 0.0,
  'gst': 0.06,
  'total_turnover_and_sebi_charges': 0.01,
  'total_other_charges': 0.58,
  'total_brokerage': 0.89},
 'Status': 200,
 'Error': None}


  ```
</details>

<br>
<a href="#index">Back to Index</a>

<hr>

<h3 id="limit_calculator">Limit Calculator</h3>


```python
breeze.limit_calculator(strike_price="24000",                                    
            product_type = "optionplus",                 
            expiry_date  = "06-Feb-2025",
            underlying = "NIFTY",
            exchange_code = "NFO",
            order_flow = "Buy",
            stop_loss_trigger = "8",
            option_type = "Call",
            source_flag = "P",
            limit_rate = "7.5",
            order_reference = "",
            available_quantity = "",
            market_type = "limit",
            fresh_order_limit = "10.95")
```
<br>
<details>
  <summary><b>View API Response</b></summary>

  ```json
  {'Success': 
 {'available_quantity': '0',
  'action_id': '0',
  'order_margin': '0',
  'limit_rate': '16'},
 'Status': 200,
 'Error': None}

  ```
</details>

<br>
<a href="#index">Back to Index</a>

<hr>

<h3 id="margin_calculator">Margin Calculator</h3>


```python
breeze.margin_calculator([{
            "strike_price": "0",
            "quantity": "30",
            "right": "others",
            "product": "futures",
            "action": "buy",
            "price": "49500",
            "expiry_date": "27-Feb-2025",
            "stock_code": "CNXBAN",
            "cover_order_flow": "N",
            "fresh_order_type": "N",
            "cover_limit_rate": "0",
            "cover_sltp_price": "0",
            "fresh_limit_rate": "0",
            "open_quantity": "0"
        },
        {
            "strike_price": "50000",
            "quantity": "30",
            "right": "Call",
            "product": "options",
            "action": "buy",
            "price": "1150",
            "expiry_date": "27-Feb-2025",
            "stock_code": "CNXBAN",
            "cover_order_flow": "N",
            "fresh_order_type": "N",
            "cover_limit_rate": "0",
            "cover_sltp_price": "0",
            "fresh_limit_rate": "0",
            "open_quantity": "0"
        },
        {
            "strike_price": "0",
            "quantity": "75",
            "right": "others",
            "product": "futures",
            "action": "buy",
            "price": "23400",
            "expiry_date": "27-Feb-2025",
            "stock_code": "NIFTY",
            "cover_order_flow": "N",
            "fresh_order_type": "N",
            "cover_limit_rate": "0",
            "cover_sltp_price": "0",
            "fresh_limit_rate": "0",
            "open_quantity": "0"
        },
        {
            "strike_price": "23400",
            "quantity": "75",
            "right": "call",
            "product": "options",
            "action": "buy",
            "price": "577",
            "expiry_date": "27-Feb-2025",
            "stock_code": "NIFTY",
            "cover_order_flow": "sell",
            "fresh_order_type": "limit",
            "cover_limit_rate": "0",
            "cover_sltp_price": "0",
            "fresh_limit_rate": "0",
            "open_quantity": "0"
        }],exchange_code = "NFO")

```
<br>
<details>
  <summary><b>View API Response</b></summary>

  ```json
  {'Success': {'margin_calulation': [{'strike_price': '0',
    'quantity': '30',
    'right': 'Others',
    'product': 'Futures',
    'action': 'Buy',
    'price': '49500',
    'expiry_date': '27-Feb-2025',
    'stock_code': 'CNXBAN'},
   {'strike_price': '50000',
    'quantity': '30',
    'right': 'Call',
    'product': 'Options',
    'action': 'Buy',
    'price': '1150',
    'expiry_date': '27-Feb-2025',
    'stock_code': 'CNXBAN'},
   {'strike_price': '0',
    'quantity': '75',
    'right': 'Others',
    'product': 'Futures',
    'action': 'Buy',
    'price': '23400',
    'expiry_date': '27-Feb-2025',
    'stock_code': 'NIFTY '},
   {'strike_price': '23400',
    'quantity': '75',
    'right': 'Call',
    'product': 'Options',
    'action': 'Buy',
    'price': '577',
    'expiry_date': '27-Feb-2025',
    'stock_code': 'NIFTY '}],
  'non_span_margin_required': '0',
  'order_value': '493011.26',
  'order_margin': '0',
  'trade_margin': None,
  'block_trade_margin': '0',
  'span_margin_required': '493011.26'},
 'Status': 200,
 'Error': None}

  ```
</details>

<br>
<a href="#index">Back to Index</a>

<hr>

<h1>GTT(Good Till Trigger)</h1>

<h3 id="gtt_three_leg_place_order"> GTT Three Leg OCO(One Cancels Other) Place order </h3>


```python
breeze.gtt_three_leg_place_order(exchange_code ="NFO",
                  stock_code="NIFTY",
                  product="options",
                  quantity = "75",
                  expiry_date="2025-02-06T06:00:00.00Z",
                  right = "call",
                  strike_price = "24000",
                  gtt_type="cover_oco",
                  fresh_order_action="buy",
                  fresh_order_price="8",
                  fresh_order_type="limit",
                  index_or_stock="index",
                  trade_date="2025-02-05T06:00:00.00Z",
                  order_details=[
                    {
                      "gtt_leg_type" : "target",
                      "action" : "sell",
                      "limit_price" : "15",
                      "trigger_price" : "14.50"
                    },
                    {
                      "gtt_leg_type" : "stoploss",
                      "action" : "sell",
                      "limit_price" : "7",
                      "trigger_price" : "7.5"
                    },
                    ])
```
<br>
<details>
  <summary><b>View API Response</b></summary>

  ```json
  {'Success': 
{'gtt_order_id': '2025020500001234',
'message': 'Your GTT Order Request Placed Successfully'},
 'Status': 200,
 'Error': None}

  ```
</details>

<br>
<a href="#index">Back to Index</a>
<hr>
<h3 id="gtt_three_leg_modify_order"> GTT Three Leg Modify order </h3>


```python
breeze.gtt_three_leg_modify_order(exchange_code = "NFO",
                      gtt_order_id = "2025020500001234",
                      gtt_type ="oco",
                      order_details = [
                        {
                          "gtt_leg_type" : "target",
                          "action" : "sell",
                          "limit_price" : "12",
                          "trigger_price" : "11.50"
                        },
                        {
                          "gtt_leg_type" : "stoploss",
                          "action" : "sell",
                          "limit_price" : "4",
                          "trigger_price" : "5"
                        }])
```
<br>
<details>
  <summary><b>View API Response</b></summary>

  ```json
  {'Success': 
 {'gtt_order_id': '2025020500001234',
  'message': 'Order Modified Successfully'},
 'Status': 200,
 'Error': None}

  ```
</details>

<br>
<a href="#index">Back to Index</a>
<hr>

<h3 id="gtt_three_leg_cancel_order"> GTT Three Leg Cancel order </h3>


```python
breeze.gtt_three_leg_cancel_order(exchange_code = "NFO",
                        gtt_order_id = "2025020500001234")
```
<br>
<details>
  <summary><b>View API Response</b></summary>

  ```json
  {'Success': 
 {'gtt_order_id': '2025020500001234',
  'message': 'Your request for order cancellation successfully submitted !'},
 'Status': 200,
 'Error': None}

  ```
</details>

<br>
<a href="#index">Back to Index</a>
<hr>

<h3 id="gtt_single_leg_place_order"> GTT Single Leg Place order </h3>


```python
breeze.gtt_single_leg_place_order(exchange_code ="NFO",
                    stock_code="NIFTY",
                    product="options",
                    quantity = "75",
                    expiry_date="2025-02-06T06:00:00.00Z",
                    right = "call",
                    strike_price = "24000",
                    gtt_type="single",
                    index_or_stock="index",
                    trade_date="2025-02-05T06:00:00.00Z",
                    order_details=[
                    {
                        "action" : "buy",
                        "limit_price" : "7",
                        "trigger_price" : "8"
                    }])

```
<br>
<details>
  <summary><b>View API Response</b></summary>

  ```json
  {'Success': 
 {'gtt_order_id': '2025020500001234',
  'message': 'Your GTT Order Request Placed Successfully'},
 'Status': 200,
 'Error': None}

  ```
</details>

<br>
<a href="#index">Back to Index</a>

<hr>

<h3 id="gtt_single_leg_modify_order"> GTT Single Leg Modify order </h3>


```python
breeze.gtt_single_leg_modify_order(exchange_code="NFO",
                      gtt_order_id="2025020500001234",
                      gtt_type="single",
                      order_details=[
                        {
                          "action": "buy",
                          "limit_price": "6",
                          "trigger_price": "7"
                        }])

```
<br>
<details>
  <summary><b>View API Response</b></summary>

  ```json
  {'Success': 
 {'gtt_order_id': '2025020500001234',
  'message': 'Order Modified Successfully'},
 'Status': 200,
 'Error': None}

  ```
</details>

<br>
<a href="#index">Back to Index</a>

<hr>
<h3 id="gtt_single_leg_cancel_order"> GTT Single Leg Cancel order </h3>


```python
breeze.gtt_single_leg_cancel_order(exchange_code = "NFO",
                                   gtt_order_id = "2025011500003608")
```
<br>
<details>
  <summary><b>View API Response</b></summary>

  ```json
{'Success': 
 {'gtt_order_id': '2025020500001234',
  'message': 'Your request for order cancellation successfully submitted !'},
 'Status': 200,
 'Error': None}
  ```
</details>

<br>
<a href="#index">Back to Index</a>

<hr>

<h3 id="gtt_order_book"> OCO and Single GTT order book </h3>


```python
breeze.gtt_order_book(exchange_code ="NFO",
            from_date = "2025-02-05T06:00:00.00Z",
            to_date = "2025-02-05T06:00:00.00Z")
```
<br>
<details>
  <summary><b>View API Response</b></summary>

  ```json
  {'Success': [{'order_details': [{'gtt_leg_type': None,
     'action': 'Buy',
     'trigger_price': 7.0,
     'limit_price': 6.0,
     'status': 'Cancelled',
     'gtt_order_id': '2025020500001234'}],
   'exchange_code': 'NFO',
   'product_type': 'Options',
   'stock_code': 'NIFTY',
   'expiry_date': '06-Feb-2025',
   'strike_price': 24000.0,
   'right': 'Call',
   'quantity': 75,
   'index_or_stock': 'Index',
   'gtt_type': 'Single',
   'fresh_order_id': None,
   'order_datetime': '05-FEB-2025 11:19:32'},
  {'order_details': [{'gtt_leg_type': 'Target',
     'action': 'Sell',
     'trigger_price': 11.5,
     'limit_price': 12.0,
     'status': 'Cancelled',
     'gtt_order_id': '2025020500001234'},
    {'gtt_leg_type': 'Stoploss',
     'action': 'Sell',
     'trigger_price': 5.0,
     'limit_price': 4.0,
     'status': 'Cancelled',
     'gtt_order_id': '2025020500001234'}],
   'exchange_code': 'NFO',
   'product_type': 'Options',
   'stock_code': 'NIFTY',
   'expiry_date': '06-Feb-2025',
   'strike_price': 24000.0,
   'right': 'Call',
   'quantity': 75,
   'index_or_stock': 'Index',
   'gtt_type': 'Cover OCO',
   'fresh_order_id': '202502052500001234',
   'order_datetime': '05-FEB-2025 11:14:38'}],
 'Status': 200,
 'Error': None}

  ```
</details>

<br>
<a href="#index">Back to Index</a>

<hr>
