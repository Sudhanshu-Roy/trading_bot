from binance.client import Client
from binance.exceptions import BinanceAPIException
from requests.exceptions import RequestException

from config import API_KEY, API_SECRET
from logger import logger

import time

class BinanceFuturesClient:

    def __init__(self):

        self.client = Client(
            API_KEY,
            API_SECRET
        )

        self.client.FUTURES_URL = (
            "https://testnet.binancefuture.com/fapi"
        )

        self._sync_time()

    def _sync_time(self):
        """
        Synchronize local timestamp
        with Binance server timestamp.
        """

        try:

            server_time = (
                self.client.get_server_time()
                ["serverTime"]
            )

            self.client.timestamp_offset = (
                server_time
                - int(time.time() * 1000)
            )

            logger.info(
                "Timestamp synchronized."
            )

        except Exception as e:

            logger.error(
                f"Timestamp sync failed: {e}"
            )

            raise

    def validate_symbol(
        self,
        symbol: str
    ) -> bool:

        try:

            exchange_info = (
                self.client.futures_exchange_info()
            )

            valid_symbols = {
                s["symbol"]
                for s in exchange_info["symbols"]
            }

            return symbol.upper() in valid_symbols

        except Exception as e:

            logger.error(
                f"Symbol validation failed: {e}"
            )

            raise

    def place_order(
        self,
        symbol: str,
        side: str,
        order_type: str,
        quantity: float,
        price: float = None
    ):

        symbol = symbol.upper()

        if not self.validate_symbol(symbol):

            raise ValueError(
                f"Invalid symbol: {symbol}"
            )

        try:

            params = {
                "symbol": symbol,
                "side": side.upper(),
                "type": order_type.upper(),
                "quantity": quantity
            }

            if order_type.upper() == "LIMIT":

                params["price"] = price
                params["timeInForce"] = "GTC"

            logger.info(
                f"ORDER REQUEST: {params}"
            )

            response = (
                self.client.futures_create_order(
                    **params
                )
            )

            logger.info(
                f"ORDER RESPONSE: {response}"
            )

            return response

        except BinanceAPIException as e:

            logger.error(
                f"Binance API Error: "
                f"{e.code} | {e.message}"
            )

            raise

        except RequestException as e:

            logger.error(
                f"Network Error: {e}"
            )

            raise

        except Exception as e:

            logger.error(
                f"Unexpected Error: {e}"
            )

            raise

    def get_order_details(
        self,
        symbol: str,
        order_id: int
    ):

        try:

            response = (
                self.client.futures_get_order(
                    symbol=symbol,
                    orderId=order_id
                )
            )

            logger.info(
                f"ORDER DETAILS: {response}"
            )

            return response

        except Exception as e:

            logger.error(
                f"Failed to fetch order: {e}"
            )

            raise

