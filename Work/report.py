# report.py
#
# Exercise 2.4
import sys

from fileparse import parse_csv


def read_portfolio(file_name):
    """
    Read a stock portfolio file into a list of dictionaries with keys
    name, shares, and price.
    """
    with open(file_name) as file:
        portfolio = parse_csv(
            file, types=[str, int, float], select=["name", "shares", "price"]
        )
    return portfolio


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
        if stock["name"] in prices:
            stocks.append(
                (
                    stock["name"],
                    stock["shares"],
                    f'${round(prices[stock["name"]], 2)}',
                    stock["price"] - prices[stock["name"]],
                )
            )

    print_report(stocks)


def print_report(report):
    """
    Print a nicely formated table from a list of (name, shares, price, change) tuples.
    """
    headers = ("Name", "Shares", "Price", "Change")
    print(f"{headers[0]:>10s} {headers[1]:>10s} {headers[2]:>10s} {headers[3]:>10s}")
    print(f"{10 * '-':>10s} {10 * '-':>10s} {10 * '-':>10s} {10 * '-':>10s}")
    for row in report:
        print("{:>10s} {:>10d} {:>10s} {:>10.2f}".format(*row))


def portfolio_report(portfolio_file, prices_file):
    """
    Make a stock report given portfolio and price data files.
    """
    portfolio = read_portfolio(portfolio_file)
    prices = read_prices(prices_file)
    make_report(portfolio, prices)


def main(args_list):
    return portfolio_report(args_list[1], args_list[2])


if __name__ == "__main__":
    main(sys.argv)
