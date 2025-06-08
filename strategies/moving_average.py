# import yfinance as yf
# import pandas as pd

# def get_price_data():
#     data = yf.download("AAPL", period="2d", interval="1h")
#     return data

# def generate_signal(df):
#     df['MA5'] = df['Close'].rolling(window=5).mean()
#     df['MA10'] = df['Close'].rolling(window=10).mean()

#     if df['MA5'].iloc[-1] > df['MA10'].iloc[-1]:
#         return 'buy'
#     elif df['MA5'].iloc[-1] < df['MA10'].iloc[-1]:
#         return 'sell'
#     else:
#         return 'hold'


import yfinance as yf

def get_price_data():
    df = yf.download("AAPL", period="2d", interval="1h")
    return df

def generate_signal(df):
    df['MA5'] = df['Close'].rolling(window=5).mean()
    df['MA10'] = df['Close'].rolling(window=10).mean()
    if df['MA5'].iloc[-1] > df['MA10'].iloc[-1]:
        return 'buy'
    elif df['MA5'].iloc[-1] < df['MA10'].iloc[-1]:
        return 'sell'
    return 'hold'
