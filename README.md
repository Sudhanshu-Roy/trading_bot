# Binance Futures Testnet Trading Bot

## Overview

This project is a Python-based trading bot that interacts with the Binance Futures Testnet (USDT-M). The application allows users to place MARKET and LIMIT orders from the command line while providing input validation, structured logging, and error handling.

The project was developed as part of an application task to demonstrate API integration, software design, and Python programming skills.

---

## Features

* Place MARKET orders
* Place LIMIT orders
* Supports BUY and SELL sides
* Command-line interface using argparse
* Input validation
* Structured project architecture
* Detailed logging of requests, responses, and errors
* Binance server time synchronization to prevent timestamp errors
* Exception handling for:

  * Invalid user input
  * Binance API errors
  * Network failures

---

## Project Structure

```text
trading_bot/
│
├── main.py
├── config.py
├── logger.py
├── requirements.txt
│
├── client/
│   └── binance_client.py
│
├── cli/
│   └── commands.py
│
├── logs/
│   ├── market_order.log
│   ├── limit_order.log
│   └── trading_bot.log
│
├── .env
│
├── streamlit_app.py
└── README.md
```

---

## Requirements

* Python 3.10+
* Binance Futures Demo/Testnet Account
* Binance API Key and Secret Key

---

## Installation

### 1. Clone Repository

```bash
git clone https://github.com/Sudhanshu-Roy/trading_bot
cd trading_bot
```

### 2. Create Virtual Environment

```bash
python -m venv venv
```

Activate:

Windows:

```bash
venv\Scripts\activate
```

Linux/Mac:

```bash
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file in the project root:

```env
API_KEY=your_api_key
API_SECRET=your_api_secret
```

---

## Usage

### MARKET BUY Order

```bash
python main.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001
```

### MARKET SELL Order

```bash
python main.py --symbol BTCUSDT --side SELL --type MARKET --quantity 0.001
```

### LIMIT BUY Order

```bash
python main.py --symbol BTCUSDT --side BUY --type LIMIT --quantity 0.001 --price 50000
```

### LIMIT SELL Order

```bash
python main.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.001 --price 120000
```

---

## Example Output

```text
===== ORDER REQUEST =====

Symbol   : BTCUSDT
Side     : BUY
Type     : MARKET
Quantity : 0.001

Order Submitted Successfully!
Order ID : 14793127322

===== ORDER RESPONSE =====

Order ID      : 14793127322
Status        : FILLED
Executed Qty  : 0.0010
Average Price : 62896.000000

SUCCESS
```

---

## Logging

All API activity is logged to:

```text
logs/trading_bot.log
```

Logged information includes:

* Timestamp synchronization
* Order requests
* Order responses
* Final order details
* Validation failures
* API errors
* Unexpected exceptions

Sample log entry:

```text
2026-06-11 19:58:00 | INFO | ORDER REQUEST: {...}
2026-06-11 19:58:00 | INFO | ORDER RESPONSE: {...}
2026-06-11 19:58:02 | INFO | ORDER DETAILS: {...}
```

---

## Error Handling

The application handles:

### Input Validation

* Invalid symbol
* Missing LIMIT order price
* Negative quantity
* Invalid order type

### API Errors

* Authentication failures
* Invalid order parameters
* Exchange-side errors

### Network Errors

* Connection failures
* Request timeouts

---

## Design Decisions

### Separation of Concerns

The project separates responsibilities into dedicated modules:

* CLI Layer → User input handling
* Client Layer → Binance API communication
* Logging Layer → Centralized logging
* Configuration Layer → Environment management

### Timestamp Synchronization

Binance requires signed requests to use synchronized timestamps. The client automatically synchronizes local time with Binance server time during initialization.

---

## Assumptions

* User has a valid Binance Futures Demo/Testnet account.
* API credentials are stored in a local `.env` file.
* Internet connectivity is available.
* Orders are placed only on Binance Futures Demo/Testnet, not on the live exchange.

---

## Bonus Feature

Enhanced CLI experience with:

* Argument validation
* Helpful error messages
* Structured terminal output
* Clear success and failure notifications

Streamlit UI

Launch:

```
streamlit run streamlit_app.py
```
<img width="1453" height="934" alt="Screenshot 2026-06-11 203020" src="https://github.com/user-attachments/assets/60e4bd0e-8e26-4fe4-bff8-97b81854a822" />


This provides a lightweight graphical interface
for placing Futures Testnet orders in addition
to the required CLI interface.

---

## Author

Sudhanshu Roy
