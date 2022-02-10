from get_excel_file import Data
from dotenv import load_dotenv
import pandas as pd
import sqlalchemy

# import csv
import os

COLS_TO_USE = [
    "CASE_NUMBER",
    "VISA_CLASS",
    "JOB_TITLE",
    "SOC_TITLE",
    "FULL_TIME_POSITION",
    "EMPLOYER_NAME",
    "EMPLOYER_CITY",
    "EMPLOYER_STATE",
    "WAGE_RATE_OF_PAY_FROM",
    "WAGE_RATE_OF_PAY_TO",
    "WAGE_UNIT_OF_PAY",
    "PREVAILING_WAGE",
    "PW_UNIT_OF_PAY",
]

tmp = Data()
year, quarter = tmp._check_calendar()
CSV_FILE_PATH = f"data/LCA_Disclosure_Data_FY{year}_{quarter}.xlsx"


def csv_to_df(csv_filename):
    # Convert excel to csv
    df = pd.read_excel(csv_filename, usecols=COLS_TO_USE)
    df = coerce_to_numeric_type(df)
    df = strip_and_standardize_casing(df)
    df["WAGE_RATE_OF_PAY_FROM"] = df["WAGE_RATE_OF_PAY_FROM"].astype(float)
    df["WAGE_RATE_OF_PAY_TO"] = df["WAGE_RATE_OF_PAY_TO"].astype(float)
    df["PREVAILING_WAGE"] = df["PREVAILING_WAGE"].astype(float)

    return df


def coerce_to_numeric_type(df):
    # ̶ T̶O̶D̶O̶:̶ C̶h̶a̶n̶g̶e̶ t̶o̶ l̶i̶s̶t̶ c̶o̶m̶p̶r̶e̶h̶e̶n̶s̶i̶o̶n̶
    # List comprehension below doesn't work because list comprehension turns this into a list and not an object as required to mutate an entire dataframe
    # df = [df.iloc[:, row].str.strip() for row in range(len(df.columns)) if df.iloc[:, row].dtype == 'object']

    # Converting float column with strings to turn them into NaN. Otherwise, stripping will get rid of numbers in columns with strings
    df["PREVAILING_WAGE"] = pd.to_numeric(df["PREVAILING_WAGE"], errors="coerce")
    df["WAGE_RATE_OF_PAY_FROM"] = pd.to_numeric(
        df["WAGE_RATE_OF_PAY_FROM"], errors="coerce"
    )
    df["WAGE_RATE_OF_PAY_TO"] = pd.to_numeric(
        df["WAGE_RATE_OF_PAY_TO"], errors="coerce"
    )

    return df


def strip_and_standardize_casing(df):
    # Get rid of all the spaces and standardize casing for strings
    # Create an object out of all the columns with the dtype object
    df_object = df.select_dtypes(["object"])

    # Modify key values
    # Strips away leading and trailing spaces
    df[df_object.columns] = df_object.apply(lambda x: x.str.strip()).apply(
        lambda x: x.str.title()
    )

    return df


def connect_to_database():
    """
    Connect to cockroach database
    Args: N/A
    Return: Engine object, provides access to a Connection, which can then invoke SQL statements
    """
    # Export the dataframe to the database
    connection_string = (
        os.path.expandvars(os.environ["CRDB_CONN_STR"])
        .replace("postgres://", "cockroachdb://")
        .replace("postgresql://", "cockroachdb://")
    )
    engine = sqlalchemy.create_engine(connection_string)
    return engine


def export_dataframe_to_database(df, engine, table_name):
    """
    Export dataframe to database
    Args:
        df: pandas dataframe
        engine: sqlalchemy engine
        table_name: name of table to be created in database
    Return: N/A
    """
    print("Exporting dataframe to database...")
    df.to_sql(table_name, engine, if_exists="replace", index=False)
    print("Dataframe exported to database successfully!")


if __name__ == "__main__":
    # Get environment variables set in the .env file
    load_dotenv()

    # Create a dataframe from the csv file
    df = csv_to_df(CSV_FILE_PATH)

    # Connect to database
    engine = connect_to_database()

    # Export the dataframe to the database
    export_dataframe_to_database(df, engine, "h1bdata_table")
