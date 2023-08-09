import unittest
from unittest.mock import Mock, patch
import sys
sys.path.append('../breeze_connect') 
from breeze_connect import *


class TestSocketEventBreeze(unittest.TestCase):

    @patch('socketio.ClientNamespace.__init__')
    @patch('socketio.Client.connect')
    def setUp(self, mock_connect, mock_super_init):
        self.breeze_instance = BreezeConnect("dummy appkey")
        self.namespace = '/test'
        self.socket_event = SocketEventBreeze(self.namespace, self.breeze_instance)

    def test_connect(self):
        self.socket_event.sio = Mock()
        self.socket_event.breeze.user_id = 'AE684764'
        self.socket_event.breeze.session_key = 'QUU2ODQ3NjQ6OTczNDcyMzM='

        self.socket_event.connect('https://livestream.icicidirect.com')

        self.socket_event.sio.connect.assert_called_once_with(
            'https://livestream.icicidirect.com',
            headers={"User-Agent": "python-socketio[client]/socket"},
            auth={"user": 'AE684764', "token": 'QUU2ODQ3NjQ6OTczNDcyMzM='},
            transports="websocket",
            wait_timeout=3
        )
        self.socket_event.sio.on.assert_called_once_with("connect_error", self.socket_event.my_connect_error)

    def test_on_message_nse(self):
        mock_data = ["4.1!47869",53.35,43.05,53.35,31.7,-24.21,42.9,5250,43.05,3400,100,40.43,"","",36079750,393050,613650,"145.87C","",0.05,321.8,1691387295,56.8]
        received = self.socket_event.breeze.parse_data(mock_data)
        self.socket_event.breeze.on_ticks = Mock()
        self.socket_event.on_message(mock_data)
        #self.socket_event.breeze.on_ticks2 = Mock()
        #print("------------>>>>>>>>>",received)
        expected = {'symbol': '4.1!47869', 'open': 53.35, 'last': 43.05, 'high': 53.35, 'low': 31.7, 'change': -24.21, 'bPrice': 42.9, 'bQty': 5250, 'sPrice': 43.05, 'sQty': 3400, 'ltq': 100, 'avgPrice': 40.43, 'quotes': 'Quotes Data', 'OI': '', 'CHNGOI': '', 'ttq': 36079750, 'totalBuyQt': 393050, 'totalSellQ': 613650, 'ttv': '145.87C', 'trend': '', 'lowerCktLm': 0.05, 'upperCktLm': 321.8, 'ltt': 'Mon Aug  7 11:18:15 2023', 'close': 56.8, 'exchange': 'NSE Futures & Options'}
        self.assertEqual(expected, received, "parsed data incorrect in NSE exchange quote")
        
    def test_on_message_nse_currency(self):
        mock_data = ["4.1!10604",885,893.75,894.75,884,0.94,893.65,15,893.75,561,2,891.46,786772,280490,296628,"70.14C","",796.9,973.9,1691559630,885.4]
        received = self.socket_event.breeze.parse_data(mock_data)
        self.socket_event.breeze.on_ticks = Mock()
        self.socket_event.on_message(mock_data)
        #self.socket_event.breeze.on_ticks2 = Mock()
        #print("------------>>>>>>>>>",received)
        expected = {'symbol': '4.1!10604', 'open': 885, 'last': 893.75, 'high': 894.75, 'low': 884, 'change': 0.94, 'bPrice': 893.65, 'bQty': 15, 'sPrice': 893.75, 'sQty': 561, 'ltq': 2, 'avgPrice': 891.46, 'quotes': 'Quotes Data', 'ttq': 786772, 'totalBuyQt': 280490, 'totalSellQ': 296628, 'ttv': '70.14C', 'trend': '', 'lowerCktLm': 796.9, 'upperCktLm': 973.9, 'ltt': 'Wed Aug  9 11:10:30 2023', 'close': 885.4, 'exchange': 'NSE Equity'}
        self.assertEqual(expected, received, "parsed data incorrect in NSE exchange currency")
        
    def test_on_message_nse_market_depth(self):
        mock_data = ["4.2!95826",1691390811,[[14.6,375,1,"",15.1,375,1,""],[14.55,375,1,"",15.15,375,1,""],[14.4,750,1,"",15.45,375,1,""],[14.3,750,1,"",15.5,1875,1,""],[14.2,375,1,"",15.6,750,1,""]]]
        received = self.socket_event.breeze.parse_data(mock_data)
        self.socket_event.breeze.on_ticks = Mock()
        self.socket_event.on_message(mock_data)
        #self.socket_event.breeze.on_ticks2 = Mock()
        #print("------------>>>>>>>>>",received)
        expected = {'symbol': '4.2!95826', 'time': 'Mon Aug  7 12:16:51 2023', 'depth': [{'BestBuyRate-1': 14.6, 'BestBuyQty-1': 375, 'BuyNoOfOrders-1': 1, 'BuyFlag-1': '', 'BestSellRate-1': 15.1, 'BestSellQty-1': 375, 'SellNoOfOrders-1': 1, 'SellFlag-1': ''}, {'BestBuyRate-2': 14.55, 'BestBuyQty-2': 375, 'BuyNoOfOrders-2': 1, 'BuyFlag-2': '', 'BestSellRate-2': 15.15, 'BestSellQty-2': 375, 'SellNoOfOrders-2': 1, 'SellFlag-2': ''}, {'BestBuyRate-3': 14.4, 'BestBuyQty-3': 750, 'BuyNoOfOrders-3': 1, 'BuyFlag-3': '', 'BestSellRate-3': 15.45, 'BestSellQty-3': 375, 'SellNoOfOrders-3': 1, 'SellFlag-3': ''}, {'BestBuyRate-4': 14.3, 'BestBuyQty-4': 750, 'BuyNoOfOrders-4': 1, 'BuyFlag-4': '', 'BestSellRate-4': 15.5, 'BestSellQty-4': 1875, 'SellNoOfOrders-4': 1, 'SellFlag-4': ''}, {'BestBuyRate-5': 14.2, 'BestBuyQty-5': 375, 'BuyNoOfOrders-5': 1, 'BuyFlag-5': '', 'BestSellRate-5': 15.6, 'BestSellQty-5': 750, 'SellNoOfOrders-5': 1, 'SellFlag-5': ''}], 'quotes': 'Market Depth'}
        self.socket_event.breeze.on_ticks.assert_called_once_with(expected)
        self.assertEqual(expected, received, "parsed data incorrect in NSE")
        
    def test_on_message_bse(self):
        mock_data = ["1.1!543349",1233.05,1239,1245,1233.05,0.74,1238.1,2,1239.9,1,1,1238.43,3493,6435,5653,"43.25L","",983.9,1475.8,1691387639,1229.85]
        received = self.socket_event.breeze.parse_data(mock_data)
        self.socket_event.breeze.on_ticks = Mock()
        self.socket_event.on_message(mock_data)
        #self.socket_event.breeze.on_ticks2 = Mock()
        #print("------------>>>>>>>>>",received)
        expected = {'symbol': '1.1!543349', 'open': 1233.05, 'last': 1239, 'high': 1245, 'low': 1233.05, 'change': 0.74, 'bPrice': 1238.1, 'bQty': 2, 'sPrice': 1239.9, 'sQty': 1, 'ltq': 1, 'avgPrice': 1238.43, 'quotes': 'Quotes Data', 'ttq': 3493, 'totalBuyQt': 6435, 'totalSellQ': 5653, 'ttv': '43.25L', 'trend': '', 'lowerCktLm': 983.9, 'upperCktLm': 1475.8, 'ltt': 'Mon Aug  7 11:23:59 2023', 'close': 1229.85, 'exchange': 'BSE'}
        self.assertEqual(expected, received, "parsed data incorrect in BSE")
        
    def test_on_message_bse_market_depth(self):
        mock_data = ["1.2!530005",1691391056,[[216.25,1,216.5,12],[216.2,17,216.55,145],[216.15,353,216.6,632],[216.1,626,216.65,342],[216.05,915,216.7,211]]]
        received = self.socket_event.breeze.parse_data(mock_data)
        self.socket_event.breeze.on_ticks = Mock()
        self.socket_event.on_message(mock_data)
        
        expected = {'symbol': '1.2!530005', 'time': 'Mon Aug  7 12:20:56 2023', 'depth': [{'BestBuyRate-1': 216.25, 'BestBuyQty-1': 1, 'BestSellRate-1': 216.5, 'BestSellQty-1': 12}, {'BestBuyRate-2': 216.2, 'BestBuyQty-2': 17, 'BestSellRate-2': 216.55, 'BestSellQty-2': 145}, {'BestBuyRate-3': 216.15, 'BestBuyQty-3': 353, 'BestSellRate-3': 216.6, 'BestSellQty-3': 632}, {'BestBuyRate-4': 216.1, 'BestBuyQty-4': 626, 'BestSellRate-4': 216.65, 'BestSellQty-4': 342}, {'BestBuyRate-5': 216.05, 'BestBuyQty-5': 915, 'BestSellRate-5': 216.7, 'BestSellQty-5': 211}], 'quotes': 'Market Depth', 'exchange': 'BSE'}
        self.socket_event.breeze.on_ticks.assert_called_once_with(expected)
        self.assertEqual(expected, received, "parsed data incorrect in BSE")
        
        
    def test_on_message_one_click_data(self):
        mock_data = ["2023-06-21 13:33:53","2023-06-21 13:35:23","1342","Call Initiated","Multiple","NFO","options","stock","TCS   ","2023-06-29 00:00:00","E","put","3440","buy","100","200","175","130.95","197","283.5","3241.95","1200","33250","500","33250","165380.75","2","active"]
        received = self.socket_event.breeze.parse_data(mock_data)
        self.socket_event.breeze.on_ticks = Mock()
        self.socket_event.on_message(mock_data)
        
        expected = {'strategy_date': '2023-06-21 13:33:53', 'modification_date': '2023-06-21 13:35:23', 'portfolio_id': '1342', 'call_action': 'Call Initiated', 'portfolio_name': 'Multiple', 'exchange_code': 'NFO', 'product_type': 'options', 'underlying': 'TCS   ', 'expiry_date': '2023-06-29 00:00:00', 'option_type': 'put', 'strike_price': '3440', 'action': 'buy', 'recommended_price_from': '100', 'recommended_price_to': '200', 'minimum_lot_quantity': '175', 'last_traded_price': '130.95', 'best_bid_price': '197', 'best_offer_price': '283.5', 'last_traded_quantity': '3241.95', 'target_price': '1200', 'expected_profit_per_lot': '33250', 'stop_loss_price': '500', 'expected_loss_per_lot': '33250', 'total_margin': '165380.75', 'leg_no': '2', 'status': 'active'}
        self.socket_event.breeze.on_ticks.assert_called_once_with(expected)
        self.assertEqual(expected, received, "parsed data incorrect in oneclick streaming")
        
    def test_on_message_i_click_data(self):
        mock_data = ["HINDALCO INDUSTRIES LIMITED(HINDAL)Momentum Pick-Buy","HINDAL","buy","","","","Momentum Pick","430-437,2023-05-11 14:15:35","430","437","2023-05-11 14:15:35","470","430","447,50","0","0","  Book Partial Profit:2023-05-11 14:16:20   ","open","iclick_2_gain                 "]
        received = self.socket_event.breeze.parse_data(mock_data)
        self.socket_event.breeze.on_ticks = Mock()
        self.socket_event.on_message(mock_data)
        ##print("----->",received)
        expected = {'stock_name': 'HINDALCO INDUSTRIES LIMITED(HINDAL)Momentum Pick-Buy', 'stock_code': 'HINDAL', 'action_type': 'buy', 'expiry_date': '', 'strike_price': '', 'option_type': '', 'stock_description': 'Momentum Pick', 'recommended_price_and_date': '430-437,2023-05-11 14:15:35', 'recommended_price_from': '430', 'recommended_price_to': '437', 'recommended_date': '2023-05-11 14:15:35', 'target_price': '470', 'sltp_price': '430', 'part_profit_percentage': '447,50', 'profit_price': '0', 'exit_price': '0', 'recommended_update': '  Book Partial Profit:2023-05-11 14:16:20   ', 'iclick_status': 'open', 'subscription_type': 'iclick_2_gain                 '}
        self.socket_event.breeze.on_ticks.assert_called_once_with(expected)
        self.assertEqual(expected, received, "parsed data incorrect in oneclick streaming")
        
    def test_on_message_mcx_data(self):
        mock_data = ["6.1!247311","32"," "," ",0,0,0,0,0,0,0,"",268900,0,0,0,0,0,0,464000,464000,0,[0,0,0,"",0,0,0,""],[0,0,0,"",0,0,0,""],[0,0,0,"",0,0,0,""],[0,0,0,"",0,0,0,""],[0,0,0,"",0,0,0,""]]
        received = self.socket_event.breeze.parse_data(mock_data)
        self.socket_event.breeze.on_ticks = Mock()
        self.socket_event.on_message(mock_data)
        ##print("----->",received)
        expected = {'symbol': '6.1!247311', 'AndiOPVolume': '32', 'Reserved': ' ', 'IndexFlag': ' ', 'ttq': 0, 'last': 0, 'ltq': 0, 'ltt': 'Thu Jan  1 05:30:00 1970', 'AvgTradedPrice': 0, 'TotalBuyQnt': 0, 'TotalSellQnt': 0, 'ReservedStr': '', 'ClosePrice': 268900, 'OpenPrice': 0, 'HighPrice': 0, 'LowPrice': 0, 'ReservedShort': 0, 'CurrOpenInterest': 0, 'TotalTrades': 0, 'HightestPriceEver': 464000, 'LowestPriceEver': 464000, 'TotalTradedValue': 0, 'Quantity-0': 0, 'OrderPrice-0': 0, 'TotalOrders-0': 0, 'Reserved-0': '', 'SellQuantity-0': 0, 'SellOrderPrice-0': 0, 'SellTotalOrders-0': 0, 'SellReserved-0': '', 'Quantity-1': 0, 'OrderPrice-1': 0, 'TotalOrders-1': 0, 'Reserved-1': '', 'SellQuantity-1': 0, 'SellOrderPrice-1': 0, 'SellTotalOrders-1': 0, 'SellReserved-1': '', 'Quantity-2': 0, 'OrderPrice-2': 0, 'TotalOrders-2': 0, 'Reserved-2': '', 'SellQuantity-2': 0, 'SellOrderPrice-2': 0, 'SellTotalOrders-2': 0, 'SellReserved-2': '', 'Quantity-3': 0, 'OrderPrice-3': 0, 'TotalOrders-3': 0, 'Reserved-3': '', 'SellQuantity-3': 0, 'SellOrderPrice-3': 0, 'SellTotalOrders-3': 0, 'SellReserved-3': '', 'Quantity-4': 0, 'OrderPrice-4': 0, 'TotalOrders-4': 0, 'Reserved-4': '', 'SellQuantity-4': 0, 'SellOrderPrice-4': 0, 'SellTotalOrders-4': 0, 'SellReserved-4': '', 'exchange': 'Commodity'}
        self.socket_event.breeze.on_ticks.assert_called_once_with(expected)
        self.assertEqual(expected, received, "parsed data incorrect in mcx/commodity streaming")
        
    def test_on_message_currency_data(self):
        mock_data = ["13.1!9501",105.58,105.4625,105.59,105.35,0.102,105.4575,35,105.465,59,13,105.4677,"","",15170,3090,3008,"15999.45C","",103.1,109.4775,1691399681,105.355]
        received = self.socket_event.breeze.parse_data(mock_data)
        self.socket_event.breeze.on_ticks = Mock()
        self.socket_event.on_message(mock_data)
        ##print("----->",received)
        expected = {'symbol': '13.1!9501', 'open': 105.58, 'last': 105.4625, 'high': 105.59, 'low': 105.35, 'change': 0.102, 'bPrice': 105.4575, 'bQty': 35, 'sPrice': 105.465, 'sQty': 59, 'ltq': 13, 'avgPrice': 105.4677, 'quotes': 'Quotes Data', 'OI': '', 'CHNGOI': '', 'ttq': 15170, 'totalBuyQt': 3090, 'totalSellQ': 3008, 'ttv': '15999.45C', 'trend': '', 'lowerCktLm': 103.1, 'upperCktLm': 109.4775, 'ltt': 'Mon Aug  7 14:44:41 2023', 'close': 105.355, 'exchange': 'NSE Currency'}
        self.socket_event.breeze.on_ticks.assert_called_once_with(expected)
        self.assertEqual(expected, received, "parsed data incorrect in currency streaming")
        
        
    def test_on_ohlc_stream(self):
        mock_data = "NSE,NIFTY,18687.95,18687.95,18687.95,18687.95,0,2022-12-02 14:13:53,1SEC"
        received = self.socket_event.breeze.parse_ohlc_data(mock_data)
        #print("------------>>>>>>>>>",received)
        expected = {'interval': '1second', 'exchange_code': 'NSE', 'stock_code': 'NIFTY', 'low': '18687.95', 'high': '18687.95', 'open': '18687.95', 'close': '18687.95', 'volume': '0', 'datetime': '2022-12-02 14:13:53'}
        #self.socket_event.breeze.on_ticks.assert_called_once_with(expected)
        self.assertEqual(expected, received, "difference in expected and actual in ohlc data,test failed")
        
    def test_on_ohlc_stream_options(self):
        mock_data = "NFO,NIFTY,08-Dec-2022,18700.0,CE,120.5,120.5,120.5,120.5,2500,7592550,2022-12-02 14:10:14,1SEC"
        received = self.socket_event.breeze.parse_ohlc_data(mock_data)
        #print("------------>>>>>>>>>",received)
        expected = {'interval': '1second', 'exchange_code': 'NFO', 'stock_code': 'NIFTY', 'expiry_date': '08-Dec-2022', 'strike_price': '18700.0', 'right_type': 'CE', 'low': '120.5', 'high': '120.5', 'open': '120.5', 'close': '120.5', 'volume': '2500', 'oi': '7592550', 'datetime': '2022-12-02 14:10:14'}
        #self.socket_event.breeze.on_ticks.assert_called_once_with(expected)
        self.assertEqual(expected, received, "difference in expected and actual in ohlc data - options,test failed")
        
    def test_on_ohlc_stream_futures(self):
        mock_data = "NFO,NIFTY,29-Dec-2022,18807.35,18807.35,18807.35,18807.35,0,11771450,2022-12-02 14:19:21,1SEC"
        received = self.socket_event.breeze.parse_ohlc_data(mock_data)
        #print("------------>>>>>>>>>",received)
        expected = {'interval': '1second', 'exchange_code': 'NFO', 'stock_code': 'NIFTY', 'expiry_date': '29-Dec-2022', 'low': '18807.35', 'high': '18807.35', 'open': '18807.35', 'close': '18807.35', 'volume': '0', 'oi': '11771450', 'datetime': '2022-12-02 14:19:21'}
        #self.socket_event.breeze.on_ticks.assert_called_once_with(expected)
        self.assertEqual(expected, received, "difference in expected and actual in ohlc data - options,test failed")
        
    def test_on_message_order(self):
        
        mock_data = [ '1',
            '*',
            'AA073203',
            '*',
            '\u0019230',
            '5',
            '2023080700000518',
            '07-08-2023',
            '11:49:55',
            'Intraday Calls',
            'N',
            '6',
            '8509042060',
            'NFO',
            'NIFTY',
            'O',
            'C',
            'E',
            '2000000',
            '10-Aug-2023',
            '07-Aug-2023',
            'B',
            'L',
            'T',
            '300',
            'R',
            '202308071300000009',
            '50',
            '0',
            '0',
            '0',
            '0',
            'N',
            '13',
            'WEB',
            'Y',
            '07-Aug-2023',
            '*',
            '*',
            '0.000000',
            '0.000000',
            'N',
            'N',
            'N',
            'N',
            'N',
            'N',
            '0.000000',
            '66',
            '',
            '',
            'G\u001a' ]
        #received = self.socket_event.breeze.parse_data(mock_data)
        self.socket_event.breeze.on_ticks = Mock()
        self.socket_event.on_message(mock_data)
        
        received = self.socket_event.breeze.parse_data(mock_data)
        
        #self.socket_event.on_message(mock_data)
        expected = {'sourceNumber': '1', 'group': '*', 'userId': 'AA073203', 'key': '*', 'messageLength': '\x19230', 'requestType': '5', 'messageSequence': '2023080700000518', 'messageDate': '07-08-2023', 'messageTime': '11:49:55', 'messageCategory': 'Intraday Calls', 'messagePriority': 'N', 'messageType': '6', 'orderMatchAccount': '8509042060', 'orderExchangeCode': 'NFO', 'stockCode': 'NIFTY', 'productType': 'Options', 'optionType': 'Call', 'exerciseType': 'E', 'strikePrice': '2000000', 'expiryDate': '10-Aug-2023', 'orderValidDate': '07-Aug-2023', 'orderFlow': 'Buy', 'limitMarketFlag': 'Limit', 'orderType': 'Day', 'limitRate': '300', 'orderStatus': 'Requested', 'orderReference': '202308071300000009', 'orderTotalQuantity': '50', 'executedQuantity': '0', 'cancelledQuantity': '0', 'expiredQuantity': '0', 'stopLossTrigger': '0', 'specialFlag': 'N', 'pipeId': '13', 'channel': 'WEB', 'modificationOrCancelFlag': 'Y', 'tradeDate': '07-Aug-2023', 'acknowledgeNumber': '*', 'stopLossOrderReference': '*', 'totalAmountBlocked': '*', 'averageExecutedRate': '0.000000', 'cancelFlag': '0.000000', 'squareOffMarket': 'N', 'quickExitFlag': 'N', 'stopValidTillDateFlag': 'N', 'priceImprovementFlag': 'N', 'conversionImprovementFlag': 'N', 'trailUpdateCondition': 'N', 'systemPartnerCode': 'N'}
        self.socket_event.breeze.on_ticks.assert_called_once_with(expected)
        self.assertEqual(expected, received, "parsed data incorrect in order streaming")
    def test_on_message_order2(self):
        
        mock_data = [ '1',
        '*',
        'AA034655',
        '*',
        '\u0019254',
        '5',
        '2023080700000981',
        '07-08-2023',
        '14:43:56',
        'Intraday Calls',
        'N',
        '6',
        '8509017275',
        'NFO',
        'TCS',
        'I',
        'C',
        'E',
        '330000',
        '31-Aug-2023',
        '07-Aug-2023',
        'B',
        'S',
        'T',
        '23140',
        'R',
        '202308071300000054',
        '350',
        '0',
        '0',
        '0',
        '17800',
        'N',
        '13',
        'WEB',
        'N',
        '07-Aug-2023',
        '*',
        '202308071300000053',
        '0.000000',
        '0.000000',
        'N',
        'N',
        'N',
        'N',
        'N',
        'N',
        '0.000000',
        '82',
        '',
        '' ]
        #received = self.socket_event.breeze.parse_data(mock_data)
        self.socket_event.breeze.on_ticks = Mock()
        self.socket_event.on_message(mock_data)
        
        received = self.socket_event.breeze.parse_data(mock_data)
        
        #self.socket_event.on_message(mock_data)
        expected = {'sourceNumber': '1', 'group': '*', 'userId': 'AA034655', 'key': '*', 'messageLength': '\x19254', 'requestType': '5', 'messageSequence': '2023080700000981', 'messageDate': '07-08-2023', 'messageTime': '14:43:56', 'messageCategory': 'Intraday Calls', 'messagePriority': 'N', 'messageType': '6', 'orderMatchAccount': '8509017275', 'orderExchangeCode': 'NFO', 'stockCode': 'TCS', 'productType': 'OptionPlus', 'optionType': 'Call', 'exerciseType': 'E', 'strikePrice': '330000', 'expiryDate': '31-Aug-2023', 'orderValidDate': '07-Aug-2023', 'orderFlow': 'Buy', 'limitMarketFlag': 'StopLoss', 'orderType': 'Day', 'limitRate': '23140', 'orderStatus': 'Requested', 'orderReference': '202308071300000054', 'orderTotalQuantity': '350', 'executedQuantity': '0', 'cancelledQuantity': '0', 'expiredQuantity': '0', 'stopLossTrigger': '17800', 'specialFlag': 'N', 'pipeId': '13', 'channel': 'WEB', 'modificationOrCancelFlag': 'N', 'tradeDate': '07-Aug-2023', 'acknowledgeNumber': '*', 'stopLossOrderReference': '*', 'totalAmountBlocked': '202308071300000053', 'averageExecutedRate': '0.000000', 'cancelFlag': '0.000000', 'squareOffMarket': 'N', 'quickExitFlag': 'N', 'stopValidTillDateFlag': 'N', 'priceImprovementFlag': 'N', 'conversionImprovementFlag': 'N', 'trailUpdateCondition': 'N', 'systemPartnerCode': 'N'}
        self.socket_event.breeze.on_ticks.assert_called_once_with(expected)
        self.assertEqual(expected, received, "parsed data incorrect in order streaming")

if __name__ == '__main__':
    unittest.main()
