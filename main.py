#(5/5 points) Initial comments with your name, class and project at the top of your .py file.
# INF601 - Advanced Programming in Python
# Joshua Seirer
# Mini Project 1

#(5/5 points) Proper import of packages used.
import yfinance as yf
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

#(20/20 points) Using an API of your choice (yfinance works), collect the closing price of 5 of your favorite stock
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
try:
    Path("Charts").mkdir()
except FileExistsError:
    pass

stocks = ["MSFT", "AAPL", "GME", "SONY", "META"]

for stock in stocks:
    mstfClosing = np.array(getClosing(stock))
    days = list(range(1, len(mstfClosing) + 1))
    # Plots graph
    plt.plot(days, mstfClosing)


    prices = getClosing(stock)
    prices.sort()
    low_price = prices[0]
    high_price = prices[-1]

    # form [xmin, xmax, ymin, ymax]
    plt.axis([1, 10, low_price-2, high_price+2])

    # Sets x and y labels
    plt.xlabel("Days")
    plt.ylabel("Closing Price")
    plt.title("Closing Price for " + stock)

    saveFile = "Charts/" + stock + ".png"
    plt.savefig(saveFile)

    plt.show()




#(10/10 points) Store this information in a list that you will convert to a ndarray in NumPy.
#(10/10 points) Plot these 5 graphs. Feel free to add as much information to the graphs as you like exploring the
# documentation for matplotlib. At minimum it just needs to show 10 data points.
#(10/10 points) Save these graphs in a folder called charts as PNG files. Do not upload these to your project folder,
# the project should save these when it executes. You may want to add this folder to your .gitignore file.
#(10/10 points) There should be a minimum of 5 commits on your project, be sure to commit often!
#(10/10 points) I will be checking out the master branch of your project. Please be sure to include a requirements.txt
# file which contains all the packages that need installed. You can create this fille with the output of pip freeze at
# the terminal prompt.
#(20/20 points) There should be a README.md file in your project that explains what your project is, how to install
# the pip requirements, and how to execute the program. Please use the GitHub flavor of Markdown.