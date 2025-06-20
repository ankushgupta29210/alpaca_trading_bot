# 🦙 Alpaca Crypto Trading Bot

An automated crypto trading bot built in Python that uses technical analysis strategies like **RSI**, **EMA**, **MACD**, and more to generate trading signals and execute buy/sell orders on the **Alpaca API**. The bot supports multiple cryptocurrencies, real-time monitoring, Telegram alerts, and configurable risk management (stop-loss, take-profit, and quantity).

## 🔧 Features

- ✅ Trades live using Alpaca's crypto API (paper or live)
- 📊 Signal generation using:
  - RSI (Relative Strength Index)
  - EMA crossover
  - MACD (Moving Average Convergence Divergence)
  - CCI Divergence, Fib Pullback, Heikin Ashi, and more
- 🔔 Telegram notifications for each trade
- 💼 Supports multiple crypto symbols (ETH/USD, SOL/USD, XRP/USD, TON/USD, etc.)
- 📈 Tracks average entry prices and PnL
- ⏱️ Runs every 15 minutes with smart scheduling
- ☁️ Deployed on a cloud server for 24/7 trading

## 📁 Project Structure

alpaca_trading_bot/
├── broker/
│ └── alpaca_api.py
├── strategies/
│ ├── strategy_ema.py
│ ├── strategy_rsi.py
│ └── ...
├── utils/
│ ├── scheduler.py
│ ├── logger.py
│ └── backtester.py
├── main.py
├── config.py
├── telegram_alert.py
└── requirements.txt


## 🧠 Strategies Used

The bot uses a **signal aggregation** approach — combining multiple strategies to vote on a final action:

- `buy` if majority of signals say buy  
- `sell` if majority say sell  
- `hold` if no consensus  

Each strategy runs independently and contributes to the decision logic.

## 🚀 How to Use

1. Clone the repo:
   ```bash
   git clone https://github.com/ankushgupta29210/alpaca_trading_bot.git
   cd alpaca_trading_bot
2. pip install -r requirements.txt
3. ALPACA_API_KEY=your_key
ALPACA_SECRET_KEY=your_secret
TELEGRAM_TOKEN=your_bot_token
TELEGRAM_CHAT_ID=your_chat_id
4.python main.py


🌐 Deployment
The bot is currently hosted on a cloud server using cron or background scheduler to run every 15 minutes.
It logs every trade, error, and signal vote to bot.log.

📬 Contact
Developed by Ankush Gupta
📧 ankushgupta29210@gmail.com
📍 Surrey, BC | LinkedIn



