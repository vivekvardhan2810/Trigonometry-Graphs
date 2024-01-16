# -*- coding: utf-8 -*-
"""Trigonometry.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/15mhjq85IJJHZhHnjaRWeYEimT49mQjGA
"""

import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0,4*np.pi,0.1)
y = np.sin(x)

plt.plot(x,y)
plt.show()

x = np.arange(0,4*np.pi,0.1)
y = np.sin(x)
z = np.cos(x)

plt.plot(x,y,z)
plt.show()

x = np.arange(0,4*np.pi,0.1)
y = np.sin(x)
z = np.cos(x)

plt.plot(x,y,x,z)
plt.legend(['sin(x)',['cos(x)']])
plt.show()

import matplotlib.pyplot as plt
import numpy as np

# Define the x values
x = np.arange(0, 4*np.pi, 0.1)

# Calculate y values for sine and cosine functions
sin_y = np.sin(x)
cos_y = np.cos(x)

# Plot the sine and cosine functions
plt.plot(x, sin_y, label='sin(x)')
plt.plot(x, cos_y, label='cos(x)')
plt.legend()
plt.title('Graphs of sin(x) and cos(x)')
plt.xlabel('x')
plt.ylabel('y')
plt.show()

# Calculate y values for tan, cot, cosec, and sec functions
tan_y = np.tan(x)
cot_y = 1 / np.tan(x)
cosec_y = 1 / np.sin(x)
sec_y = 1 / np.cos(x)

# Plot the tan, cot, cosec, and sec functions
plt.plot(x, tan_y, label='tan(x)')
plt.plot(x, cot_y, label='cot(x)')
plt.plot(x, cosec_y, label='cosec(x)')
plt.plot(x, sec_y, label='sec(x)')

# Adding grid and labels
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid(True, linestyle='--', alpha=0.7)

# Displaying legend
plt.legend()

# Show the plot
plt.title('Graphs of tan, cot, cosec, and sec Functions')
plt.xlabel('x')
plt.ylabel('y')
plt.show()

import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Generate some sample data
np.random.seed(42)
angles = np.sort(2 * np.pi * np.random.rand(100))
sine_values = np.sin(angles) + 0.1 * np.random.randn(100)

# Reshape the data for sklearn
angles = angles.reshape(-1, 1)

# Create a linear regression model
model = LinearRegression()

# Fit the model to the data
model.fit(angles, sine_values)

# Generate predictions for the input data
predicted_sine = model.predict(angles)

# Plot the original data and the regression line
plt.scatter(angles, sine_values, label='Actual Data')
plt.plot(angles, predicted_sine, color='red', label='Linear Regression')
plt.title('Linear Regression for Sine Values')
plt.xlabel('Angle (radians)')
plt.ylabel('Sine Value')
plt.legend()
plt.show()