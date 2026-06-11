import streamlit as st
from binance.exceptions import BinanceAPIException

from client.binance_client import BinanceFuturesClient

st.set_page_config(
    page_title="Binance Futures Trading Bot",
    page_icon="📈",
    layout="centered"
)

st.title("📈 Binance Futures Trading Bot")
st.markdown(
    "Place MARKET and LIMIT orders on Binance Futures Testnet."
)

try:
    client = BinanceFuturesClient()

except Exception as e:
    st.error(f"Failed to connect to Binance: {e}")
    st.stop()

# -------------------------
# Form
# -------------------------

with st.form("order_form"):

    symbol = st.text_input(
        "Symbol",
        value="BTCUSDT"
    ).upper()

    side = st.selectbox(
        "Side",
        ["BUY", "SELL"]
    )

    order_type = st.selectbox(
        "Order Type",
        ["MARKET", "LIMIT"]
    )

    quantity = st.number_input(
        "Quantity",
        min_value=0.0001,
        value=0.001,
        step=0.001,
        format="%.4f"
    )

    price = None

    if order_type == "LIMIT":

        price = st.number_input(
            "Price",
            min_value=0.01,
            value=50000.0,
            step=100.0
        )

    submit = st.form_submit_button(
        "Place Order"
    )

# -------------------------
# Submit Logic
# -------------------------

if submit:

    try:

        st.subheader("Order Request")

        st.write(
            {
                "Symbol": symbol,
                "Side": side,
                "Type": order_type,
                "Quantity": quantity,
                "Price": price
            }
        )

        order = client.place_order(
            symbol=symbol,
            side=side,
            order_type=order_type,
            quantity=quantity,
            price=price
        )

        order_id = order["orderId"]

        details = client.get_order_details(
            symbol=symbol,
            order_id=order_id
        )

        st.success("Order Submitted Successfully!")

        st.subheader("Order Response")

        st.write(
            {
                "Order ID": details.get("orderId"),
                "Status": details.get("status"),
                "Executed Qty": details.get("executedQty"),
                "Average Price": details.get("avgPrice"),
            }
        )

    except ValueError as e:

        st.error(f"Validation Error: {e}")

    except BinanceAPIException as e:

        st.error(
            f"Binance API Error: {e.message}"
        )

    except Exception as e:

        st.error(
            f"Unexpected Error: {e}"
        )