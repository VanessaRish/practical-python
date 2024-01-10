# fileparse.py
#
# Exercise 3.3
import csv


def parse_csv(
    file_object,
    select=None,
    types=None,
    has_headers=True,
    delimiter=",",
    silence_errors=False,
):
    """
    Parse a CSV file into a list of records with type conversion
    """
    if isinstance(file_object, str):
        print("Wrong file object format, should be iterable")
        raise TypeError
    if select and not has_headers:
        raise RuntimeError("select argument requires column headers")
    # with open(filename) as f:
    rows = [r.strip().replace('"', "").split(delimiter) for r in file_object]
    headers = rows.pop(0) if has_headers else []
    if select:
        indices = [headers.index(col_name) for col_name in select]
        headers = select
    records = []
    for row_number, row in enumerate(rows, 1):
        if not row or len(row) < 2:
            continue
        if select:
            row = [row[index] for index in indices]
        if types:
            try:
                row = [func(val) for func, val in zip(types, row)]
            except ValueError as e:
                if not silence_errors:
                    print(f"Row {row_number}: Couldn't convert {row}")
                    print(f"Row {row_number}: {e}")
                continue
        if has_headers:
            records.append(dict(zip(headers, row)))
        else:
            records.append(tuple(row))
    return records
