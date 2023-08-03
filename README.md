# Yang-Zhang-s-Realized-Volatility-Automated-Estimation-in-Python
This software automatizes the estimation of Yang &amp; Zhang's RV proxy for financial securities

# Content
The Python Code named as Yang_Zhang_RV_proxy.py estimates Yang & Zhang's Realized Volatility from high-frequency intraday stock data. It contains four functions: Yang_Zhang_RV_yahoo, Yang_Zhang_RV_own_data, Multivariate_Yang_Zhang_RV_own_data, and Multivariate_Yang_Zhang_RV_yahoo. The functions containing 'yahoo' in their name make use of Yahoo Finance's API through the Python library yfinance. Additionally, in the folder Examples, examples in Jupyter Notebooks of the code use can be found for univariate and multivariate data with common mistakes made when using the code.

# Functions Description
Yang_Zhang_RV_yahoo(tickers, start=None, end=None, period=None, interval=None)

Needed parameters: tickers = list containing stock's ticker as shown in Yahoo Finance (e.g. ["^GSPC"], ["^IXIC"], ["^RUT"], ["^DJI"], etc), interval = string containing the frequency of data (e.g. "1m", "5m", "15m", "30m", etc.)

Semi-optional parameters: start = date from when the data extraction should start (e.g. "2004-12-30", "2005-12-30", "2006-12-30", etc.), end = date when the data extraction should end (e.g. "2020-12-30", "2021-12-30", "2022-12-30", etc.), period = number of days ago that the data extraction should consider (should be used only if start and end parameters are not used, and vice-versa) (e.g. "7d", "30d", "60d", etc.)

Yang_Zhang_RV_own_data(data)

Needed parameters: data = Pandas DataFrame containing an index named "Date" and with DatetimeIndex as data type, and the following columns: "Close": high-frequency intraday stock close prices, "Open": high-frequency intraday stock open prices, "High": high-frequency intraday stock high prices, "Low": high-frequency intraday stock low prices (the order of the columns is not important).

Multivariate_Yang_Zhang_RV_own_data(data_list)

Needed parameters: data_list = a list containing Pandas DataFrames containing an index named "Date" and with DatetimeIndex as data type, and the following columns: "Close": high-frequency intraday stock close prices, "Open": high-frequency intraday stock open prices, "High": high-frequency intraday stock high prices, "Low": high-frequency intraday stock low prices (the order of the columns is not important).

Multivariate_Yang_Zhang_RV_yahoo(tickers, start=None, end=None, period=None, interval=None)

Needed parameters: tickers = list containing stocks' tickers as shown in Yahoo Finance (e.g. ["^GSPC", "^IXIC", "^RUT", "^DJI"]), interval = string containing the frequency of data (e.g. "1m", "5m", "15m", "30m", etc.)

Semi-optional parameters: start = date from when the data extraction should start (e.g. "2004-12-30", "2005-12-30", "2006-12-30", etc.), end = date when the data extraction should end (e.g. "2020-12-30", "2021-12-30", "2022-12-30", etc.), period = number of days ago that the data extraction should consider (should be used only if start and end parameters are not used, and vice-versa) (e.g. "7d", "30d", "60d", etc.)

# Authors

@authors: Hugo Gobato Souto* and Amir Moradi**

*International School of Business at HAN University of Applied Sciences, Ruitenberglaan 31, 
6826 CC Arnhem, the Netherlands; H.GobatoSouto@han.nl; https://orcid.org/0000-0002-7039-0572

Contact author.
**International School of Business at HAN University of Applied Sciences, Ruitenberglaan 31, 
6826 CC Arnhem, the Netherlands; amir.moradi@han.nl; https://orcid.org/0000-0003-1169-7192.
