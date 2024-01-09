import sys
import csv

from report import read_portfolio


def portfolio_cost(file_name):
    total_amount = 0
    portfolio = read_portfolio(file_name)
    for idx, record in enumerate(portfolio):
        try:
            shares = record['shares']
            price = record['price']
            total_amount += shares * price
        except ValueError as e:
            print(f'Row {idx}: Bad row: {record}')
            continue
    return total_amount


filename = "./Data/portfoliodate.csv"
if len(sys.argv) == 2:
    filename = sys.argv[1]

cost = portfolio_cost(filename)
print(f"Total cost: {cost}")
