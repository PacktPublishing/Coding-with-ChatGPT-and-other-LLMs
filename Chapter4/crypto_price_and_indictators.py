# -*- coding: utf-8 -*-
"""
Created on Fri Apr 12 13:31:27 2024

@author: Vincent Hall and Gemini from Alphabet.
I don't know what this code does, Gemini just gave it to me.
"""
# Gemini code corrected by Claude.
import requests
from datetime import datetime, timedelta
import pandas as pd
import matplotlib.pyplot as plt

def fetch_data(url, params):
    response = requests.get(url, params=params)
    response.raise_for_status()  # Raise an exception for non-200 status codes
    return response.json()

def calculate_indicators(data):
    # Convert 'Close' column to float
    data['Close'] = data['Close'].astype(float)
    data["SMA"] = data["Close"].rolling(window=20).mean()
    data["RSI"] = calculate_rsi(data["Close"])
    return data

def calculate_rsi(closes, window=14):
    delta = closes.diff()
    delta = delta.dropna()
    gains = delta[delta > 0]
    losses = -delta[delta < 0]
    avg_gain = gains.ewm(alpha=1/window, min_periods=window).mean()
    avg_loss = losses.ewm(alpha=1/window, min_periods=window).mean().abs()
    rsi = 100 - 100 / (1 + avg_gain / avg_loss)
    return rsi

def plot_data(data, title):
    data[["Close", "SMA"]].plot(figsize=(12, 6), style=["b-", "g-"])
    data["RSI"].plot(ax=plt.twinx(), style="r-")
    plt.title(title)
    plt.show()

if __name__ == "__main__":
    base_url = "https://api.binance.com/api/v3/klines"
    symbol = "BTCUSDT"
    interval = "1d"  # Daily data

    today = datetime.utcnow()
    one_year_ago = today - timedelta(days=365)

    params = {
        "symbol": symbol,
        "interval": interval,
        "startTime": int(one_year_ago.timestamp() * 1000),  # Convert to Unix timestamp in milliseconds
        "endTime": int(today.timestamp() * 1000),  # Convert to Unix timestamp in milliseconds
    }

    data = fetch_data(base_url, params)
    data = pd.DataFrame(data)
    data.columns = ["Open Time", "Open", "High", "Low", "Close", "Volume", "Close Time", "Quote Asset Volume", "Number of Trades", "Taker Buy Base Asset Volume", "Taker Buy Quote Asset Volume", "Ignore"]
    data["Open Time"] = pd.to_datetime(data["Open Time"], unit="ms")
    data.set_index("Open Time", inplace=True)
    data = calculate_indicators(data.copy())
    plot_data(data, f"{symbol} Price & Indicators (Past Year)")


