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
import matplotlib.pyplot as plt

# Read the data
df = pd.read_csv('https://coding-platform.s3.amazonaws.com/dev/lms/tickets/7a31467b-9891-41fa-a114-6a0773be5ad7/P0kp1LfzWCHNHOBW.csv')

# For a falling object under gravity:
# h = h₀ - (1/2)gt²
# This is a quadratic equation: h = a + bt + ct²
# where c = -g/2

# Fit a quadratic polynomial
coefficients = np.polyfit(df['Time (s)'], df['Height (m)'], 2)

# Extract coefficients
a = round(coefficients[2], 3)  # constant term
b = round(coefficients[1], 3)  # linear term
c = round(coefficients[0], 3)  # quadratic term

# Calculate gravitational acceleration (g = -2c)
calculated_g = round(abs(2 * c), 3)

# Create points for the fitted curve
time_range = np.linspace(min(df['Time (s)']), max(df['Time (s)']), 100)
height_fit = coefficients[0]*time_range**2 + coefficients[1]*time_range + coefficients[2]

# Plot the data and the fitted curve
plt.figure(figsize=(10, 6))
plt.scatter(df['Time (s)'], df['Height (m)'], label='Data points', color='blue')
plt.plot(time_range, height_fit, 'r-', label='Fitted curve', linewidth=2)
plt.xlabel('Time (s)')
plt.ylabel('Height (m)')
plt.title('Height vs Time with Quadratic Fit')
plt.legend()
plt.grid(True)

print("Polynomial coefficients:")
print(f"h(t) = {c}t² + {b}t + {a}")
print(f"\nCalculated gravitational acceleration: {calculated_g} m/s²")

# Define planet gravities
planet_gravities = {
    'Mercury': 3.700,
    'Venus': 8.870,
    'Earth': 9.800,
    'Mars': 3.730,
    'Jupiter': 24.790,
    'Saturn': 10.440,
    'Uranus': 8.690,
    'Neptune': 11.150
}

# Calculate and display differences
print("\nDifference from each planet's gravity:")
for planet, gravity in sorted(planet_gravities.items()):
    difference = round(abs(gravity - calculated_g), 3)
    print(f"{planet}: {difference} m/s²")

# Find closest planet
closest_planet = min(planet_gravities.items(), 
                    key=lambda x: abs(x[1] - calculated_g))

print(f"\nClosest matching planet: {closest_planet[0]}")
print(f"Planet's gravity: {closest_planet[1]} m/s²")
print(f"Calculated gravity: {calculated_g} m/s²")
print(f"Absolute difference: {round(abs(closest_planet[1] - calculated_g), 3)} m/s²")
