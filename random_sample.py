import random as rm
import pandas as pd


class RandomSample:
    """Class for generating random samples."""
    def __init__(self, min_value: int, max_value: int):
        """Initialize the RandomSample class and set it's min/max values."""
        self.min_value = min_value
        self.max_value = max_value

    def random_table(self, rows: int, columns: int, export: bool = False):
        """Returns a multidimensional list of size [columns][rows] filled
        with random numbers between the min_value and max_value of the RandomSample object.
        If export flag is True, the table will be exported to CSV.
        """
        random_list = [[rm.randint(self.min_value, self.max_value) for x in range(columns)] for y in range(rows)]
        if export is True:
            self._export(random_list)
        return random_list

    def _export(self, random_list: list):
        """Convert list to Pandas dataframe and output as CSV"""
        df = pd.DataFrame(random_list)
        df.to_csv('table.csv', header=False, index=False, sep=',')
