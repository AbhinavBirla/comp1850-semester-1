# Week 1.6, Session 1: Task 5

# Write a program here that uses the QuakeFeed and QuakeDataset
# classes to download earthquake data from a USGS data feed,
# analyze it and display the results

# See README.md for full details of what is required and what
# program output should look like
from feed import QuakeFeed
from dataset import QuakeDataset

level = input("Enter significance level: ")
period = input("Enter time period: ")

feed = QuakeFeed(level, period)

dataset = QuakeDataset(feed)

dataset.read_feed()

print(dataset)

print(f"Mean depth = {dataset.mean_depth():.2f} km")
print(f"Mean magnitude = {dataset.mean_magnitude():.1f}")

quake = dataset.strongest_quake()

print("\nStrongest quake:")
print(f"Time = {quake.when}")
print(f"Longitude = {quake.longitude}")
print(f"Latitude = {quake.latitude}")
print(f"Depth = {quake.depth} km")
print(f"Magnitude = {quake.magnitude}")