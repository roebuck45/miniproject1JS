# INF601 - Advanced Programming in Python
# Joshua Seirer
# Mini Project 1

# pip freeze > requirements.txt

import yfinance as yf
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path


# tickers for the last 10 trading days.
# Apple is is AAPL
# Mircosoft is MSFT

def getClosing(ticker):
    stock = yf.Ticker(ticker)
    # get historical market data.
    hist = stock.history(period="10d")

    closingList = []

    for price in hist['Close']:
        closingList.append(round(price,2))
    return closingList
def getStocks():
    stock = []
    print("Please pick 5 stocks")
    for i in range(1, 6):
        while True:
            print("Enter stock trick number " + str(i))
            ticker = input("> ")
             try:
                stock = yf.Ticker(ticker)
                stock.info
                stocks.append(ticker)
                break
            except:
                print("Not valdi")

# Create our "Charts" directory
try:
    Path("Charts").mkdir()
except FileExistsError:
    pass

stocks = ["MSFT", "AAPL", "GME", "SONY", "META"]

for stock in getStocks():
    mstfClosing = np.array(getClosing(stock))
    days = list(range(1, len(mstfClosing) + 1))
    # Plots graph
    plt.plot(days, mstfClosing)

    # Get our min and max for Y
    prices = getClosing(stock)
    prices.sort()
    low_price = prices[0]
    high_price = prices[-1]

    # Set out X axis min and max
    # form [xmin, xmax, ymin, ymax]
    plt.axis([1, 10, low_price-2, high_price+2])

    # Set out labels for the graph
    plt.xlabel("Days")
    plt.ylabel("Closing Price")
    plt.title("Closing Price for " + stock)

    # Saves plot
    saveFile = "Charts/" + stock + ".png"
    plt.savefig(saveFile)

    # Show the the graph
    plt.show()
