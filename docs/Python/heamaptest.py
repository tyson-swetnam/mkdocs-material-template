"""
This code should hopefully show a map of snow's data
"""
import pandas as pd

import matplotlib.pyplot as plt

# Read the spreadsheet data into a pandas DataFrame

df = pd.read_excel('snowdata.xlsx')  # Update with your actual spreadsheet file name

# Extract longitude and latitude columns from the DataFrame
longitude_column = 'longitude'.lower # Update with the actual column name
latitude_column = 'latitude'.lower  # Update with the actual column name

# Create a scatter plot using longitude and latitude as coordinates
plt.scatter(df[longitude_column], df[latitude_column], c='red', marker='o')

# Set the axes labels and title
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.title('Map with Data Points')

# Display the plot

plt.show()
