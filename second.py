import pandas as pd

# Load the dataset
file_path = 'train.csv'  
titanic_df = pd.read_csv(file_path)

# Display the first few rows of the dataset
print(titanic_df.head())

# Calculate summary statistics
mean_values = titanic_df.mean(numeric_only=True)
median_values = titanic_df.median(numeric_only=True)
mode_values = titanic_df.mode(numeric_only=True).iloc[0]  # mode() returns a DataFrame
std_values = titanic_df.std(numeric_only=True)

# Print the summary statistics
print("Mean:\n", mean_values)
print("\nMedian:\n", median_values)
print("\nMode:\n", mode_values)
print("\nStandard Deviation:\n", std_values)

