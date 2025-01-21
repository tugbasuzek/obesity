import pandas as pd

# Load the CSV file
file_path = 'bmi.adc.değerleri.csv'
data = pd.read_csv(file_path)
#target="FA_avg_T2T0"
#target="ADC_avg_T2T0"
#target="ADC_avg_T2T0"
target="EatT2T0"
# Group by a categorical column and compute mean and std deviation for subgroups
subgroup_stats = data.groupby('Sex')[target].agg(['mean', 'std']).reset_index()
subgroup_stats.rename(columns={'mean': 'Subgroup Mean', 'std': 'Subgroup Std Dev'}, inplace=True)

# Calculate the total mean and std for the entire dataset
total_mean = data[target].mean()
total_std = data[target].std()

# Add the total statistics to the results DataFrame
subgroup_stats.loc[len(subgroup_stats.index)] = ['Overall', total_mean, total_std]

# Display or save results
print(subgroup_stats)
subgroup_stats.to_csv('subgroup_and_total_stats.csv', index=False)

