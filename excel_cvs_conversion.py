import pandas as pd


def data_cleaning():
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
    # TODO: Export dataframe to database, we don't need to save a csv to disk
    #df.to_csv(f'{FILENAME}.csv', index=None, header=True)


def get_cleaned_dataframe(df):
    #̶ T̶O̶D̶O̶:̶ C̶h̶a̶n̶g̶e̶ t̶o̶ l̶i̶s̶t̶ c̶o̶m̶p̶r̶e̶h̶e̶n̶s̶i̶o̶n̶
    # List comprehension below doesn't work because list comprehension turns this into a list and not an object as required to mutate an entire dataframe
    # df = [df.iloc[:, row].str.strip() for row in range(len(df.columns)) if df.iloc[:, row].dtype == 'object']

    # Converting float column with strings to turn them into NaN. Otherwise, stripping will get rid of numbers in columns with strings
    df['PREVAILING_WAGE'] = pd.to_numeric(df['PREVAILING_WAGE'], errors='coerce')
    df['WAGE_RATE_OF_PAY_FROM'] = pd.to_numeric(df['PREVAILING_WAGE'], errors='coerce')
    df['WAGE_RATE_OF_PAY_TO'] = pd.to_numeric(df['PREVAILING_WAGE'], errors='coerce')

    # Get rid of all the spaces and standardize casing for strings
    # Create an object out of all the columns with the dtype object
    df_object = df.select_dtypes(['object'])

    # Modify key values
        # Strips away leading and trailing spaces
    df[df_object.columns] = df_object.apply(lambda x: x.str.strip())
        # Title/proper casing for all the values
            # For some reason I had to make a new object in order for it to strip AND titlecase because method chaining didn't work
            # Without a new object, the effect of one method replaces the other
    stripped_df_object = df.select_dtypes(['object'])
    df[stripped_df_object.columns] = stripped_df_object.apply(lambda x: x.str.title())

    return df


if __name__ == '__main__':
    data_cleaning()
