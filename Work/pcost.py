import sys

from report import read_portfolio


def portfolio_cost(file_name):
    total_amount = 0
    portfolio = read_portfolio(file_name)
    for idx, record in enumerate(portfolio):
        try:
            total_amount += record.cost()
        except ValueError as e:
            print(f"Row {idx}: Bad row: {record}")
            continue
    return total_amount


def main(args_list):
    print(f"Total cost: {portfolio_cost(args_list[1])}")


if __name__ == "__main__":
    main(sys.argv)
