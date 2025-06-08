# import pandas as pd

def generate_ema_signal(df):
    # Calculate EMAs
    df['EMA12'] = df['Close'].ewm(span=12, adjust=False).mean()
    df['EMA26'] = df['Close'].ewm(span=26, adjust=False).mean()

    if df['EMA12'].iloc[-1] > df['EMA26'].iloc[-1] and df['EMA12'].iloc[-2] <= df['EMA26'].iloc[-2]:
        return 'buy'  # EMA12 crossed above EMA26
    elif df['EMA12'].iloc[-1] < df['EMA26'].iloc[-1] and df['EMA12'].iloc[-2] >= df['EMA26'].iloc[-2]:
        return 'sell'  # EMA12 crossed below EMA26
    else:
        return 'hold'
