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
    FILENAME = 'test'

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
        print('in try')
    except ValueError:
        print('there was an error')
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
    # Get rid of all the spaces
    # TODO: Change to list comprehension
    for i in range(len(df.columns)):
        print(df.iloc[:, i])
        if df.iloc[:, i].dtype == 'float64':
            continue
        df.iloc[:, i] = df.iloc[:, i].str.strip()

    # Type casting
    df['CASE_NUMBER'] = df['CASE_NUMBER'].astype(str)
    df['VISA_CLASS'] = df['VISA_CLASS'].astype(str)
    df['JOB_TITLE'] = df['JOB_TITLE'].astype(str)
    df['SOC_TITLE'] = df['SOC_TITLE'].astype(str)
    df['FULL_TIME_POSITION'] = df['FULL_TIME_POSITION'].astype(str)
    df['EMPLOYER_NAME'] = df['EMPLOYER_NAME'].astype(str)
    df['EMPLOYER_CITY'] = df['EMPLOYER_CITY'].astype(str)
    df['EMPLOYER_STATE'] = df['EMPLOYER_STATE'].astype(str)
    df['WAGE_RATE_OF_PAY_FROM'] = df['WAGE_RATE_OF_PAY_FROM'].astype(float)
    df['WAGE_RATE_OF_PAY_TO'] = df['WAGE_RATE_OF_PAY_TO'].astype(float)
    df['WAGE_UNIT_OF_PAY'] = df['WAGE_UNIT_OF_PAY'].astype(str)
    df['PREVAILING_WAGE'] = df['PREVAILING_WAGE'].astype(float)
    df['PW_UNIT_OF_PAY'] = df['PW_UNIT_OF_PAY'].astype(str)

    # TODO: Get rid of rows if columns don't match a pattern
    # ^[^0-9].*
    df = df.loc[
        (df['VISA_CLASS'].str.contains(r'^[^0-9].*', regex=True, na=False))
    ]
    print(df)

    # TODO: Add regex to make sure float columns don't contain strings
    # TODO: Standardize casing for strings

    return df


if __name__ == '__main__':
    main()
