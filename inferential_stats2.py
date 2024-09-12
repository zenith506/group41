import pandas as pd

# Load datasets
dataset2 = pd.read_csv('C:/Users/A Plus/Downloads/dataset2.csv')  # Screen time data
dataset3 = pd.read_csv('C:/Users/A Plus/Downloads/dataset3.csv')  # Well-being data

# Merge dataset2 (screen time) and dataset3 (well-being indicators) on ID
merged_data = pd.merge(dataset2, dataset3, on='ID')

# Calculate total screen time for each respondent
merged_data['Total_Screen_Time'] = (merged_data['C_we'] + merged_data['C_wk'] +
                                    merged_data['G_we'] + merged_data['G_wk'] +
                                    merged_data['S_we'] + merged_data['S_wk'] +
                                    merged_data['T_we'] + merged_data['T_wk'])

# Select well-being indicators
wellbeing_columns = ['Optm', 'Usef', 'Relx', 'Intp', 'Engs', 'Dealpr', 'Thcklr', 'Goodme', 'Clsep', 
                     'Conf', 'Mkmind', 'Loved', 'Intthg', 'Cheer']

# Calculate Pearson correlation between total screen time and each well-being indicator
correlation_results = merged_data[['Total_Screen_Time'] + wellbeing_columns].corr()

# Extract correlation between total screen time and well-being indicators
screen_time_corr = correlation_results['Total_Screen_Time'][1:]  # Skip the first row (self-correlation)

# Display the results
print("Correlation between Total Screen Time and Well-Being Indicators:")
print(screen_time_corr)
