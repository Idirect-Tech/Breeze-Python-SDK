import enum

#Breeze API BASE URL
# API_URL = "https://uatapi.icicidirect.com/iciciDirectWebApi_core/api/v1/"
API_URL = "https://api.icicidirect.com/breezeapi/api/v1/"

#Breeze New Endpoint
BREEZE_NEW_URL = "https://breezeapi.icicidirect.com/api/v2/"

#Live Feeds URL
LIVE_FEEDS_URL = "https://livefeeds.icicidirect.com"

#Live Streams URL
# LIVE_STREAM_URL = "https://uatstreams.icicidirect.com"
LIVE_STREAM_URL = "https://livestream.icicidirect.com"

#Live OHLC Stream URL
LIVE_OHLC_STREAM_URL = "https://breezeapi.icicidirect.com"

#Security Master Download Link 
SECURITY_MASTER_URL = "https://directlink.icicidirect.com/NewSecurityMaster/SecurityMaster.zip"

#Stock Script Code Download Link
STOCK_SCRIPT_CSV_URL = "https://traderweb.icicidirect.com/Content/File/txtFile/ScripFile/StockScriptNew.csv"

#API Methods
class APIRequestType(enum.Enum):

    POST = "POST"
    GET = "GET"
    PUT = "PUT"
    DELETE = "DELETE"

    def __str__(self):
        return str(self.value)

#API endpoints
class APIEndPoint(enum.Enum):

    CUST_DETAILS = "customerdetails"
    DEMAT_HOLDING = "dematholdings"
    FUND = "funds"
    HIST_CHART = "historicalcharts"
    MARGIN = "margin"
    ORDER = "order"
    PORTFOLIO_HOLDING = "portfolioholdings"
    PORTFOLIO_POSITION = "portfoliopositions"
    QUOTE = "quotes"
    TRADE = "trades"
    OPT_CHAIN = "optionchain"
    SQUARE_OFF = "squareoff"
    LIMIT_CALCULATOR = "fnolmtpriceandqtycal"
    MARGIN_CALULATOR = "margincalculator"
    GTT_ORDER = "gttorder"
    
    def __str__(self):
        return str(self.value)

#TUX Mapping
TUX_TO_USER_MAP = {
            "orderFlow": {
                "B": "Buy",
                "S": "Sell",
                "N": "NA"
            },
            "limitMarketFlag": {
                "L": "Limit",
                "M": "Market",
                "S": "StopLoss"
            },
            "orderType": {
                "T": "Day",
                "I": "IoC",
                "V": "VTC"
            },
            "productType": {
                "F": "Futures",
                "O": "Options",
                "P": "FuturePlus",
                "U": "FuturePlus_sltp",
                "I": "OptionPlus",
                "C": "Cash",
                "Y": "eATM",
                "B": "BTST",
                "M": "Margin",
                "T": "MarginPlus"
            },
            "orderStatus": {
                "A": "All",
                "R": "Requested",
                "Q": "Queued",
                "O": "Ordered",
                "P": "Partially Executed",
                "E": "Executed",
                "J": "Rejected",
                "X": "Expired",
                "B": "Partially Executed And Expired",
                "D": "Partially Executed And Cancelled",
                "F": "Freezed",
                "C": "Cancelled"
            },
            "optionType": {
                "C": "Call",
                "P": "Put",
                "*": "Others"
            },
        }

#Response Message
class ResponseMessage(enum.Enum):

    #Currency not allowed
    CURRENCY_NOT_ALLOWED = "NDX as Exchange-Code not allowed"

    #Empty Details Errors
    BLANK_EXCHANGE_CODE = "Exchange-Code cannot be empty"
    BLANK_STOCK_CODE = "Stock-Code cannot be empty"
    BLANK_PRODUCT_TYPE = "Product cannot be empty"
    BLANK_PRODUCT_TYPE_NFO_BFO = "Product-type cannot be empty for Exchange-Code 'nfo' or 'bfo'"
    BLANK_PRODUCT_TYPE_HIST_V2 = "Product-type cannot be empty for Exchange-Code 'nfo','ndx', 'mcx' or 'bfo'"
    BLANK_ACTION = "Action cannot be empty"
    BLANK_ORDER_TYPE = "Order-type cannot be empty"
    BLANK_QUANTITY = "Quantity cannot be empty"
    BLANK_LOTS = "Lots cannot be empty"
    BLANK_VALIDITY = "Validity cannot be empty"
    BLANK_ORDER_ID  = "Order-Id cannot be empty"
    BLANK_FROM_DATE = "From-Date cannot be empty"
    BLANK_TO_DATE = "To-Date cannot be empty"
    BLANK_TRANSACTION_TYPE = "Transaction-Type cannot be empty"
    BLANK_AMOUNT = "Amount cannot be empty"
    BLANK_SEGMENT = "Segment cannot be empty"
    BLANK_INTERVAL = "Interval cannot be empty"
    BLANK_STRIKE_PRICE = "Strike-Price cannot be empty for Product-Type 'options'"
    BLANK_EXPIRY_DATE = "Expiry-Date cannot be empty for exchange-code 'nfo'"
    BLANK_RIGHT_STRIKE_PRICE = "Either Right or Strike-Price cannot be empty."
    BLANK_RIGHT_EXPIRY_DATE = "Either Expiry-Date or Right cannot be empty."
    BLANK_EXPIRY_DATE_STRIKE_PRICE = "Either Expiry-Date or Strike-Price cannot be empty."

    #Validation Errors
    EXCHANGE_CODE_ERROR = "Exchange-Code should be either 'nse', or 'nfo' or 'ndx' or 'mcx'"
    EXCHANGE_CODE_HIST_V2_ERROR = "Exchange-Code should be either 'nse', 'bse' ,'nfo', 'ndx', 'mcx' or 'bfo'"
    PRODUCT_TYPE_ERROR = "Product should be either 'futures', 'options', 'futureplus', 'optionplus', 'cash', 'eatm','btst','mtf' or 'margin'"
    PRODUCT_TYPE_ERROR_NFO_BFO = "Product-type should be either 'futures', 'options', 'futureplus', or 'optionplus' for Exchange-Code 'NFO' or 'BFO'"
    PRODUCT_TYPE_ERROR_HIST_V2 = "Product-type should be either 'futures', 'options' for Exchange-Code 'NFO','NDX', 'MCX' or 'BFO'"
    ACTION_TYPE_ERROR = "Action should be either 'buy', or 'sell'"
    ORDER_TYPE_ERROR = "Order-type should be either 'limit', 'market', or 'stoploss'"
    VALIDITY_TYPE_ERROR = "Validity should be either 'day', 'ioc', or 'vtc'"
    RIGHT_TYPE_ERROR = "Right should be either 'call', 'put', or 'others'"
    TRANSACTION_TYPE_ERROR = "Transaction-Type should be either 'debit' or 'credit'"
    ZERO_AMOUNT_ERROR = "Amount should be more than 0"
    AMOUNT_DIGIT_ERROR = "Amount should only contain digits"
    INTERVAL_TYPE_ERROR = "Interval should be either '1minute', '5minute', '30minute', or '1day'"
    INTERVAL_TYPE_ERROR_HIST_V2 = "Interval should be either '1second','1minute', '5minute', '30minute', or '1day'"
    API_SESSION_ERROR = "API Session cannot be empty"
    OPT_CHAIN_EXCH_CODE_ERROR = "Exchange code should be nfo or bfo"
    NFO_FIELDS_MISSING_ERROR = "Atleast two inputs are required out of Expiry-Date, Right & Strike-Price. All three cannot be empty'."
    UNDER_LYING_ERROR = "underlying cant be empty"
    ORDER_FLOW = "order_flow cant be empty"
    STOP_LOSS_TRIGGER = "stop_loss_trigger cant be empty"
    OPTION_TYPE = "option_type cant be empty,its either CALL or PUT"
    SOURCE_FLAG = "source_flag cant be empty, it should be either P or M"
    MARKET_TYPE = "market_type cant be empty"
    FRESH_ORDER_LIMIT = "fresh_order_limit cant be empty"
    GTT_TYPE_ERROR_THREE_LEG = "type of GTT should be either 'oco' or 'cover_oco'. "
    GTT_TYPE_ERROR_SINGLE_LEG = "type of GTT should be 'single'. "
    MTF_SELL_NOT_ALLOWED = "SELL action is not allowed for MTF product type. "


    #Socket Connectivity Response
    RATE_REFRESH_NOT_CONNECTED = "socket server is not connected to rate refresh."
    RATE_REFRESH_DISCONNECTED = "socket server for rate refresh  has been disconnected."
    ORDER_REFRESH_NOT_CONNECTED = "socket server is not connected to order refresh."
    ORDER_REFRESH_DISCONNECTED = "socket server for order streaming has been disconnected."
    ORDER_NOTIFICATION_SUBSRIBED = "Order Notification subscribed successfully"
    OHLCV_STREAM_NOT_CONNECTED = "socket server is not connected to OHLCV Stream."
    OHLCV_STREAM_DISCONNECTED = "socket server for OHLCV Streaming has been disconnected."
    STRATEGY_STREAM_SUBSCRIBED = "{0} streaming subscribed successfully."
    STRATEGY_STREAM_DISCONNECTED = "strategy stream disconnected."
    STRATEGY_STREAM_NOT_CONNECTED = "socket server is not connected to strategy streaming."
    STRATEGY_STREAM_UNSUBSCRIBED = "{0} streaming unsubscribed successfully."

    #Stock Subscription Message
    STOCK_SUBSCRIBE_MESSAGE = "Stock {0} subscribed successfully"
    STOCK_UNSUBSCRIBE_MESSAGE = "Stock {0} unsubscribed successfully"

    def __str__(self):
        return str(self.value)
        
class ExceptionMessage(enum.Enum):

    #Authentication Error
    AUTHENICATION_EXCEPTION = "Could not authenticate credentials. Please check token and keys"
    #Subscribe Exception
    QUOTE_DEPTH_EXCEPTION = "Either getExchangeQuotes must be true or getMarketDepth must be true"
    EXCHANGE_CODE_EXCEPTION = "Exchange Code allowed are 'BSE', 'NSE', 'NDX', 'MCX', 'NFO', 'BFO'."
    STOCK_CODE_EXCEPTION = "Stock-Code cannot be empty."
    EXPIRY_DATE_EXCEPTION = "Expiry-Date cannot be empty for given Exchange-Code."
    PRODUCT_TYPE_EXCEPTION = "Product-Type should either be Futures or Options for given Exchange-Code."
    STRIKE_PRICE_EXCEPTION = "Strike Price cannot be empty for Product-Type 'Options'."
    RIGHT_EXCEPTION = "Rights should either be Put or Call for Product-Type 'Options'."
    STOCK_INVALID_EXCEPTION = "Stock-Code not found."
    WRONG_EXCHANGE_CODE_EXCEPTION = "Stock-Token cannot be found due to wrong exchange-code."
    STOCK_NOT_EXIST_EXCEPTION = "Stock-Data does not exist in exchange-code {0} for Stock-Token {1}."
    ISEC_NSE_STOCK_MAP_EXCEPTION = "Result Not Found"
    STREAM_OHLC_INTERVAL_ERROR = "Interval should be either '1second','1minute', '5minute', '30minute'"

    #CUSTOMER_DETAILS_API
    SESSIONKEY_INCORRECT = "Could not authenticate credentials. Please check session key."
    APPKEY_INCORRECT = "Could not authenticate credentials. Please check api key."
    SESSIONKEY_EXPIRED = "Session key is expired."
    CUSTOMERDETAILS_API_EXCEPTION = "Unable to retrieve customer details at the moment. Please try again later."

    #SOCKET EXCEPTION
    OHLC_SOCKET_CONNECTION_DISCONNECTED = "Failed to connect to OHLC stream"
    LIVESTREAM_SOCKET_CONNECTION_DISCONNECTED = "Failed to connect to live stream"
    ORDERNOTIFY_SOCKET_CONNECTION_DISCONNECTED = "Failed to connect to order stream"
    STREAMING_SOCKET_CONNECTION_DISCONNECTED = "Connection Disconnected"    

    #API Call Exception
    API_REQUEST_EXCEPTION = "Error while trying to make request {0} {1}"

    def __str__(self):
        return str(self.value)

# Type List
INTERVAL_TYPES = ["1minute", "5minute", "30minute", "1day"]
INTERVAL_TYPES_HIST_V2 = ["1second","1minute", "5minute", "30minute", "1day"]
INTERVAL_TYPES_STREAM_OHLC = ["1second","1minute", "5minute", "30minute"]
PRODUCT_TYPES = ["futures", "options", "futureplus", "optionplus", "cash", "eatm", "margin","mtf","btst"]
PRODUCT_TYPES_HIST = ["futures", "options", "futureplus", "optionplus"]
PRODUCT_TYPES_HIST_V2 = ["futures", "options","cash"]
RIGHT_TYPES = ["call", "put", "others"]
ACTION_TYPES = ["buy", "sell"]
ORDER_TYPES = ["limit", "market", "stoploss"]
VALIDITY_TYPES = ["day", "ioc", "vtc"]
TRANSACTION_TYPES = ["debit", "credit"]
EXCHANGE_CODES_HIST = ["nse", "nfo", "ndx", "mcx"]
EXCHANGE_CODES_HIST_V2 = ["nse","bse","nfo","ndx","mcx","bfo"]
FNO_EXCHANGE_TYPES = ["nfo","mcx","ndx","bfo"]
STRATEGY_SUBSCRIPTION = ["one_click_fno","i_click_2_gain"]
GTT_ORDER_TYPES = ["oco","cover_oco"]

#Isec NSE Stockcode mapping file
ISEC_NSE_CODE_MAP_FILE = {
    'nse':'NSEScripMaster.txt',
    'bse':'BSEScripMaster.txt',
    'cdnse':'CDNSEScripMaster.txt',
    'fonse':'FONSEScripMaster.txt'
}

feed_interval_map = {
    '1MIN':"1minute",
    '5MIN':"5minute",
    '30MIN':'30minute',
    '1SEC':'1second'
}

channel_interval_map = {
    '1minute':'1MIN',
    '5minute':'5MIN',
    '30minute':'30MIN',
    '1second':'1SEC'
}