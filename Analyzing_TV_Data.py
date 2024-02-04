#Codes to analyze TV Data
# Import pandas
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns


# Load the CSV data into DataFrames
super_bowls = pd.read_csv('datasets/super_bowls.csv')
tv = pd.read_csv('datasets/tv.csv')
halftime_musicians = pd.read_csv('datasets/halftime_musicians.csv')

# Display the first five rows of each DataFrame
print(super_bowls.head())
print(tv.head())
print(halftime_musicians.head())

# Summary of the TV data to inspect
tv.info()

print('\n')

# Summary of the halftime musician data to inspect
halftime_musicians.info()

# set plotting style
plt.style.use('seaborn')

# Plot a histogram of combined points
plt.hist(super_bowls.combined_pts)
plt.xlabel('Combined Points')
plt.ylabel('Number of Super Bowls')
plt.show()

# Display the Super Bowls with the highest and lowest combined scores
print(super_bowls[super_bowls['combined_pts'] > 70])
print(super_bowls[super_bowls['combined_pts'] < 25])

# Plot a histogram of point differences
plt.hist(super_bowls.difference_pts)
plt.xlabel('Point Difference')
plt.ylabel('Number of Super Bowls')
plt.show()

# Display the closest game(s) and biggest blowouts
print(super_bowls[super_bowls['difference_pts'] == 1])
print(super_bowls[super_bowls['difference_pts'] > 35])

# Join game and TV data, filtering out SB I because it was split over two networks
games_tv = pd.merge(tv[tv['super_bowl'] > 1], super_bowls, on='super_bowl')
