import schedule
import time
# from strategies.moving_average import get_price_data, generate_signal
# from broker.alpaca_api import place_bracket_order
from broker.alpaca_api import place_crypto_market_order
from config import SYMBOL, QUANTITY
from utils.logger import logger
from strategies.signal import generate_signal
from strategies.signal import get_price_data
from telegram_alert import TelegramAlert
import os
from broker.alpaca_api import monitor_trade

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN", "7648978114:AAGVd91a_Wz9Yo1XtB6UnLq1NQQu3QfyvPs")
CHAT_ID = int(os.getenv("TELEGRAM_CHAT_ID", "5169103646"))
telegram_alert = TelegramAlert(TOKEN, CHAT_ID)




def job():   
    print("\n[Bot] Running scheduled job...")   
    logger.info(" Running scheduled job")
    df = get_price_data()    
    signal = generate_signal(df)
    logger.info(f"[Signal] {signal.upper()}")

    if signal in ['buy', 'sell']:
        order = place_crypto_market_order(SYMBOL, QUANTITY, signal)
        if order:
            if hasattr(order, 'filled_avg_price') and order.filled_avg_price:
                try:
                    purchase_price = float(order.filled_avg_price)
                    print(f" {signal.upper()} order placed at ${purchase_price:.2f}")
                    monitor_trade(purchase_price)
                    
                    msg = (
                        f"✅ Signal: {signal.upper()}\n"
                        f"Order placed for {SYMBOL}\n"
                        f"Price: ${purchase_price:.2f}\n"
                        f"Qty: {QUANTITY}"
                    )
                    
                    
                except Exception as e:
                    logger.error(f"Error converting filled_avg_price to float: {e}")
                    msg = (
                        f"⚠️ Signal: {signal.upper()}\n"
                        f"Order placed but price not available.\n"
                        f"Error: {e}"
                    )
            else:
                logger.warning("Order filled_avg_price not available yet.")
                print(("Order filled_avg_price not available yet."))
                msg = (
                        f"📤 Signal: {signal.upper()}\n"
                        f"Order placed for {SYMBOL}, waiting to be filled.\n"
                        f"Status: {order.status}\n"
                        f"Qty: {order.qty}"
                    )

        else:
            msg = f"❌ Signal: {signal.upper()}\nOrder placement FAILED for {SYMBOL}"
        
        telegram_alert.send_message(msg)
        logger.info(msg.encode('ascii', 'ignore').decode())

        
    else:
        logger.info(" No action required")
        telegram_alert.send_message(f"⚠️Trading Signal: {signal.upper()}\nNo action taken.")

def run_scheduler():
    schedule.every(15).minutes.do(job)
    logger.info(" Scheduler started")
    while True:
        schedule.run_pending()
        time.sleep(300)
