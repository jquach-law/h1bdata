import get_excel_file as query
import pandas as pd
import csv

# excel_file_name = 'LCA_Disclosure_Data_FY' + year + '_' + quarter + '.xlsx'
# csv_file_name = 'LCA_Disclosure_Data_FY' + year + '_' + quarter + '.csv'

excel_file_name = query.file_name[5:]
csv_file_name = query.file_name[5:-4] + 'csv'

# # Convert excel to csv
# read_file = pd.read_excel (excel_file_name)
# read_file.to_csv (csv_file_name, index = None, header=True)

print(excel_file_name)
print(csv_file_name)