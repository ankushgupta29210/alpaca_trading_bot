from strategies.strategy_ema import generate_ema_signal
from strategies.strategy_rsi import generate_rsi_signal

# from broker.alpaca_api import place_bracket_order

import pandas as pd
import yfinance as yf

def generate_signal(df):
    # Example: Combine EMA and RSI signals for final signal
    ema_signal = generate_ema_signal(df)
    rsi_signal = generate_rsi_signal(df)
    
    print(f"EMA Signal: {ema_signal.upper()}, RSI Signal: {rsi_signal.upper()}") 

    if ema_signal == 'buy' or rsi_signal == 'buy':
        return 'buy'
    elif ema_signal == 'sell' or rsi_signal == 'sell':
        return 'sell'
    else:
        return 'hold'



# def get_price_data(symbol="TSLA", period="1d", interval="1m"):
   
def get_price_data(symbol="SOL-USD", period="7d", interval="15m"):  # ✅ Valid period and interval


    
    
    """
    Download recent price data for the symbol.
    """
    try:
        df = yf.download(tickers=symbol, period=period, interval=interval, progress=False)
        df = df[['Close']]  # Keep only 'Close' column
        df.dropna(inplace=True)
        df.index.name = 'Datetime'
        return df
    except Exception as e:
        print(f"Error fetching price data: {e}")
        return pd.DataFrame()

