import sys

from report import read_portfolio


def portfolio_cost(file_name):
    total_amount = 0
    portfolio = read_portfolio(file_name)
    return portfolio.total_cost


def main(args_list):
    print(f"Total cost: {portfolio_cost(args_list[1])}")


if __name__ == "__main__":
    main(sys.argv)
