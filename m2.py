#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# Read data from CSV file
data = pd.read_csv(r"C:\Users\Admin\Downloads\CAR DETAILS FROM CAR DEKHO.csv")

# Filter data for Datsun and Toyota cars price from 2017 and 2018
filtered_data = data[
    (data['name'].isin(['Datsun RediGO T Option', 'Toyota Corolla Altis 1.8 VL CVT'])) &
    (data['year'].isin([2017, 2018])) &
    (data['selling_price'].notnull())  # Filter for non-null selling prices
]

# Calculate the overall price mean
overall_mean = filtered_data['selling_price'].mean()

# Create a line graph of selling prices
fig, ax = plt.subplots()
line, = ax.plot(filtered_data['selling_price'])

# Animate the line graph
def animate(i):
    line.set_data(np.arange(0, i), filtered_data['selling_price'][:i])
    return line,

ani = animation.FuncAnimation(fig, animate, interval=100, frames=len(filtered_data))

plt.xlabel('Index')
plt.ylabel('Selling Price')
plt.title('Selling Prices of Datsun RediGO T Option and Toyota Corolla Altis 1.8 VL CVT')
plt.show()


# In[ ]:




