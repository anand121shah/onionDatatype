import pandas as pd

# Create DataFrames
df1 = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
df2 = pd.DataFrame({'X': [7, 8, 9], 'Y': [10, 11, 12]})

# Create an instance of Onion with initial subsets, including DataFrames
my_onion = Onion([df1, df2])

# Add a new DataFrame subset
df3 = pd.DataFrame({'C': [13, 14, 15], 'D': [16, 17, 18]})
my_onion.add_subset(df3)

# Remove a subset by index
my_onion.remove_subset(1)

# Perform a statistical operation on the Onion data (e.g., mean)
my_onion.perform_operation('mean')
