from excel_cvs_conversion import csv_to_df
import csv
import numpy as np
import pandas as pd
import pytest


@pytest.fixture
def dummy_df():
    return csv_to_df("tests/dummy_data/test_excel_cvs_conversion.xlsx")


class TestCsvToDf:
    def test_returns_df(self, dummy_df):
        assert isinstance(dummy_df, pd.DataFrame) is True

    def test_cols_are_expected_dtypes(self, dummy_df):
        assert dummy_df["WAGE_RATE_OF_PAY_FROM"].dtype == np.float64
        assert dummy_df["WAGE_RATE_OF_PAY_TO"].dtype == np.float64
        assert dummy_df["PREVAILING_WAGE"].dtype == np.float64

    def test_whitespace_stripped(self, dummy_df):
        assert dummy_df["VISA_CLASS"].iloc[0] == "H-1B"
