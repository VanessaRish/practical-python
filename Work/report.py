# report.py
#
# Exercise 2.4
import csv


def read_portfolio(file_name):
    portfolio = []
    with open(file_name, "rt") as file:
        rows = csv.reader(file)
        next(rows)
        for row in rows:
            portfolio.append({
                'name': row[0],
                'shares': int(row[1]),
                'price': float(row[2]),
            })

    return portfolio


def read_prices(file_name):
    prices = {}
    with open(file_name, "rt") as file:
        rows = csv.reader(file)
        for row in rows:
            if len(row) > 1:
                prices[row[0]] = float(row[1])
    return prices


def calculate_current_value():
    portfolio = read_portfolio("./Data/portfolio.csv")
    prices = read_prices("./Data/prices.csv")
    previous_portfolio = current_portfolio = 0
    for stock in portfolio:
        previous_portfolio += stock['shares'] * stock['price']
        if stock['name'] in prices:
            current_portfolio += stock['shares'] * prices[stock['name']]
    print(f'Previous portfolio value: {previous_portfolio}')
    print(f'Current portfolio value: {current_portfolio}')
    difference = current_portfolio - previous_portfolio
    if difference > 0:
        print(f'Gained: {difference}')
    else:
        print(f'Lost: {difference}')


calculate_current_value()
