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
