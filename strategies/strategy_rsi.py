import pandas as pd

def generate_rsi_signal(df, period=21):
    if len(df) < period + 1:
        print("Not enough data to calculate RSI.")
        return 'hold'
    
    delta = df['Close'].diff()
    gain = delta.clip(lower=0)
    loss = -delta.clip(upper=0)

    avg_gain = gain.rolling(window=period).mean()
    avg_loss = loss.rolling(window=period).mean()

    rs = avg_gain / avg_loss
    rsi = 100 - (100 / (1 + rs))
    
    
    print(rsi.tail())  # debug to check structure

    last_rsi = rsi.iloc[-1]
    if isinstance(last_rsi, pd.Series):  # defensive check
        last_rsi = last_rsi.values[0]

    # print(f"Latest RSI: {last_rsi:.2f}")

    

    if last_rsi < 30:
        return 'buy'  # Oversold
    elif last_rsi > 70:
        return 'sell'  # Overbought
    else:
        return 'hold'
