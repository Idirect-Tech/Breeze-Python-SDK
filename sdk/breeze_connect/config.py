#Breeze API BASE URL
_api_url = "https://api.icicidirect.com/breezeapi/api/v1/"

#Live Feeds URL
_live_feeds_url = "https://livefeeds.icicidirect.com"

#Live Streams URL
_live_stream_url = "https://livestream.icicidirect.com"

#Security Master Download Link 
_security_master_url = "https://directlink.icicidirect.com/NewSecurityMaster/SecurityMaster.zip"

#Stock Script Code Download Link
_stock_script_csv_url = "https://traderweb.icicidirect.com/Content/File/txtFile/ScripFile/StockScriptNew.csv"

#API endpoints
_api_endpoints = {
    "cust.details":"customerdetails",
    "demat.holding":"dematholdings",
    "fund":"funds",
    "hist.chart":"historicalcharts",
    "margin":"margin",
    "order":"order",
    "portfolio.holding":"portfolioholdings",
    "portfolio.position":"portfoliopositions",
    "quote":"quotes",
    "opt.chain":"optionchain",
    "square.off":"squareoff",
    "trade":"trades"
}

#TUX Mapping
_tux_to_user_map = {
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
