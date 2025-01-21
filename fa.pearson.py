import pandas as pd
from scipy.stats import pearsonr

# Load the uploaded CSV file
file_path = 'bmi.fa.adc.cg.na.Jan21.fa.all.unnormalized.csv'
data = pd.read_csv(file_path)

# Display the first few rows of the dataset to understand its structure
data.head(), data.columns

# Select numeric columns only, excluding 'HASTA ADI' and 'Sex'
numeric_data = data.select_dtypes(include=['float64', 'int64']).copy()

# Initialize results dictionary to store correlations and p-values
correlation_results = {}

# Calculate Pearson correlation and p-values for each column with BMIT2T0
for column in numeric_data.columns:
    if column != 'BMIT2T0':  # Skip correlation of BMI with itself
        corr, p_value = pearsonr(data['BMIT2T0'], numeric_data[column])
        correlation_results[column] = {'Pearson Coefficient': corr, 'P-value': p_value}

# Convert results to a DataFrame for better visualization
correlation_df = pd.DataFrame.from_dict(correlation_results, orient='index')
correlation_df = correlation_df.sort_values(by='P-value')  # Sort by p-value

# Write the correlation results to a text file
output_file = 'correlation_results.txt'
correlation_df.to_csv(output_file)
