import pandas as pd

# Loading the datasets
dataset1 = pd.read_csv('C:/Users/A Plus/Downloads/dataset1.csv')
dataset2 = pd.read_csv('C:/Users/A Plus/Downloads/dataset2.csv')

# Merge dataset1 (demographics) and dataset2 (screen time) on ID
merged_data = pd.merge(dataset1, dataset2, on='ID')

# Calculate the total screen time (weekdays + weekends) for each activity
merged_data['Total_C'] = merged_data['C_we'] + merged_data['C_wk']
merged_data['Total_G'] = merged_data['G_we'] + merged_data['G_wk']
merged_data['Total_S'] = merged_data['S_we'] + merged_data['S_wk']
merged_data['Total_T'] = merged_data['T_we'] + merged_data['T_wk']

# Descriptive Analysis: Average screen time by Gender
gender_stats = merged_data.groupby('gender')[['Total_C', 'Total_G', 'Total_S', 'Total_T']].mean()
print("Average Screen Time by Gender (0 = Female, 1 = Male):")
print(gender_stats)
