# What is Pandas?
# Pandas is a popular open-source data manipulation and analysis library for the Python programming language. It provides a powerful and flexible set of tools for working with structured data, making it a fundamental tool for data scientists, analysts, and engineers.
# Pandas is designed to handle data in various formats, such as tabular data, time series data, and more, making it an essential part of the data processing workflow in many industries.

# Here are some key features and functionalities of Pandas:

# Data Structures: Pandas offers two primary data structures - DataFrame and Series.

# A DataFrame is a two-dimensional, size-mutable, and potentially heterogeneous tabular data structure with labeled axes (rows and columns).
# A Series is a one-dimensional labeled array, essentially a single column or row of data.
# Data Import and Export: Pandas makes it easy to read data from various sources, including CSV files, Excel spreadsheets, SQL databases, and more. It can also export data to these formats, enabling seamless data exchange.

# Data Merging and Joining: You can combine multiple DataFrames using methods like merge and join, similar to SQL operations, to create more complex datasets from different sources.

# Efficient Indexing: Pandas provides efficient indexing and selection methods, allowing you to access specific rows and columns of data quickly.

# Custom Data Structures: You can create custom data structures and manipulate data in ways that suit your specific needs, extending Pandas' capabilities.

import pandas as pd

# Create a Series from a list
data = [10, 20, 30, 40, 50]
s = pd.Series(data)
print(s)

print(s[2])     # Access the element with label 2 (value 30)
print(s.iloc[3]) # Access the element at position 3 (value 40)
print(s[1:4])   # Access a range of elements by label

# Creating a DataFrame from a dictionary
data = {'Name': ['Alice', 'Bob', 'Charlie', 'David'],
        'Age': [25, 30, 35, 28],
        'City': ['New York', 'San Francisco', 'Los Angeles', 'Chicago']}
df = pd.DataFrame(data)
print(df)

print(df['Name'])  # Access the 'Name' column
print(df.iloc[2])   # Access the third row by position
print(df.loc[1])    # Access the second row by label
print(df[['Name', 'Age']])  # Select specific columns
print(df[1:3])             # Select specific rows

# Finding Unique Elements:
# Use the unique method to determine the unique elements in a column of a DataFrame.

unique_dates = df['Age'].unique()

# Conditional Filtering:
# You can filter data in a DataFrame based on conditions using inequality operators.
# For instance, you can filter albums released after a certain year.

high_above_102 = df[df['Age'] > 25]

# Saving DataFrames:
# To save a DataFrame to a CSV file, use the to_csv method and specify the filename with a “.csv” extension.Pandas provides other functions for saving DataFrames in different formats.

df.to_csv('trading_data.csv', index=False)