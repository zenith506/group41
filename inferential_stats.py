from scipy import stats
import pandas as pd

# Load the datasets
dataset1 = pd.read_csv('C:/Users/A Plus/Downloads/dataset1.csv')
dataset2 = pd.read_csv('C:/Users/A Plus/Downloads/dataset2.csv')

# Merge dataset1 (demographics) and dataset2 (screen time) on ID
merged_data = pd.merge(dataset1, dataset2, on='ID')

# Calculate the total screen time (weekdays + weekends) for each activity
merged_data['Total_C'] = merged_data['C_we'] + merged_data['C_wk']
merged_data['Total_G'] = merged_data['G_we'] + merged_data['G_wk']
merged_data['Total_S'] = merged_data['S_we'] + merged_data['S_wk']
merged_data['Total_T'] = merged_data['T_we'] + merged_data['T_wk']

# Separate data by gender (0 = Female, 1 = Male)
male_data = merged_data[merged_data['gender'] == 1]
female_data = merged_data[merged_data['gender'] == 0]

# Perform T-tests for each screen time category
t_test_C = stats.ttest_ind(male_data['Total_C'], female_data['Total_C'], equal_var=False)
t_test_G = stats.ttest_ind(male_data['Total_G'], female_data['Total_G'], equal_var=False)
t_test_S = stats.ttest_ind(male_data['Total_S'], female_data['Total_S'], equal_var=False)
t_test_T = stats.ttest_ind(male_data['Total_T'], female_data['Total_T'], equal_var=False)

# Display the results
print("T-test Results for Gender (Male vs. Female):")
print(f"Computers: {t_test_C}")
print(f"Games: {t_test_G}")
print(f"Smartphones: {t_test_S}")
print(f"TV: {t_test_T}")
