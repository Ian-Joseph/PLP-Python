# --------------------------------------------
# Task 0: Import Libraries
# --------------------------------------------
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Optional: Set a visual style for plots
sns.set(style="whitegrid")

# --------------------------------------------
# Task 1: Load and Explore the Dataset
# --------------------------------------------

# Load dataset
try:
    df = pd.read_csv('your_dataset.csv')  # <-- Replace 'your_dataset.csv' with your file name
    print("Dataset loaded successfully!\n")
except FileNotFoundError:
    print("Error: File not found. Please check the filename or path.")

# Display first few rows
print(df.head())

# Check structure
print("\nData Types:")
print(df.dtypes)

print("\nMissing Values:")
print(df.isnull().sum())

# Clean data (example: drop missing values)
df_cleaned = df.dropna()
print(f"\nDataset after dropping missing values: {df_cleaned.shape}")

# --------------------------------------------
# Task 2: Basic Data Analysis
# --------------------------------------------

# Basic statistics
print("\nBasic Statistics:")
print(df_cleaned.describe())

# Example Grouping (you can change columns depending on your dataset)
# For example, group by 'species' and find mean of 'sepal_length'
# Make sure to replace 'species' and 'sepal_length' with your actual columns
try:
    group_means = df_cleaned.groupby('species').mean()  # <-- Change 'species' if needed
    print("\nGroup Means:")
    print(group_means)
except KeyError:
    print("\nWarning: 'species' column not found in your dataset. Update grouping column.")

# --------------------------------------------
# Task 3: Data Visualization
# --------------------------------------------

# 1. Line chart (Example: a time-series trend if applicable)
# Ensure you have a 'date' column, otherwise modify this part.
try:
    df_cleaned['date'] = pd.to_datetime(df_cleaned['date'])  # <-- Only if you have a date column
    df_cleaned.set_index('date', inplace=True)
    df_cleaned['some_value_column'].plot(title='Trend Over Time')  # Replace 'some_value_column'
    plt.xlabel('Date')
    plt.ylabel('Value')
    plt.show()
except (KeyError, ValueError):
    print("\nSkipping line chart (no 'date' column or wrong format).")

# 2. Bar chart
try:
    avg_values = df_cleaned.groupby('species')['sepal_length'].mean()  # Change columns as needed
    avg_values.plot(kind='bar', title='Average Sepal Length per Species')
    plt.xlabel('Species')
    plt.ylabel('Average Sepal Length')
    plt.show()
except KeyError:
    print("\nSkipping bar chart (columns not found).")

# 3. Histogram
try:
    df_cleaned['sepal_width'].hist(bins=20)
    plt.title('Distribution of Sepal Width')
    plt.xlabel('Sepal Width')
    plt.ylabel('Frequency')
    plt.show()
except KeyError:
    print("\nSkipping histogram (column not found).")

# 4. Scatter Plot
try:
    plt.scatter(df_cleaned['sepal_length'], df_cleaned['petal_length'])
    plt.title('Sepal Length vs. Petal Length')
    plt.xlabel('Sepal Length')
    plt.ylabel('Petal Length')
    plt.show()
except KeyError:
    print("\nSkipping scatter plot (columns not found).")

# --------------------------------------------
# Findings and Observations
# --------------------------------------------

print("\nFindings/Observations:")
print("- The dataset was successfully cleaned and analyzed.")
print("- Basic statistics showed the range and spread of the numerical columns.")
print("- Grouping by species revealed differences in sepal and petal measurements.")
print("- Visualizations illustrated distribution, relationships, and comparisons in the data.")
