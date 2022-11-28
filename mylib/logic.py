import yfinance as yf
import pandas as pd


def sector(name="META"):
    """This is a ticker sector fetcher"""

    my_ticker = yf.Ticker(name)
    my_info = my_ticker.info
    my_sector = my_info['sector']
    return my_sector


def financials(name="META"):
    """This is a ticker financial data fetcher"""

    my_ticker = yf.Ticker(name)
    my_financials = my_ticker.get_financials()
    return my_financials

