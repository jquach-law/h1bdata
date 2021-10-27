import pandas as pd

file_name = 'LCA_Disclosure_Data_FY2021_Q3.csv'
df = pd.read_csv(file_name)

# Read full columns
print(df[['CASE_NUMBER', 'VISA_CLASS', 'JOB_TITLE', 'SOC_TITLE', 'FULL_TIME_POSITION',
        'EMPLOYER_NAME', 'EMPLOYER_CITY', 'EMPLOYER_STATE', 'WAGE_RATE_OF_PAY_FROM', 
        'WAGE_RATE_OF_PAY_TO', 'WAGE_UNIT_OF_PAY', 'PREVAILING_WAGE', 'PW_UNIT_OF_PAY']])


# Read Each Row
# print(df.head(1))

# Read Column Headers
# print(df.columns)

# # Read Whole Column
# print(df[['CASE_NUMBER']])
