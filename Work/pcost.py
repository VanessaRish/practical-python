import sys
import csv


def portfolio_cost(file_name):
    total_amount = 0
    with open(file_name, "r") as file:
        lines = csv.reader(file)
        headers = next(lines)
        for rowno, row in enumerate(lines, start=1):
            record = dict(zip(headers, row))
            try:
                nshares = int(record['shares'])
                price = float(record['price'])
                total_amount += nshares * price
            except ValueError as e:
                print(f'Row {rowno}: Bad row: {row}')
                continue
    return total_amount


filename = "./Data/portfoliodate.csv"
if len(sys.argv) == 2:
    filename = sys.argv[1]

cost = portfolio_cost(filename)
print(f"Total cost: {cost}")
