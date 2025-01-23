import pandas as pd
from scipy.stats import spearmanr

# Load the CSV file
file_path = 'bmi.depression.csv'  # Replace with your file path
data = pd.read_csv(file_path)

# Ensure the data types are numeric for Spearman's calculation
# Drop rows with missing or non-numeric values in `bmi` and `depression`
data = data[['bmi', 'depression']].apply(pd.to_numeric, errors='coerce').dropna()

# Compute Spearman's Rank Correlation Coefficient
spearman_corr, p_value = spearmanr(data['bmi'], data['depression'])

# Display results
print(f"Spearman's Rank Correlation Coefficient: {spearman_corr:.4f}")
print(f"P-value: {p_value:.4f}")

# Interpret results
if p_value < 0.05:
    print("There is a statistically significant correlation between BMI and Depression (p < 0.05).")
else:
    print("There is no statistically significant correlation between BMI and Depression (p ≥ 0.05).")
