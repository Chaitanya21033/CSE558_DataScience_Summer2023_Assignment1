import pandas as pd
import numpy as np

# Load the dataset with the correct separator and inspect the first few rows
file_path = 'auto-mpg.data'
columns = ['MPG', 'Cylinders', 'Displacement', 'Horsepower', 'Weight', 'Acceleration', 'Model Year', 'Origin']
data = pd.read_csv(file_path, sep='\s+', names=columns, na_values='?')

# Display the first few rows to inspect the data
print(data.head())

# Check for non-numeric data in 'Horsepower'
print("Non-numeric 'Horsepower' values:", data[data['Horsepower'].apply(lambda x: isinstance(x, str))])

# Replace '?' with NaN and convert 'Horsepower' to float
data['Horsepower'] = pd.to_numeric(data['Horsepower'], errors='coerce')

# Fill NaN values with the median of 'Horsepower'
# Fill NaN values without using inplace=True
data['Horsepower'] = data['Horsepower'].fillna(data['Horsepower'].median())


# Verify conversion and imputation
print("After cleaning:")
print(data['Horsepower'].describe())

# Correctly handling non-numeric values in 'Horsepower'
# Replace '?' with NaN, then convert the column to float
data['Horsepower'] = data['Horsepower'].replace('?', np.nan).astype(float)

# Fill NaN values with the median of 'Horsepower'
data['Horsepower'] = data['Horsepower'].fillna(data['Horsepower'].median())

# Proceed with one-hot encoding and normalization as before

# One-hot encoding for discrete attributes
data = pd.get_dummies(data, columns=['Cylinders', 'Origin'])

# Compute mean and variance before normalization
mean_vector = data.mean()
variance_vector = data.var()

# Normalize data (Feature Scaling)
data_normalized = (data - mean_vector) / np.sqrt(variance_vector)

# Saving the processed data
data_normalized.to_csv('processed_auto_mpg.csv', index=False)

# Compute mean and variance after normalization
mean_normalized = data_normalized.mean()
variance_normalized = data_normalized.var()

# Computing the overall variance of the dataset
overall_variance_before = variance_vector.sum()
overall_variance_after = variance_normalized.sum()

print("\nOverall Variance before normalization:", overall_variance_before)
print("Overall Variance after normalization:", overall_variance_after)
