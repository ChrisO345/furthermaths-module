class Matrix:
    def __init__(self, rows, columns, *args):
        self.rows = rows
        self.columns = columns
        if len(args) == 1 and type(args[0]) == list:
            args = args[0]
        if len(args) != rows * columns:
            raise ValueError
        self.values = []
        for i in range(columns):
            self.values.append([])
            for j in range(rows):
                self.values[i].append(args[j + i * rows])