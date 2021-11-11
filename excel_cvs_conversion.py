import pandas as pd
import csv


def main():
    COLS_TO_USE = [
        'CASE_NUMBER',
        'VISA_CLASS',
        'JOB_TITLE',
        'SOC_TITLE',
        'FULL_TIME_POSITION',
        'EMPLOYER_NAME',
        'EMPLOYER_CITY',
        'EMPLOYER_STATE',
        'WAGE_RATE_OF_PAY_FROM',
        'WAGE_RATE_OF_PAY_TO',
        'WAGE_UNIT_OF_PAY',
        'PREVAILING_WAGE',
        'PW_UNIT_OF_PAY',
    ]
    FILENAME = 'LCA_Disclosure_Data_FY2021_Q3'

    # Convert excel to csv
    try:
        # Try reading excel file with types enforced for each column
        df = pd.read_excel(
            f'data/{FILENAME}.xlsx',
            usecols=COLS_TO_USE,
            dtype={
                'CASE_NUMBER': str,
                'VISA_CLASS': str,
                'JOB_TITLE': str,
                'SOC_TITLE': str,
                'FULL_TIME_POSITION': str,
                'EMPLOYER_NAME': str,
                'EMPLOYER_CITY': str,
                'EMPLOYER_STATE': str,
                'WAGE_RATE_OF_PAY_FROM': float,
                'WAGE_RATE_OF_PAY_TO': float,
                'WAGE_UNIT_OF_PAY': str,
                'PREVAILING_WAGE': float,
                'PW_UNIT_OF_PAY': str,
            }
        )
        df = get_cleaned_dataframe(df)
    except ValueError:
        # If an error occurs because of a cell not matching the column type,
        # (such as when a cell containing a string is in a column of floats)
        # then read normally and do data cleaning to remove bad rows
        df = pd.read_excel(
            f'data/{FILENAME}.xlsx',
            usecols=COLS_TO_USE,
        )
        df = get_cleaned_dataframe(df)
        # TODO: Convert types after cleaning.
        #df['CASE_NUMBER'] = df['CASE_NUMBER'].astype(str)
        # ...
    # TODO: Export dataframe to database, we don't need to save a csv to disk
    #df.to_csv(f'{FILENAME}.csv', index=None, header=True)


def get_cleaned_dataframe(df):
    return df.loc[
        (df['CASE_NUMBER'].notnull()) &
        (df['VISA_CLASS'].notnull()) &
        (df['JOB_TITLE'].notnull()) &
        (df['SOC_TITLE'].notnull()) &
        (df['FULL_TIME_POSITION'].notnull()) &
        (df['EMPLOYER_NAME'].notnull()) &
        (df['EMPLOYER_CITY'].notnull()) &
        (df['EMPLOYER_STATE'].notnull()) &
        (df['WAGE_RATE_OF_PAY_FROM'].notnull()) &
        (df['WAGE_RATE_OF_PAY_TO'].notnull()) &
        (df['WAGE_UNIT_OF_PAY'].notnull()) &
        (df['PREVAILING_WAGE'].notnull())
        # TODO: Add regex to make sure float columns don't contain strings
    ]


if __name__ == '__main__':
    main()
