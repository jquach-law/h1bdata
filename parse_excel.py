import pandas as pd
import numpy as np


def main():
    file_name = 'LCA_Disclosure_Data_FY2021_Q3.csv'

    # Read .csv file
    df = pd.read_csv(file_name)

    # Reads named column
    COLS_TO_KEEP = [
        'CASE_NUMBER', 'VISA_CLASS', 'JOB_TITLE', 'SOC_TITLE', 'FULL_TIME_POSITION',
        'EMPLOYER_NAME', 'EMPLOYER_CITY', 'EMPLOYER_STATE', 'WAGE_RATE_OF_PAY_FROM', 
        'WAGE_RATE_OF_PAY_TO', 'WAGE_UNIT_OF_PAY', 'PREVAILING_WAGE', 'PW_UNIT_OF_PAY'
    ]
    # Replace df with only data we need
    df = df[COLS_TO_KEEP]

    # Place columns into new .csv
    df.to_csv('test.csv')


if __name__ == '__main__':
    main()
