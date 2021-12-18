from get_excel_file import Data
from datetime import datetime

def test_1():
    assert 1 == 1

def test_HTML():
    data = Data()
    data._url_to_scrape = "https://www.google.com"
    getdoc = data._getHTMLdocument
    assert type(getdoc()) is str

def test_href_string():
    data = Data()
    data._set_file_name("1965", "Q99")
    result_string = "a[href*=LCA_Disclosure_Data_FY1965_Q99]"
    assert data._file_name == result_string

def test_calendar():
    data = Data()
    yr_qrt = data._check_calendar(1, 2020)
    assert (2019, 'Q4') == yr_qrt
    yr_qrt = data._check_calendar(5, 2020)
    assert (2020, 'Q1') == yr_qrt
    yr_qrt = data._check_calendar(8, 2020)
    assert (2020, 'Q2') == yr_qrt
    yr_qrt = data._check_calendar(11, 2020)
    assert (2020, 'Q3') == yr_qrt

# def test_scraped_period():
#     data = Data()
#     data._get_scraped_period()
#     year = datetime.now().year
    
#     should_name = f'a[href*=LCA_Disclosure_Data_FY{year}_{quarter}]'