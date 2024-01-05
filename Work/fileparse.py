# fileparse.py
#
# Exercise 3.3
import csv


def parse_csv(filename, select=None, types=None, has_headers=True, delimiter=','):
    """
    Parse a CSV file into a list of records with type conversion
    """
    with open(filename) as f:
        rows = csv.reader(f, delimiter=delimiter)
        headers = next(rows) if has_headers else []
        if select:
            indices = [headers.index(col_name) for col_name in select]
            headers = select
        records = []
        for row in rows:
            if not row:
                continue
            if select:
                row = [row[index] for index in indices]
            if types:
                row = [func(val) for func, val in zip(types, row)]
            if has_headers:
                records.append(dict(zip(headers, row)))
            else:
                records.append(tuple(row))
    return records
