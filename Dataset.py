from sklearn.datasets import fetch_california_housing
import os

# Fetch the dataset
print("Fetching California Housing data...")
housing = fetch_california_housing(as_frame=True)

# Save to CSV
file_name = 'california_housing.csv'
housing.frame.to_csv(file_name, index=False)