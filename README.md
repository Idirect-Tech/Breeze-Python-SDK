# Table Of Content

<ul>
 <li><a href="#client">Breeze API Python Client</a></li>
 <li><a href="#docslink">API Documentation</a></li>
 <li><a href="#virtualenv">Set Up Virtual Environment</a></li>
 <li><a href="#clientinstall">Installing Client</a></li>
 <li><a href="#apiusage">API Usage</a></li>
 <li><a href="#websocket">Websocket Usage</a></li>
 <li><a href="#index_title">List Of Other SDK methods</a></li>
</ul>


<h4 id="client">Breeze API Python Client</h4>

breezeapi@icicisecurities.com

The official Python client library for the ICICI Securities trading APIs. BreezeConnect is a set of REST-like APIs that allows one to build a complete investment and trading platform. Following are some notable features of Breeze APIs:

1. Execute orders in real time
2. Manage Portfolio
3. Access to 10 years of historical market data including 1 sec OHLCV
4. Streaming live OHLC (websockets)
5. Option Chain API


<h4 id="docslink">API Documentation</h4>

<div class="sticky" >
<ul>
 <li><a href="https://api.icicidirect.com/breezeapi/documents/index.html">Breeze HTTP API Documentation</a></li>
 <li><a href="https://pypi.org/project/breeze-connect/">Python client documentation</a></li>
</ul>
</div>

<h4 id="virtualenv">Setup virtual environment in your Machine</h4>

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

<h4 id="clientinstall">Installing the client</h4>

You can install the latest release via pip

```
pip install --upgrade breeze-connect
```

Or, You can also install the specific release version via pip

```
pip install breeze-connect==1.0.36
```

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

<h4 id ="websocket"> Websocket Usage</h4>

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

# subscribe stocks feeds
breeze.subscribe_feeds(exchange_code="NFO", stock_code="ZEEENT", product_type="options", expiry_date="31-Mar-2022", strike_price="350", right="Call", get_exchange_quotes=True, get_market_depth=False)

# subscribe stocks feeds by stock-token
breeze.subscribe_feeds(stock_token="1.1!500780")

# unsubscribe stocks feeds
breeze.unsubscribe_feeds(exchange_code="NFO", stock_code="ZEEENT", product_type="options", expiry_date="31-Mar-2022", strike_price="350", right="Call", get_exchange_quotes=True, get_market_depth=False)

# unsubscribe stocks feeds by stock-token
breeze.unsubscribe_feeds(stock_token="1.1!500780")

# subscribe to Real Time Streaming OHLCV Data of stocks
breeze.subscribe_feeds(exchange_code="NFO", stock_code="ZEEENT", product_type="options", expiry_date="31-Mar-2022", strike_price="350", right="Call", interval="1minute")

# subscribe to Real Time Streaming OHLCV Data of stocks by stock-token
breeze.subscribe_feeds(stock_token="1.1!500780",interval="1second")

# unsubscribe to Real Time Streaming OHLCV Data of stocks
breeze.unsubscribe_feeds(exchange_code="NFO", stock_code="ZEEENT", product_type="options", expiry_date="31-Mar-2022", strike_price="350", right="Call", interval="1minute")

# unsubscribe to Real Time Streaming OHLCV Data of stocks by stock-token
breeze.unsubscribe_feeds(stock_token="1.1!500780",interval="1second")

# subscribe order notification feeds(it will connect to order streaming server)
breeze.subscribe_feeds(get_order_notification=True)

# unsubscribe order notification feeds(also it will disconnect the order streaming server)
breeze.unsubscribe_feeds(get_order_notification=True)

# subscribe oneclick strategy stream
breeze.subscribe_feeds(stock_token = "one_click_fno")

# unsubscribe oneclick strategy stream
breeze.unsubscribe_feeds(stock_token = "one_click_fno")

# subscribe oneclick equity strategy stream(i_click_2_gain)
breeze.subscribe_feeds(stock_token = "i_click_2_gain")

# unsubscribe oneclick equity strategy stream(i_click_2_gain)
breeze.unsubscribe_feeds(stock_token = "i_click_2_gain")


# ws_disconnect (it will disconnect from all actively connected servers)
breeze.ws_disconnect()

```
<br>

---

**NOTE**

Examples for stock_token are "4.1!38071" or "1.1!500780".

Template for stock_token : X.Y!<token>
X : exchange code
Y : Market Level data
Token : ISEC stock code

Value of X can be :
1 for BSE,
4 for NSE,
13 for NDX,
6 for MCX,
4 for NFO,

Value of Y can be :
1 for Level 1 data,
4 for Level 2 data

Token number can be obtained via get_names() function or downloading master security file via 
https://api.icicidirect.com/breezeapi/documents/index.html#instruments


exchange_code must be 'BSE', 'NSE', 'NDX', 'MCX' or 'NFO'.

stock_code should not be an empty string. Examples for stock_code are "WIPRO" or "ZEEENT".

product_type can be either 'Futures', 'Options' or an empty string. 
Product_type can not be an empty string for exchange_code 'NDX', 'MCX' and 'NFO'. 

strike_date can be in DD-MMM-YYYY(Ex.: 01-Jan-2022) or an empty string. 
strike_date can not be an empty string for exchange_code 'NDX', 'MCX' and 'NFO'.

strike_price can be float-value in string or an empty string. 
strike_price can not be an empty string for product_type 'Options'.

right can be either 'Put', 'Call' or an empty string. right can not be an empty string for product_type 'Options'.

Either get_exchange_quotes must be True or get_market_depth must be True. 

Both get_exchange_quotes and get_market_depth can be True, But both must not be False.

For Streaming OHLCV, interval must not be empty and must be equal to either of the following "1second","1minute", "5minute", "30minute"

---

<h4> List of other SDK Methods:</h4>

<h5 id="index_title" >Index</h5>

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
 <li><a href="#square_off1">square_off</a></li>
 <li><a href="#modify_order">modify_order</a></li>
 <li><a href="#trade_list">get_trade_list</a></li>
 <li><a href="#trade_detail">get_trade_detail</a></li>
 <li><a href="#get_names"> get_names </a></li>
 <li><a href="#preview_order"> preview_order </a></li>
</ul>
</div>


<h4 id="customer_detail" > Get Customer details by api-session value.</h4>


```python
breeze.get_customer_details(api_session="your_api_session") 
```

<br>
<a href="#index">Back to Index</a>
<hr>


<h4 id="demat_holding"> Get Demat Holding details of your account.</h4>

```python

breeze.get_demat_holdings()

```
<br>
<a href="#index">Back to Index</a>
<hr>


<h4 id="get_funds"> Get Funds details of your account.</h4>


```python

breeze.get_funds()

```


<br>
<a href="#index">Back to Index</a>
<hr>

<h4 id="set_funds"> Set Funds of your account</h4>


```python
breeze.set_funds(transaction_type="debit", 
                    amount="200",
                    segment="Equity")
```

<p> Note: Set Funds of your account by transaction-type as "Credit" or "Debit" with amount in numeric string as rupees and segment-type as "Equity" or "FNO".</p>
<br>
<a href="#index">Back to Index</a>
<hr>

<h4 id="historical_data1">Get Historical Data for Futures</h4>


```python
breeze.get_historical_data(interval="1minute",
                            from_date= "2022-08-15T07:00:00.000Z",
                            to_date= "2022-08-17T07:00:00.000Z",
                            stock_code="ICIBAN",
                            exchange_code="NFO",
                            product_type="futures",
                            expiry_date="2022-08-25T07:00:00.000Z",
                            right="others",
                            strike_price="0")
                            
```

<a href="#index">Back to Index</a>

<h4 id="historical_data2">Get Historical Data for Equity</h4>


```python
breeze.get_historical_data(interval="1minute",
                            from_date= "2022-08-15T07:00:00.000Z",
                            to_date= "2022-08-17T07:00:00.000Z",
                            stock_code="ITC",
                            exchange_code="NSE",
                            product_type="cash")
```

<a href="#index">Back to Index</a>


<h4 id="historical_data3">Get Historical Data for Options</h4>


```python

breeze.get_historical_data(interval="1minute",
                            from_date= "2022-08-15T07:00:00.000Z",
                            to_date= "2022-08-17T07:00:00.000Z",
                            stock_code="CNXBAN",
                            exchange_code="NFO",
                            product_type="options",
                            expiry_date="2022-09-29T07:00:00.000Z",
                            right="call",
                            strike_price="38000")
```


<p> Note : Get Historical Data for specific stock-code by mentioned interval either as "1minute", "5minute", "30minute" or as "1day"</p>
<br>
<a href="#index">Back to Index</a>
<hr>

<h4 id="historical_data_v21">Get Historical Data (version 2) for Futures</h4>


```python
breeze.get_historical_data_v2(interval="1minute",
                            from_date= "2022-08-15T07:00:00.000Z",
                            to_date= "2022-08-17T07:00:00.000Z",
                            stock_code="ICIBAN",
                            exchange_code="NFO",
                            product_type="futures",
                            expiry_date="2022-08-25T07:00:00.000Z",
                            right="others",
                            strike_price="0")
                            
```

<a href="#index">Back to Index</a>

<h4 id="historical_data_v22">Get Historical Data (version 2) for Equity</h4>


```python
breeze.get_historical_data_v2(interval="1minute",
                            from_date= "2022-08-15T07:00:00.000Z",
                            to_date= "2022-08-17T07:00:00.000Z",
                            stock_code="ITC",
                            exchange_code="NSE",
                            product_type="cash")
```

<a href="#index">Back to Index</a>
<h4 id="historical_data_v23">Get Historical Data (version 2) for Options</h4>


```python

breeze.get_historical_data_v2(interval="1minute",
                            from_date= "2022-08-15T07:00:00.000Z",
                            to_date= "2022-08-17T07:00:00.000Z",
                            stock_code="CNXBAN",
                            exchange_code="NFO",
                            product_type="options",
                            expiry_date="2022-09-29T07:00:00.000Z",
                            right="call",
                            strike_price="38000")
```


<p> 
Note : 

1) Get Historical Data (version 2) for specific stock-code by mentioning interval either as "1second","1minute", "5minute", "30minute" or as "1day". 

2) Maximum candle intervals in one single request is 1000

</p>
<br>
<a href="#index">Back to Index</a>
<hr>


<h4 id="add_margin">Add Margin to your account.</h4>


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


<br>
<a href="#index">Back to Index</a>
<hr>

<h4 id="get_margin">Get Margin of your account.</h4>


```python
breeze.get_margin(exchange_code="NSE")

```

<p> Note: Please change exchange_code=“NFO” to get F&O margin details </p>
<br>
<a href="#index">Back to Index</a>
<hr>

<h4 id="place_order">Placing a Futures Order from your account.</h4>


```python
breeze.place_order(stock_code="ICIBAN",
                    exchange_code="NFO",
                    product="futures",
                    action="buy",
                    order_type="limit",
                    stoploss="0",
                    quantity="3200",
                    price="200",
                    validity="day",
                    validity_date="2022-08-22T06:00:00.000Z",
                    disclosed_quantity="0",
                    expiry_date="2022-08-25T06:00:00.000Z",
                    right="others",
                    strike_price="0",
                    user_remark="Test")
```                    


<h4 id="place_order2">Placing an Option Order from your account.</h4>


```python 
breeze.place_order(stock_code="NIFTY",
                    exchange_code="NFO",
                    product="options",
                    action="buy",
                    order_type="market",
                    stoploss="",
                    quantity="50",
                    price="",
                    validity="day",
                    validity_date="2022-08-30T06:00:00.000Z",
                    disclosed_quantity="0",
                    expiry_date="2022-09-29T06:00:00.000Z",
                    right="call",
                    strike_price="16600")
```


<br>
<a href="#index">Back to Index</a>

<h4 id="place_order3">Place a cash order from your account.</h4>


```python
breeze.place_order(stock_code="ITC",
                    exchange_code="NSE",
                    product="cash",
                    action="buy",
                    order_type="limit",
                    stoploss="",
                    quantity="1",
                    price="305",
                    validity="day"
                )
```                

<br>
<a href="#index">Back to Index</a>

<h4 id="place_order4">Place an optionplus order</h4>

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
<a href="#index">Back to Index</a>

<h4 id="place_order5">Place an future plus order</h4>

```python

breeze.place_order(stock_code= "NIFTY",
                    exchange_code= "NFO",                                     
                    product= "futureplus",                                    
                    action= "Buy",                                            
                    order_type= "limit",
                    stoploss="18720",                                            
                    quantity="50",                                          
                    price= "18725",                                                                             
                    validity="Day",       
                    disclosed_quantity="0",                                  
                    expiry_date="29-DEC-2022")

```                
<br>
<p>Future plus - "Stop loss trigger price cannot be less than last traded price for Buy order" </p>
<a href="#index">Back to Index</a>

<hr>

<h4 id="order_detail">Get an order details by exchange-code and order-id from your account.</h4>

```python
breeze.get_order_detail(exchange_code="NSE",
                        order_id="20220819N100000001")
```                        

<p> Note: Please change exchange_code=“NFO” to get details about F&O</p>
<br>
<a href="#index">Back to Index</a>
<hr>

<h4 id="order_list">Get order list of your account.</h4>


```python
breeze.get_order_list(exchange_code="NSE",
                        from_date="2022-08-01T10:00:00.000Z",
                        to_date="2022-08-19T10:00:00.000Z")
```

<p> Note: Please change exchange_code=“NFO” to get details about F&O</p>
<br>
<a href="#index">Back to Index</a>
<hr>


<h4 id="cancel_order">Cancel an order from your account whose status are not Executed.</h4> 


```python
breeze.cancel_order(exchange_code="NSE",
                    order_id="20220819N100000001")
```                    

<br>
<a href="#index">Back to Index</a>
<hr>

<h4 id="modify_order">Modify an order from your account whose status are not Executed.</h4> 


```python
breeze.modify_order(order_id="202208191100000001",
                    exchange_code="NFO",
                    order_type="limit",
                    stoploss="0",
                    quantity="250",
                    price="290100",
                    validity="day",
                    disclosed_quantity="0",
                    validity_date="2022-08-22T06:00:00.000Z")
```

<br>
<a href="#index">Back to Index</a>
<hr>

<h4 id="portfolio_holding">Get Portfolio Holdings of your account.</h4>


```python
breeze.get_portfolio_holdings(exchange_code="NFO",
                                from_date="2022-08-01T06:00:00.000Z",
                                to_date="2022-08-19T06:00:00.000Z",
                                stock_code="",
                                portfolio_type="")
```

<p> Note: Please change exchange_code=“NSE” to get Equity Portfolio Holdings</p>
<br>
<a href="#index">Back to Index</a>
<hr>

<h4 id="portfolio_position">Get Portfolio Positions from your account.</h4>


```python
breeze.get_portfolio_positions()

```

<br>
<a href="#index">Back to Index</a>
<hr>

<h4 id="get_quotes">Get quotes of mentioned stock-code </h4>


```python
breeze.get_quotes(stock_code="ICIBAN",
                    exchange_code="NFO",
                    expiry_date="2022-08-25T06:00:00.000Z",
                    product_type="futures",
                    right="others",
                    strike_price="0")
```

<br>
<a href="#index">Back to Index</a>
<hr>

<h4 id="get_option_chain">Get option-chain of mentioned stock-code for product-type Futures where input of expiry-date is not compulsory</h4>


```python
breeze.get_option_chain_quotes(stock_code="ICIBAN",
                    exchange_code="NFO",
                    product_type="futures",
                    expiry_date="2022-08-25T06:00:00.000Z")
```                    

<br>
<a href="#index">Back to Index</a>

<h4 id="get_option_chain2">Get option-chain of mentioned stock-code for product-type Options where atleast 2 input is required out of expiry-date, right and strike-price</h4>


```python
breeze.get_option_chain_quotes(stock_code="ICIBAN",
                    exchange_code="NFO",
                    product_type="options",
                    expiry_date="2022-08-25T06:00:00.000Z",
                    right="call")
```

<br>
<a href="#index">Back to Index</a>
<hr>

<h4 id="square_off1">Square off an Equity Margin Order</h4>


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

<p> Note: Please refer get_portfolio_positions() for settlement id and margin_amount</p>
<br>
<a href="#index">Back to Index</a>

<h4 id="square_off2">Square off an FNO Futures Order</h4>


```python
breeze.square_off(exchange_code="NFO",
                    product="futures",
                    stock_code="ICIBAN",
                    expiry_date="2022-08-25T06:00:00.000Z",
                    action="sell",
                    order_type="market",
                    validity="day",
                    stoploss="0",
                    quantity="50",
                    price="0",
                    validity_date="2022-08-12T06:00:00.000Z",
                    trade_password="",
                    disclosed_quantity="0")
```

<br>
<a href="#index">Back to Index</a>

<h4 id="square_off3">Square off an FNO Options Order</h4>


```python
breeze.square_off(exchange_code="NFO",
                    product="options",
                    stock_code="ICIBAN",
                    expiry_date="2022-08-25T06:00:00.000Z",
                    right="Call",
                    strike_price="16850",
                    action="sell",
                    order_type="market",
                    validity="day",
                    stoploss="0",
                    quantity="50",
                    price="0",
                    validity_date="2022-08-12T06:00:00.000Z",
                    trade_password="",
                    disclosed_quantity="0")
```                    

<br>
<a href="#index">Back to Index</a>
<hr>

<h4 id="trade_list">Get trade list of your account.</h4>


```python
breeze.get_trade_list(from_date="2022-08-01T06:00:00.000Z",
                        to_date="2022-08-19T06:00:00.000Z",
                        exchange_code="NSE",
                        product_type="",
                        action="",
                        stock_code="")
```                        

<p> Note: Please change exchange_code=“NFO” to get details about F&O</p>
<br>
<a href="#index">Back to Index</a>
<hr>

<h4 id="trade_detail">Get trade detail of your account.</h4>


```python
breeze.get_trade_detail(exchange_code="NSE",
                        order_id="20220819N100000005")
```

<p> Note: Please change exchange_code=“NFO” to get details about F&O</p>
<br>
<a href="#index">Back to Index</a>
<hr>


<h4 id = "get_names">Get Names </h4>


```python
breeze.get_names(exchange_code = 'NSE',stock_code = 'TATASTEEL')
breeze.get_names(exchange_code = 'NSE',stock_code = 'RELIANCE')
```
<p>Note: Use this method to find ICICI specific stock codes / token </p>

<a href="#index">Back to Index</a>

<hr>

<h4 id="preview_order">Preview Order.</h4>


```python

breeze.preview_order(
    stock_code = "ICIBAN",
    exchange_code = "NSE",
    product = "margin",
    order_type = "limit",
    price = "907.05",
    action = "buy",
    quantity = "1",
    specialflag = "N"
)
```

<br>
<a href="#index">Back to Index</a>
