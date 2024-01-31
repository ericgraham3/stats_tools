# import packages
import pandas as pd
import numpy as np

import matplotlib.pyplot as plt


class Frequency:
    def __init__(self, user_csv):
        self.user_csv = user_csv
        self.df = pd.read_csv(self.user_csv)

    def frequency_table(self):
        freq_table = pd.crosstab(self.df.iloc[:, 0], 'frequency')

        # count data points in dataset and take square root of that value to determine number of bins in histogram
        n_data = len(data)
        n_bins = np.sqrt(n_data)
        n_bins = n_bins.astype(int)

        # create and show histogram and frequency table
        plt.hist(self.df, bins=n_bins)
        plt.show()
        print(freq_table)
