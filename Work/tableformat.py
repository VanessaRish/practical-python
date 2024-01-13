class TableFormatter:
    def headings(self, headers):
        """
        Emit the table headings.
        """
        raise NotImplementedError()

    def row(self, row_data):
        """
        Emit a single row of table data.
        """
        raise NotImplementedError()


class TextTableFormatter(TableFormatter):
    """
    Emit a table in plain-text format.
    """

    def headings(self, headers):
        for header in headers:
            print(f"{header:>10s}", end=" ")
        print()
        print(("-" * 10 + " ") * len(headers))

    def row(self, row_data):
        for item in row_data:
            print(f"{item:>10s}", end=" ")
        print()


class CSVTableFormatter(TableFormatter):
    """
    Output portfolio data in CSV format.
    """

    def headings(self, headers):
        print(",".join(headers))

    def row(self, row_data):
        print(",".join(row_data))


class HTMLTableFormatter(TableFormatter):
    def headings(self, headers):
        print("<tr><th>" + "<tr><th>".join(headers) + "<tr><th>")

    def row(self, row_data):
        print("<tr><th>" + "<tr><th>".join(row_data) + "<tr><th>")


def create_formatter(name):
    if name == "txt":
        return TextTableFormatter()
    elif name == "csv":
        return CSVTableFormatter()
    elif name == "html":
        return HTMLTableFormatter()
    else:
        raise RuntimeError(f"Unknown format {name}")


def print_table(data, columns, formatter):
    formatter.headings(columns)
    for item in data:
        formatter.row([str(item.__getattribute__(col_name)) for col_name in columns])
