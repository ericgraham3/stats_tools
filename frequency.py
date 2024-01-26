# import packages
import pandas as pd
import numpy as np

import matplotlib.pyplot as plt

# reading csv file as pandas dataframe
data = pd.read_csv('table.csv')

# create frequency table
freq_table = pd.crosstab(data.iloc[:, 0], 'frequency')

# count data points in dataset and take square root of that value to determine number of bins in histogram
n_data = len(data)
n_bins = np.sqrt(n_data)
n_bins = n_bins.astype(int)

# create and show histogram and frequency table
plt.hist(data, bins=n_bins)
plt.show()
print(freq_table)
