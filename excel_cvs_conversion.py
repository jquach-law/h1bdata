# import get_excel_file as query
from dotenv import load_dotenv
import pandas as pd
import sqlalchemy
# import csv
import os


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
CSV_FILENAME = 'test'


def csv_to_df(csv_filename):

    # Convert excel to csv
    try:
        # Try reading excel file with types enforced for each column
        df = pd.read_excel(
            f'data/{csv_filename}.xlsx',
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
            f'data/{csv_filename}.xlsx',
            usecols=COLS_TO_USE,
        )
        df = get_cleaned_dataframe(df)

        # TODO: Convert types after cleaning.
        #df['CASE_NUMBER'] = df['CASE_NUMBER'].astype(str)
        # ...
    return df

def get_cleaned_dataframe(df):
    #̶ T̶O̶D̶O̶:̶ C̶h̶a̶n̶g̶e̶ t̶o̶ l̶i̶s̶t̶ c̶o̶m̶p̶r̶e̶h̶e̶n̶s̶i̶o̶n̶
    # List comprehension below doesn't work because list comprehension turns this into a list and not an object as required to mutate an entire dataframe
    # df = [df.iloc[:, row].str.strip() for row in range(len(df.columns)) if df.iloc[:, row].dtype == 'object']

    # Converting float column with strings to turn them into NaN. Otherwise, stripping will get rid of numbers in columns with strings
    df['PREVAILING_WAGE'] = pd.to_numeric(df['PREVAILING_WAGE'], errors='coerce')
    df['WAGE_RATE_OF_PAY_FROM'] = pd.to_numeric(df['WAGE_RATE_OF_PAY_FROM'], errors='coerce')
    df['WAGE_RATE_OF_PAY_TO'] = pd.to_numeric(df['WAGE_RATE_OF_PAY_TO'], errors='coerce')

    # Get rid of all the spaces and standardize casing for strings
    # Create an object out of all the columns with the dtype object
    df_object = df.select_dtypes(['object'])

    # Modify key values
        # Strips away leading and trailing spaces
    df[df_object.columns] = df_object.apply(lambda x: x.str.strip()).apply(lambda x: x.str.title())

    return df


if __name__ == '__main__':

    # Get environment variables set in the .env file
    load_dotenv()

    # Create a dataframe from the csv file
    df = csv_to_df(CSV_FILENAME)

    # Export the dataframe to the database
    connection_string = os.path.expandvars(
      os.environ['CRDB_CONN_STR']
    ).replace(
        'postgres://', 'cockroachdb://'
    ).replace(
        'postgresql://', 'cockroachdb://'
    )
    engine = sqlalchemy.create_engine(connection_string)
    df.to_sql('sometablenamehere', engine, if_exists='replace', index=False)
    
    # TODO: remove prints below later
    # Print tables in the database
    metadata = sqlalchemy.MetaData()
    metadata.reflect(bind=engine)
    print(metadata.tables)
    
    # Print all rows in table
    with engine.connect() as conn:
        result = conn.execute(
            sqlalchemy.select([metadata.tables['sometablenamehere']])
        )
        for row in result:
            print(row)
    
    # Print df from db table
    print(pd.read_sql('sometablenamehere', engine))
