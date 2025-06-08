
from utils.scheduler import run_scheduler
from utils.logger import logger

if __name__ == "__main__":
    print("Alpaca Trading Bot has started...")  # Message on terminal
    logger.info(" Alpaca Trading Bot Started")
    try:
        run_scheduler()
    except Exception as e:
        logger.error(f" Bot crashed: {e}")
        print(f"Bot crashed: {e}")  # Also show error on terminal
