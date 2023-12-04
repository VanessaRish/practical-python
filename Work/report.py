# report.py
#
# Exercise 2.4
import csv


def read_portfolio(file_name):
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
    prices = {}
    with open(file_name, "rt") as file:
        rows = csv.reader(file)
        for row in rows:
            if len(row) > 1:
                prices[row[0]] = float(row[1])
    return prices


def make_report(portfolio, prices):
    stocks = []
    headers = ["Name", "Shares", "Price", "Change"]
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
    print(f"{headers[0]:>10s} {headers[1]:>10s} {headers[2]:>10s} {headers[3]:>10s}")
    print(f"{10 * '-':>10s} {10 * '-':>10s} {10 * '-':>10s} {10 * '-':>10s}")
    for stock in stocks:
        print("{:>10s} {:>10d} {:>10s} {:>10.2f}".format(*stock))
    return stocks


portfolio = read_portfolio("Data/portfoliodate.csv")
prices = read_prices("Data/prices.csv")
make_report(portfolio, prices)
