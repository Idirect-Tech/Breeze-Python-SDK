#intialize keys
app_key = "K=89z83417URm)G9+362111V2M9z75dP"
secret_key = "67751&2KNh482s6P&99~8^4w716N8j90"
session_token = '2139838'

# pip install --upgrade breeze-connect

from breeze_connect import BreezeConnect

breeze = BreezeConnect(api_key=app_key)
breeze.generate_session(api_secret=secret_key,session_token=session_token)

# Get data
data = breeze.get_historical_data(interval="1minute",
                            from_date= "2022-11-28T07:00:00.000Z",
                            to_date= "2022-11-28T07:00:00.000Z",
                            stock_code="NIFTY",
                            exchange_code="NFO",
                            product_type="options",
                            expiry_date="2022-12-01T07:00:00.000Z",
                            right="call",
                            strike_price="18000")


def format_data(df):
    # convert the 'datetime' column to Date format 
    df['datetime']= pd.to_datetime(df['datetime'])

    #convert other columns to number format
    for column in df.columns:
        if column == 'datetime': pass 
        else : 
            df[column] = df[column].astype(float)  
            df[column] = df[column].round(1)
        
    return df

def sma(df):
    # calculate moving average - 14 day and 30 day
    df['short_sma'] = df.close.rolling(14).mean().round(1)
    df['long_sma'] = df.close.rolling(30).mean().round(1)
    df = df.dropna()
    return df


def RSI(df, period):
  # calculate RSI for 'period' 
    delta = df['close'].diff()
    up, down = delta.copy(), delta.copy()

    up[up < 0] = 0
    down[down > 0] = 0

    rUp = up.ewm(com=period - 1,  adjust=False).mean()
    rDown = down.ewm(com=period - 1, adjust=False).mean().abs()

    df['RSI_' + str(period)] = 100 - 100 / (1 + rUp / rDown)
    df['RSI_' + str(period)].fillna(0, inplace=True)
    df['RSI_' + str(period)] = df['RSI_' + str(period)].round(1)
    df = df.dropna()
    return df


