import argparse


def parse_arguments():

    parser = argparse.ArgumentParser(
        description="Binance Futures Trading Bot"
    )

    parser.add_argument(
        "--symbol",
        required=True
    )

    parser.add_argument(
        "--side",
        required=True,
        choices=["BUY", "SELL"]
    )

    parser.add_argument(
        "--type",
        required=True,
        choices=["MARKET", "LIMIT"]
    )

    parser.add_argument(
        "--quantity",
        required=True,
        type=float
    )

    parser.add_argument(
        "--price",
        type=float
    )

    return parser.parse_args()