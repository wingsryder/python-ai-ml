'''
Using curve fitting and how to establish a relationship between height (the height from which a ball is dropped) and time (the time taken by the ball to reach the ground). This relationship reflected Earth's gravity.
Now, we have provided you with a dataset containing values for height and time. Your task is to analyze this data and determine the planet whose gravity matches the observed data.
Keep in mind that different planets have different gravitational accelerations i.e. gravity. For example:
• Earth: 9.8 m/s2
• Mars: 3.73 m/s2
• Saturn: 10.44 m/s2

You may search online to check the gravitational accelerations of all the planets in our solar system.
Height and Time dataset for this question can be accessed here: https://coding-platform.s3.amazonaws.com/dev/lms/tickets/7a31467b-9891-41fa-a114-6a0773be5ad7/P0kp1LfzWCHNHOBW.csv

Calculate the gravitational acceleration based on the dataset and select the correct planet from the options provided.
Mercury, Venus, Earth, Mars, Jupiter, Saturn, Uranus, Neptune
'''

import pandas as pd
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

# Read the data
df = pd.read_csv('https://coding-platform.s3.amazonaws.com/dev/lms/tickets/7a31467b-9891-41fa-a114-6a0773be5ad7/P0kp1LfzWCHNHOBW.csv')

# Calculate t² for each time value
df['t_squared'] =  df['Time (s)'] ** 2

# Create the linear regression
# We'll use h = (1/2)gt², so slope = g/2
slope, intercept, r_value, p_value, std_err = stats.linregress(df['t_squared'], df['Height (m)'])

# Calculate g (gravity) - multiply slope by 2 since g = 2*slope
calculated_g = abs(2 * slope)  # Taking absolute value since height might be negative

# Create a scatter plot of the data with the fitted line
plt.figure(figsize=(10, 6))
plt.scatter(df['t_squared'], df['Height (m)'], label='Data points')
plt.plot(df['t_squared'], slope * df['t_squared'] + intercept, 'r', label=f'Fitted line (g = {calculated_g:.2f} m/s²)')
plt.xlabel('Time² (s²)')
plt.ylabel('Height (m)')
plt.title('Height vs Time² for Falling Object')
plt.legend()
plt.grid(True)


# Define planet gravities
planet_gravities = {
    'Mercury': 3.7,
    'Venus': 8.87,
    'Earth': 9.8,
    'Mars': 3.73,
    'Jupiter': 24.79,
    'Saturn': 10.44,
    'Uranus': 8.69,
    'Neptune': 11.15
}

# Find closest planet
closest_planet = min(planet_gravities.items(), key=lambda x: abs(x[1] - calculated_g))


# Message Output
print("Standard Error: ", std_err)
print("Slope: ", slope)

# Print results
print(f"\nCalculated gravitational acceleration: {calculated_g:.2f} m/s²")

print(f"\nPlanet Difference with Calculated Gravity (lesser will be closer)")

# Printing each planet difference
for planet, g in planet_gravities.items():
    print(f"{planet} : {round(abs(g - calculated_g),2)} m/s²")


print(f"\nClosest matching planet: {closest_planet[0]}")
print(f"Planet's gravity: {closest_planet[1]} m/s²")
print(f"Difference: {abs(closest_planet[1] - calculated_g):.2f} m/s²")
