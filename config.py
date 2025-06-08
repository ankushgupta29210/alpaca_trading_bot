from dotenv import load_dotenv
import os

load_dotenv()

ALPACA_API_KEY = os.getenv("ALPACA_API_KEY")
ALPACA_SECRET_KEY = os.getenv("ALPACA_SECRET_KEY")
ALPACA_BASE_URL = os.getenv("ALPACA_BASE_URL")

# Trading parameters
# SYMBOL = os.getenv("SYMBOL", "TSLA")  # Default to AAPL
SYMBOL = os.getenv("SYMBOL", "SOL-USD")  # Default to SOL
QUANTITY = float(os.getenv("QUANTITY", 1))

# Risk Management
STOP_LOSS_PCT = float(os.getenv("STOP_LOSS_PERCENT", 0.10))  # 3% default
TAKE_PROFIT_PCT = float(os.getenv("TAKE_PROFIT_PERCENT", 0.10))  # 5% default






TELEGRAM_BOT_TOKEN = "7648978114:AAGVd91a_Wz9Yo1XtB6UnLq1NQQu3QfyvPs"
TELEGRAM_CHAT_ID = "@Alpacaalert_bot"

