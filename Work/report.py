# report.py
#
# Exercise 2.4
import sys

from fileparse import parse_csv
from stock import Stock
import tableformat


def read_portfolio(file_name):
    """
    Read a stock portfolio file into a list of dictionaries with keys
    name, shares, and price.
    """
    with open(file_name) as file:
        portfolio = parse_csv(
            file, types=[str, int, float], select=["name", "shares", "price"]
        )
    return [Stock(p["name"], p["shares"], p["price"]) for p in portfolio]


def read_prices(file_name):
    """
    Read a CSV file of price data into a dict mapping names to prices.
    """
    with open(file_name) as file:
        prices = parse_csv(file, types=[str, float], has_headers=False)
    return dict(prices)


def make_report(portfolio, prices):
    """
    Make a list of (name, shares, price, change) tuples given a portfolio list
    and prices dictionary.
    """
    stocks = []
    for stock in portfolio:
        if stock.name in prices:
            stocks.append(
                (
                    stock.name,
                    stock.shares,
                    round(prices[stock.name], 2),
                    prices[stock.name] - stock.price,
                )
            )
    return stocks


def print_report(report, formatter):
    """
    Print a nicely formated table from a list of (name, shares, price, change) tuples.
    """
    formatter.headings(["Name", "Shares", "Price", "Change"])
    for name, shares, price, change in report:
        rowdata = [name, str(shares), f"{price:0.2f}", f"{change:0.2f}"]
        formatter.row(rowdata)


def portfolio_report(portfolio_file, prices_file, fmt="txt"):
    """
    Make a stock report given portfolio and price data files.
    """
    portfolio = read_portfolio(portfolio_file)
    prices = read_prices(prices_file)
    report = make_report(portfolio, prices)

    formatter = tableformat.create_formatter(fmt)
    print_report(report, formatter)


def main(args_list):
    return portfolio_report(args_list[1], args_list[2], args_list[3])


if __name__ == "__main__":
    main(sys.argv)
