from breeze_connect import BreezeConnect

# ###################################### Generate Session ######################################
breeze = BreezeConnect(api_key="your_api_key")

# Redirect the user to the login url obtained
# from login url, and receive the session_token from key named as API_Session
# from the registered redirect url after the login flow.

breeze.generate_session(api_secret="your_secret",
                      session_token="YOUR_SESSION_TOKEN_OBTAINED_FROM_LOGIN_PAGE_RESPONSE")


###################################### Websocket ######################################
# connect to websocket streaming service
breeze.ws_connect()

# # subscribe stocks feeds by stock-token
# breeze.subscribe_stock(stock_token="")

# # subscribe stocks feeds by exchange_code, stock_code, product_type, strike_date, strike_price, right, get_exchange_quotes, get_market_depth, 
# breeze.subscribe_stock(exchange_code="", stock_code="", product_type="", strike_date="", strike_price="", right="", get_exchange_quotes=True, get_market_depth=True)

def on_ticks(ticks):
    # Callback to receive ticks.
    print("Ticks: {}".format(ticks))

breeze.on_ticks = on_ticks

# # unsubscribe stocks feeds by stock-token
# breeze.unsubscribe_stock(stock_token="")

# # unsubscribe stocks feeds by exchange_code, stock_code, product_type, strike_date, strike_price, right, get_exchange_quotes, get_market_depth, 
# breeze.unsubscribe_stock(exchange_code="", stock_code="", product_type="", strike_date="", strike_price="", right="", get_exchange_quotes=True, get_market_depth=True)

# # Please Note:
# # Examples for stock_token are "4.1!38071" or "1.1!500780"
# # exchange_code must be 'BSE', 'NSE', 'NDX', 'MCX' or 'NFO'.
# # stock_code should not be an empty string. Examples for stock_token are "WIPRO" or "ZEEENT".
# # product_type can be either 'Futures', 'Options' or an empty string. product_type should not be an empty string for exchange_code 'NDX', 'MCX' and 'NFO'. 
# # strike_date can be in DD-MMM-YYYY(Ex.: 01-Jan-2022) or an empty string. strike_date should not be an empty string for exchange_code 'NDX', 'MCX' and 'NFO'.
# # strike_price can be float-value in string or an empty string. strike_price should not be an empty string for product_type 'Options'.
# # right can be either 'Put', 'Call' or an empty string. right should not be an empty string for product_type 'Options'.
# # Either get_exchange_quotes must be True or get_market_depth must be True. Both get_exchange_quotes and get_market_depth can be True, But both must not be False.



# import time
# breeze.subscribe_stock(stock_token="1.1!500780")
# breeze.subscribe_stock(stock_token="4.1!38071")
# breeze.subscribe_stock(exchange_code="NFO", stock_code="ZEEENT", product_type="Options", strike_date="27-Jan-2022", strike_price="425", right="Call", get_exchange_quotes=True, get_market_depth=False)
# time.sleep(10)
# breeze.unsubscribe_stock(stock_token="1.1!500780")
# time.sleep(10)
# breeze.unsubscribe_stock(stock_token="1.1!500780")
# time.sleep(10)
# breeze.unsubscribe_stock(exchange_code="NFO", stock_code="ZEEENT", product_type="Options", strike_date="27-Jan-2022", strike_price="425", right="Call", get_exchange_quotes=True, get_market_depth=False)
# time.sleep(12)
# breeze.unsubscribe_stock(exchange_code="NFO", stock_code="ZEEENT", product_type="Options", strike_date="24-Feb-2022", strike_price="300", right="Put", get_exchange_quotes=True, get_market_depth=False)


###################################### APIfication ######################################

# print(breeze.customer_login(user_id="",
#                           password="",
#                           date_of_birth=""))

# print(breeze.get_customer_details(
#     API_Session="YOUR_SESSION_TOKEN_OBTAINED_FROM_LOGIN_PAGE_RESPONSE"))

# print(breeze.get_demat_holdings())

# print(breeze.get_funds())

# print(breeze.set_funds(transaction_type="Debit",
#                      amount="200",
#                      segment="Equity"))

# print(breeze.get_historical_charts_list(interval="30minute",
#                                       from_date="2021-11-15T07:00:00.000Z",
#                                       to_date="2021-11-15T07:00:00.000Z",
#                                       stock_code="AXIBAN",
#                                       exchange_code="NSE",
#                                       segment="D",
#                                       product_type="F",
#                                       exercise_type="E",
#                                       expiry_date="2021-11-30T07:00:00.000Z",
#                                       option_type="*",
#                                       strike_price="0"))

# print(breeze.add_margins(product_type="M",
#                        stock_code="TCS",
#                        exchange_code="BSE",
#                        order_segment_code="N",
#                        order_settlement="2021220",
#                        add_amount="100",
#                        margin_amount="3817.10",
#                        order_open_quantity="10",
#                        cover_quantity="0",
#                        category_INDSTK="",
#                        contract_tag="",
#                        add_margin_amount="",
#                        expiry_date="",
#                        order_optional_exercise_type="",
#                        option_type="",
#                        exercise_type="",
#                        strike_price="",
#                        order_stock_code=""))

# print(breeze.get_margins(exchange_code="NSE"))

# print(breeze.order_placement(stock_code="AXIBAN",
#                            exchange_code="NFO",
#                            product="Futures",
#                            action="Buy",
#                            order_type="Limit",
#                            stoploss="0",
#                            quantity="1200",
#                            price="712.00",
#                            validity="Day",
#                            validity_date="2021-12-16T06:00:00.000Z",
#                            disclosed_quantity="0",
#                            expiry_date="2021-12-25T06:00:00.000Z",
#                            right="Others",
#                            strike_price="0",
#                            user_remark="Test"))

# print(breeze.get_order_detail(exchange_code="NSE",
#                             order_id="20211116N100000023"))

# print(breeze.get_order_detail(exchange_code="NFO",
#                             order_id="202111161100000284"))

# print(breeze.get_order_list(exchange_code="NSE",
#                           from_date="2021-11-01T10:00:00.000Z",
#                           to_date="2021-11-30T10:00:00.000Z"))

# print(breeze.order_cancellation(exchange_code="NSE",
#                               order_id="20211116N100000022"))

# print(breeze.order_modification(order_id="202111241100000002",
#                               exchange_code="NFO",
#                               order_type="Limit",
#                               stoploss="0",
#                               quantity="250",
#                               price="290100",
#                               validity="Day",
#                               disclosed_quantity="0",
#                               validity_date="2021-12-30T06:00:00.000Z"))

# print(breeze.get_portfolio_holdings(exchange_code="NFO",
#                                   from_date="2021-11-01T06:00:00.000Z",
#                                   to_date="2021-11-30T06:00:00.000Z",
#                                   underlying="A",
#                                   portfolio_type=""))

# print(breeze.get_portfolio_positions())

# print(breeze.get_quotes(stock_code="",
#                       exchange_code="NFO",
#                       expiry_date="2021-12-30T06:00:00.000Z",
#                       product_type="Futures",
#                       right="Others",
#                       strike_price="0"))

# print(breeze.square_off(source_flag="",
#                       order_stock_code="NIFTY",
#                       exchange_code="NFO",
#                       order_quantity="50",
#                       order_rate="0",
#                       order_flow="S",
#                       order_type="M",
#                       order_validity="T",
#                       order_stop_loss_price="0",
#                       order_disclosed_quantity="0",
#                       protection_percentage="",
#                       order_segment_code="",
#                       order_settlement="",
#                       margin_amount="",
#                       order_open_quantity="",
#                       order_cover_quantity="",
#                       order_product="F",
#                       order_exp_date="2021-12-30T06:00:00.000Z",
#                       order_exc_type="",
#                       order_option_type="",
#                       order_strike_price="0",
#                       order_trade_date="2021-12-16T06:00:00.000Z",
#                       trade_password="",
#                       order_option_exercise_type="*E"))

# print(breeze.get_trade_list(from_date="2021-09-28T06:00:00.000Z",
#                           to_date="2021-11-15T06:00:00.000Z",
#                           exchange_code="NSE",
#                           product_type="",
#                           action="",
#                           stock_code=""))

# print(breeze.get_trade_detail(exchange_code="NSE",
#                             order_id="20210928N100000067"))
