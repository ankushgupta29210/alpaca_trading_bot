# def backtest(df):
#     results = []
#     for i in range(10, len(df)):
#         ma5 = df['Close'][i-5:i].mean()
#         ma10 = df['Close'][i-10:i].mean()
#         signal = 'buy' if ma5 > ma10 else 'sell' if ma5 < ma10 else 'hold'
#         results.append((df.index[i], signal, df['Close'][i]))
#     return results

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
# from strategies.strategy_ema import generate_ema_signal

# def backtest(df):
#     results = []

#     # Precompute EMA columns once to avoid recalculating
#     df['EMA12'] = df['Close'].ewm(span=12, adjust=False).mean()
#     df['EMA26'] = df['Close'].ewm(span=26, adjust=False).mean()

#     # Start from index 26 to ensure EMAs are valid
#     for i in range(26, len(df)):
#         temp_df = df.iloc[:i+1]  # Slice up to current point
#         signal = generate_ema_signal(temp_df)
#         results.append((df.index[i], signal, df['Close'].iloc[i]))

#     return results

def backtest(df):
    results = []
    position = None
    profit = 0.0
    entry_price = 0.0
    total_profit = 0.0
    total_pct_return = 0.0
    trades = []

    for i in range(10, len(df)):
        ma5 = df['Close'][i-5:i].mean()
        ma10 = df['Close'][i-10:i].mean()
        signal = 'buy' if ma5 > ma10 else 'sell' if ma5 < ma10 else 'hold'
        price = df['Close'][i]

        # Track signals
        results.append((df.index[i], signal, price))

        # Simulate trade
        if signal == 'buy' and position is None:
            position = 'long'
            entry_price = price
            trades.append(f" BUY at {price:.2f} on {df.index[i].date()}")
        elif signal == 'sell' and position == 'long':
            profit = price - entry_price
            pct_return = ((price - entry_price) / entry_price) * 100
            total_profit += profit
            total_pct_return += pct_return
            
            trades.append(f" SELL at {price:.2f} on {df.index[i].date()} ➜ Profit: {pct_return:.2f}")
            position = None

    # Print or return summary
    print("\n--- Trade History ---")
    for trade in trades:
        print(trade)

    print(f"\n Total Profit: ${total_profit:.2f}")
    print(f" Total Return: {total_pct_return:.2f}%")
    return results

