### Enter your API Keys

api_key = "INSERT_YOUR_APP_KEY_HERE"
api_secret = "INSERT_YOUR_SECRET_KEY_HERE"
api_session = 'INSERT_YOUR_API_SESSION_HERE'

import time
import pandas as pd
from datetime import timedelta, datetime

from breeze_connect import BreezeConnect

# Initialize SDK
breeze = BreezeConnect(api_key=api_key)

# Generate Session
breeze.generate_session(api_secret=api_secret,
                        session_token=api_session)

# initialize user inputs
STOCK = "SUZENE"
INTERVAL = '1day'
SMA_PERIOD = float(20)
DURATION_IN_SECONDS = 120

today = datetime.now()
MARKET_OPEN = today.replace(hour=9,minute=15,second=0, microsecond=0)
MARKET_CLOSE = today.replace(hour=15,minute=30,second=0, microsecond=0)

try:
    assert (today > MARKET_OPEN) and (today < MARKET_CLOSE)
except Exception as e:
    print("Please re-check Time\nStart time should be between 09:45 to 15:00")

def get_sma():
    global STOCK, INTERVAL, SMA_PERIOD
    current_time = datetime.now()
    from_date = current_time - timedelta(days=SMA_PERIOD)
    
    try:
        # note that we have converted dates to ISO time-format before making API call
        data = breeze.get_historical_data_v2(interval=INTERVAL,
                                            from_date = from_date.strftime('%Y-%m-%dT%H:%M:%S.000Z'),
                                            to_date = current_time.strftime('%Y-%m-%dT%H:%M:%S.000Z'),
                                            stock_code=STOCK,
                                            exchange_code="NSE",
                                            product_type="cash")

    except Exception as error: 
        print('Failed Historical API Request', error)
        return False
      

    if(data['Status']==200):

          # Calculate simple moving average of 'close' price
          data = pd.DataFrame(data['Success'])
          data.close = data.close.astype(float)
          sma = round(data.close.mean(),2)
          return sma

      elif(data['Status']==500):
          print('Bad API request : ',data)
          return False

def get_current_price(stock):
    #This function fetches the last traded price (LTP) of stock
    try:
        price = breeze.get_quotes(stock_code=stock,exchange_code="NSE",product_type="cash")
        return price['Success'][0]['ltp']

    except Exception as error:
        print('Failed Quotes API request', error)

def start_strategy():
    # This function starts strategy for 'duration' seconds provided by user
    global DURATION_IN_SECONDS

    # Set time interval for which strategy will run
    current_time = datetime.now()
    end_time = current_time + timedelta(seconds = DURATION_IN_SECONDS)

    # Start the loop
    while (current_time < end_time):

        #print current time in Hour:Minute:Second format
        print(f'Time --> {current_time.time().strftime('%H:%M:%S')}')

        #fetch current price of stock
        try:
            current_price = get_current_price(STOCK)
            indicator = get_sma()
        
        #check condition for buy signal
        if (current_price > indicator) :
            print(f'BUY SIGNAL --> current price {current_price} is greater than SMA {indicator}!')

        else:
            print(f'No signal --> current price {current_price} is lesser than SMA {indicator}!')

        # Pause for 60 seconds and then reset the current time for next iteration
        time.sleep(60)
        current_time = datetime.now()
        
if __name__ == "__main__":
  start_strategy()
