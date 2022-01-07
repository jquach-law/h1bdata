from get_excel_file import Data
from datetime import datetime
import bs4

def test_1():
    assert 1 == 1

def test_getHTMLdocument():
    data = Data()
    data._url_to_scrape = "https://www.google.com"
    getdoc = data._getHTMLdocument
    assert type(getdoc()) is str

def test_set_file_name():
    data = Data()
    data._set_file_name(1965, "Q99")
    result_string = "a[href*=LCA_Disclosure_Data_FY1965_Q99]"
    assert data._file_name == result_string

def test_check_calendar():
    data = Data()
    yr_qrt = data._check_calendar(1, 2020)
    assert (2019, 'Q4') == yr_qrt
    yr_qrt = data._check_calendar(5, 2020)
    assert (2020, 'Q1') == yr_qrt
    yr_qrt = data._check_calendar(8, 2020)
    assert (2020, 'Q2') == yr_qrt
    yr_qrt = data._check_calendar(11, 2020)
    assert (2020, 'Q3') == yr_qrt

def test_init_soup():
    data = Data()
    soup = data._init_soup()
    assert type(soup) is bs4.BeautifulSoup

def test_init_query_input():
    data = Data()
    file_name = data._init_query(1965, 'Q99', True)
    result_string = "a[href*=LCA_Disclosure_Data_FY1965_Q99]"
    assert file_name == result_string

def test_init_query_default():
    data = Data()
    file_name = data._init_query(None, None, False)
    year, quarter = data._check_calendar()
    result_string = f"a[href*=LCA_Disclosure_Data_FY{year}_{quarter}]"
    assert file_name == result_string

def test_get_tag_elements():
    data = Data()
    tag = data._get_tag_elements()
    assert len(tag) == 1
    assert type(tag) is bs4.element.ResultSet


#     print(tag)
#     print(type(tag))
#     for element in tag:
#         print(element['href'])

# test_get_tag_elements()

# def test_scraped_period():
#     data = Data()
#     data._get_scraped_period()
#     year = datetime.now().year
    
#     should_name = f'a[href*=LCA_Disclosure_Data_FY{year}_{quarter}]'