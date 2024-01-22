# import packages
import pandas as pd
import numpy as np

import matplotlib.pyplot as plt

# reading csv file as pandas dataframe
data = pd.read_csv('table.csv')

# one way frequency table for the species column.
freq_table = pd.crosstab(data.iloc[:, 0], 'frequency')
bins = [10, 20, 30, 40, 50, 60, 70, 80, 90]
plt.hist(data, bins=bins)
plt.show()
print(freq_table)
