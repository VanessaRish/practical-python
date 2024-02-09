from follow import follow
import csv
import report
import tableformat


def parse_stock_data(lines):
    rows = csv.reader(lines)
    rows = ([row[index] for index in [0, 1, 4]] for row in rows)
    types = [str, float, float]
    rows = ([func(val) for func, val in zip(types, row)] for row in rows)
    rows = (dict(zip(["name", "price", "change"], row)) for row in rows)
    return rows


def ticker(portfolio, logfile, fmt):
    portfolio = report.read_portfolio(portfolio)
    rows = parse_stock_data(follow(logfile))
    rows = (row for row in rows if row["name"] in portfolio)
    formatter = tableformat.create_formatter(fmt)
    formatter.headings(["Name", "Price", "Change"])
    for row in rows:
        formatter.row([row["name"], f"{row['price']:0.2f}", f"{row['change']:0.2f}"])


if __name__ == "__main__":
    pass
