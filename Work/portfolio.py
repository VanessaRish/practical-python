from collections import Counter
import stock
from fileparse import parse_csv


class Portfolio:
    def __init__(self):
        self._holdings = []

    @classmethod
    def from_csv(cls, lines, **opts):
        self = cls()
        portfolio_dict = parse_csv(
            lines, types=[str, int, float], select=["name", "shares", "price"], **opts
        )
        for d in portfolio_dict:
            self.append(stock.Stock(**d))
        return self

    def append(self, holding):
        if not isinstance(holding, stock.Stock):
            raise TypeError("Expected a Stock instance")
        self._holdings.append(holding)

    def __iter__(self):
        return self._holdings.__iter__()

    def __len__(self):
        return len(self._holdings)

    def __getitem__(self, index):
        return self._holdings[index]

    def __contains__(self, name):
        return any(s.name == name for s in self._holdings)

    @property
    def total_cost(self):
        return sum(s.cost for s in self._holdings)

    def tabulate_shares(self):
        total_shares = Counter()
        for s in self._holdings:
            total_shares[s.name] += s.shares
        return total_shares
