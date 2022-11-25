import enum

#Breeze API BASE URL
API_URL = "https://api.icicidirect.com/breezeapi/api/v1/"

#Live Feeds URL
LIVE_FEEDS_URL = "https://livefeeds.icicidirect.com"

#Live Streams URL
LIVE_STREAM_URL = "https://livestream.icicidirect.com"

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
    OPT_CHAIN = "optionchain"
    SQUARE_OFF = "squareoff"
    TRADE = "trades"

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

    #Empty Details Errors
    BLANK_EXCHANGE_CODE = "Exchange-Code cannot be empty"
    BLANK_STOCK_CODE = "Stock-Code cannot be empty"
    BLANK_PRODUCT_TYPE = "Product cannot be empty"
    BLANK_PRODUCT_TYPE_HIST = "Product-type cannot be empty for Exchange-Code 'nfo'"
    BLANK_ACTION = "Action cannot be empty"
    BLANK_ORDER_TYPE = "Order-type cannot be empty"
    BLANK_QUANTITY = "Quantity cannot be empty"
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

    #Validation Errors
    EXCHANGE_CODE_ERROR = "Exchange-Code should be either 'nse', or 'nfo'"
    PRODUCT_TYPE_ERROR = "Product should be either 'futures', 'options', 'futureplus', 'optionplus', 'cash', 'eatm', or 'margin'"
    PRODUCT_TYPE_ERROR_HIST = "Product-type should be either 'futures', 'options', 'futureplus', or 'optionplus' for Exchange-Code 'NFO'"
    ACTION_TYPE_ERROR = "Action should be either 'buy', or 'sell'"
    ORDER_TYPE_ERROR = "Order-type should be either 'limit', 'market', or 'stoploss'"
    VALIDITY_TYPE_ERROR = "Validity should be either 'day', 'ioc', or 'vtc'"
    RIGHT_TYPE_ERROR = "Right should be either 'call', 'put', or 'others'"
    TRANSACTION_TYPE_ERROR = "Transaction-Type should be either 'debit' or 'credit'"
    ZERO_AMOUNT_ERROR = "Amount should be more than 0"
    INTERVAL_TYPE_ERROR = "Interval should be either '1minute', '5minute', '30minute', or '1day'"

# Type List
INTERVAL_TYPES = ["1minute", "5minute", "30minute", "1day"]
PRODUCT_TYPES = ["futures", "options", "futureplus", "optionplus", "cash", "eatm", "margin"]
PRODUCT_TYPES_HIST = ["futures", "options", "futureplus", "optionplus"]
RIGHT_TYPES = ["call", "put", "others"]
ACTION_TYPES = ["buy", "sell"]
ORDER_TYPES = ["limit", "market", "stoploss"]
VALIDITY_TYPES = ["day", "ioc", "vtc"]
TRANSACTION_TYPES = ["debit", "credit"]
EXCHANGE_CODES_HIST = ["nse", "nfo"]

#Isec NSE Stockcode mapping file
ISEC_NSE_CODE_MAP_FILE = {
    'nse':'NSEScripMaster.txt',
    'bse':'BSEScripMaster.txt',
    'cdnse':'CDNSEScripMaster.txt',
    'fonse':'FONSEScripMaster.txt'
}