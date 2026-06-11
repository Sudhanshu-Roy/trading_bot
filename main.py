from cli.commands import parse_arguments
from client.binance_client import BinanceFuturesClient

from binance.exceptions import BinanceAPIException

import time


def main():

    args = parse_arguments()

    try:

        # -------------------------
        # Input Validation
        # -------------------------

        if args.quantity <= 0:
            raise ValueError(
                "Quantity must be greater than 0."
            )

        if (
            args.type == "LIMIT"
            and args.price is None
        ):
            raise ValueError(
                "Price is required for LIMIT orders."
            )

        if (
            args.type == "LIMIT"
            and args.price <= 0
        ):
            raise ValueError(
                "Price must be greater than 0."
            )

        # -------------------------
        # Print Order Request
        # -------------------------

        print("\n===== ORDER REQUEST =====")

        print(f"Symbol   : {args.symbol}")
        print(f"Side     : {args.side}")
        print(f"Type     : {args.type}")
        print(f"Quantity : {args.quantity}")

        if args.type == "LIMIT":
            print(f"Price    : {args.price}")

        # -------------------------
        # Create Client
        # -------------------------

        client = BinanceFuturesClient()

        # -------------------------
        # Place Order
        # -------------------------

        order = client.place_order(
            symbol=args.symbol,
            side=args.side,
            order_type=args.type,
            quantity=args.quantity,
            price=args.price
        )

        print("\nOrder Submitted Successfully!")

        print(
            f"Order ID : "
            f"{order['orderId']}"
        )

        # -------------------------
        # Wait For Exchange Update
        # -------------------------

        time.sleep(2)

        # -------------------------
        # Get Final Order Details
        # -------------------------

        details = client.get_order_details(
            args.symbol,
            order["orderId"]
        )

        print("\n===== ORDER RESPONSE =====")

        print(
            f"Order ID      : "
            f"{details.get('orderId')}"
        )

        print(
            f"Status        : "
            f"{details.get('status')}"
        )

        print(
            f"Executed Qty  : "
            f"{details.get('executedQty')}"
        )

        avg_price = (
            details.get("avgPrice")
        )

        print(
        f"Average Price : "
        f"{details.get('avgPrice', 'N/A')}"
        )

        print("\nSUCCESS")

    except ValueError as e:

        print(
            f"\nInput Error: {e}"
        )

    except BinanceAPIException as e:

        print(
            f"\nBinance API Error: "
            f"{e.message}"
        )

    except Exception as e:

        print(
            f"\nUnexpected Error: {e}"
        )


if __name__ == "__main__":
    main()