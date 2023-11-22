import sys
import csv


def portfolio_cost(filename):
    total_amount = 0
    with open(filename, "r") as file:
        lines = csv.reader(file)
        _ = next(lines)
        for line in lines:
            try:
                total_amount += int(line[1]) * float(line[2])
            except ValueError as e:
                print("Value is missing!")
                print(e)
                continue
    return total_amount


filename = "./Data/portfolio.csv"
if len(sys.argv) == 2:
    filename = sys.argv[1]

cost = portfolio_cost(filename)
print(f"Total cost: {cost}")
