from utils.logger import logger
from alpaca_trade_api.rest import REST
from config import ALPACA_API_KEY, ALPACA_SECRET_KEY, ALPACA_BASE_URL
import time
from config import STOP_LOSS_PCT, TAKE_PROFIT_PCT, SYMBOL, QUANTITY  # <-- Added here


api = REST(ALPACA_API_KEY, ALPACA_SECRET_KEY, ALPACA_BASE_URL, api_version='v1')


def monitor_trade(purchase_price, qty=QUANTITY, symbol=SYMBOL, check_interval=60):
    """
    Monitor crypto price and place a sell order if stop-loss or take-profit triggers.
    :param purchase_price: Price at which the asset was bought.
    :param qty: Quantity bought.
    :param symbol: Symbol of the crypto asset.
    :param check_interval: Seconds between each price check.
    """
    stop_loss_price = purchase_price * (1 - STOP_LOSS_PCT)
    take_profit_price = purchase_price * (1 + TAKE_PROFIT_PCT)
    print(f"Monitoring trade for {symbol}:")
    print(f"Purchase price: {purchase_price}")
    print(f"Stop loss trigger: {stop_loss_price}")
    print(f"Take profit trigger: {take_profit_price}")

    while True:
        try:
            # Fetch latest market price for the symbol
            barset = api.get_crypto_bars(symbol, timeframe='1Min').df
            latest_price = barset[symbol]['close'][-1]

            print(f"Latest price: {latest_price}")

            if latest_price <= stop_loss_price:
                print("Stop loss triggered! Placing SELL order...")
                place_sell_order(symbol, qty)
                break
            elif latest_price >= take_profit_price:
                print("Take profit triggered! Placing SELL order...")
                place_sell_order(symbol, qty)
                break
            else:
                print("No trigger yet. Continuing monitoring...")

        except Exception as e:
            print(f"Error fetching price or placing order: {e}")

        time.sleep(check_interval)

def place_sell_order(symbol, qty):
    try:
        order = api.submit_order(
            symbol=symbol,
            qty=qty,
            side='sell',
            type='market',
            time_in_force='gtc'
        )
        print(f"SELL order placed successfully for {qty} {symbol}")
        return order
    except Exception as e:
        print(f"Failed to place sell order: {e}")
        return None





def place_crypto_market_order(symbol: str, qty: float, side: str):
    """
    Place a market order for crypto (ETH/USD, BTC/USD, etc.)
    side: 'buy' or 'sell'
    """
    try:
        order = api.submit_order(
            symbol=symbol,
            qty=qty,
            side=side,
            type="market",
            time_in_force="gtc"
        )
        print(f"{side.upper()} order for {symbol} placed successfully.")
        logger.info(f"{side.upper()} order for {symbol} placed successfully. Order ID: {order.id}")
        return order
    except Exception as e:
        print(f"Crypto order failed: {e}")
        logger.error(f"[Order Error] {e}")
        return None
