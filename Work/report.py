# report.py
#
# Exercise 2.4
import csv


def read_portfolio(file_name):
    """
    Read a stock portfolio file into a list of dictionaries with keys
    name, shares, and price.
    """
    portfolio = []
    with open(file_name, "rt") as file:
        rows = csv.reader(file)
        headers = next(rows)
        for rowno, row in enumerate(rows, start=1):
            try:
                record = dict(zip(headers, row))
                portfolio.append(
                    {
                        "name": record['name'],
                        "shares": int(record['shares']),
                        "price": float(record['price']),
                    }
                )
            except Exception as e:
                print(f'Row {rowno}: Bad row: {row}')
                continue

    return portfolio


def read_prices(file_name):
    """
    Read a CSV file of price data into a dict mapping names to prices.
    """
    prices = {}
    with open(file_name, "rt") as file:
        rows = csv.reader(file)
        for row in rows:
            if len(row) > 1:
                prices[row[0]] = float(row[1])
    return prices


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
    headers = ('Name', 'Shares', 'Price', 'Change')
    print(f"{headers[0]:>10s} {headers[1]:>10s} {headers[2]:>10s} {headers[3]:>10s}")
    print(f"{10 * '-':>10s} {10 * '-':>10s} {10 * '-':>10s} {10 * '-':>10s}")
    for row in report:
        print('{:>10s} {:>10d} {:>10s} {:>10.2f}'.format(*row))


def portfolio_report(portfolio_file, prices_file):
    """
    Make a stock report given portfolio and price data files.
    """
    portfolio = read_portfolio(portfolio_file)
    prices = read_prices(prices_file)
    make_report(portfolio, prices)


portfolio_report("Data/portfoliodate.csv", "Data/prices.csv")
