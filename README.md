# Analyzing Stock Prices

In this guided project, we'll work with stock market data that was downloaded from Yahoo Finance using the yahoo_finance Python package. This data consists of the daily stock prices from 2007-1-1 to 2017-04-17 for several hundred stock symbols traded on the NASDAQ stock exchange, stored in the prices folder. The download_data.py script in the same folder as the Jupyter notebook was used to download all of the stock price data. Each file in the prices folder is named for a specific stock symbol, and contains the:

    date -- date that the data is from.
    close -- the closing price on that day, which is the price when the trading day ends.
    open -- the opening price on that day, which is the price when the trading day starts.
    high -- the highest price the stock reached during trading.
    low -- the lowest price the stock reached during trading.
    volume -- the number of shares that were traded during the day.

Here are the first few rows of aapl.csv:
	date 	close 	open 	high 	low 	volume
0 	2007-01-03 	83.800002 	86.289999 	86.579999 	81.899999 	309579900
1 	2007-01-04 	85.659998 	84.050001 	85.949998 	83.820003 	211815100
2 	2007-01-05 	85.049997 	85.770000 	86.199997 	84.400002 	208685400
3 	2007-01-08 	85.470000 	85.959998 	86.529998 	85.280003 	199276700
4 	2007-01-09 	92.570003 	86.450003 	92.979999 	85.150000 	837324600

As you can see, the prices are sorted in ascending order by day. Stock trading doesn't happen on certain days, like weekends and holidays, so there are gaps between days -- we only have data for days on which trading happening.

To read in and store all of the data, we'll need several layers of indices:

    Layer 1 -- the stock symbol, or an numeric index representing the stock symbol.
    Layer 2 -- the rows in a stock symbol csv file.
    Layer 3 -- The column names in a stock symbol csv file.
