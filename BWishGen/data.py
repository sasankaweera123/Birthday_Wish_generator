import pandas as pd


class Data:

    def __init__(self, path):
        self.path = path
        self.data = pd.read_csv(self.path)

    def get_data(self):
        return self.data

    def get_column(self, column):
        return self.data[column]

    def get_row(self, row):
        return self.data.iloc[row]

    def get_cell(self, row, column):
        return self.data.iloc[row][column]

    def get_row_count(self):
        return self.data.shape[0]

    def get_column_count(self):
        return self.data.shape[1]

    def get_column_names(self):
        return self.data.columns

    def get_column_type(self, column):
        return self.data.dtypes[column]








