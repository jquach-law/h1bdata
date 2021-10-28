import pandas as pd
import csv

# Convert excel to csv
read_file = pd.read_excel (r'LCA_Disclosure_Data_FY2021_Q3.xlsx')
read_file.to_csv (r'LCA_Disclosure_Data_FY2021_Q3.csv', index = None, header=True)