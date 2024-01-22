from random_sample import RandomSample

# This is a sort of "main" file for testing/running functions from other classes

# create random table object
sample = RandomSample(1, 100)

table = sample.random_table(2000, 1, True)

print(table)
