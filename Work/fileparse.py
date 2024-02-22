# fileparse.py
#
# Exercise 3.3
import logging
log = logging.getLogger(__name__)


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
        log.error("Wrong file object format, should be iterable")
        raise TypeError
    if select and not has_headers:
        raise RuntimeError("select argument requires column headers")
    rows = [r.strip().replace('"', "").split(delimiter) for r in file_object]
    headers = rows.pop(0) if has_headers else []
    indices = []
    if select:
        indices = [headers.index(col_name) for col_name in select]
        headers = select
    records = []
    for row_number, row in enumerate(rows, 1):
        if not row or len(row) < 2:
            continue
        if select and indices:
            row = [row[index] for index in indices]
        if types:
            try:
                row = [func(val) for func, val in zip(types, row)]
            except ValueError as e:
                if not silence_errors:
                    log.warning("Row %d: Couldn't convert %s", row_number, row)
                    log.debug("Row %d: Reason %s", row_number, e)
                continue
        if has_headers:
            records.append(dict(zip(headers, row)))
        else:
            records.append(tuple(row))
    return records
