"""Prompt 3: A block of code for Jupiter notebook that will if given a column of data display a plot a graph. 
Written by Vincent Hall of Build Intellect Ltd. and ABT NEWS Ltd. 12 Feb 2024."""

import pandas as pd 

import matplotlib.pyplot as plt 

 

# Sample data (replace with your data) 

data = pd.Series([1, 2, 3, 4, 5]) 

 

# Assuming the data is in a column named "values" 

fig, ax = plt.subplots() 

ax.plot(data) 

ax.set_xlabel("Index") 

ax.set_ylabel("Value") 

ax.set_title("Line Plot of Data") 

plt.show() 
