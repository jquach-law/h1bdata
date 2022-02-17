import bs4
from pathlib import Path
import requests
from datetime import datetime


class Data:
    def __init__(self):
        self._base_url = "https://www.dol.gov"
        self._url_to_scrape = (
            "https://www.dol.gov/agencies/eta/foreign-labor/performance"
        )
        self._file_name = None

    def _getHTMLdocument(self):
        """function to extract html document from given url"""
        # request for HTML document of given url
        response = requests.get(self._url_to_scrape)
        # response will be provided in JSON format
        return response.text

    def _set_file_name(self, year, quarter):
        self._file_name = f"a[href*=LCA_Disclosure_Data_FY{year}_{quarter}]"

    def _check_calendar(self, curr_mo=None, year=None):
        # Determine 'year' and 'quarter' for url
        if curr_mo is None and year is None:
            curr_mo = datetime.now().month
            year = datetime.now().year

        if 1 <= curr_mo <= 3:
            year -= 1
            quarter = "Q4"
        elif 4 <= curr_mo <= 6:
            quarter = "Q1"
        elif 7 <= curr_mo <= 9:
            quarter = "Q2"
        else:  # 10<= current month<=12
            quarter = "Q3"

        return year, quarter

    def _init_soup(self):
        # create document
        html_document = self._getHTMLdocument()
        # create soup object
        soup = bs4.BeautifulSoup(html_document, "html.parser")

        return soup

    def _init_query(self, year, quarter, manual_input=False):
        # Handle manual input
        if manual_input:
            self._set_file_name(year, quarter)
        else:
            # Sets url with correct year & quarter
            year, quarter = self._check_calendar()
            self._set_file_name(year, quarter)

        return self._file_name

    def _get_tag_elements(self, year=None, quarter=None, manual_input=False):
        soup = self._init_soup()
        query = self._init_query(year, quarter, manual_input)

        # Find the links to the relevant excel files
        matching_tag_elements = soup.select(query)

        return matching_tag_elements

    def download_file(self, year=None, quarter=None, manual_input=False):

        matching_tag_elements = self._get_tag_elements(year, quarter, manual_input)

        for tag_element in matching_tag_elements:

            # tag_element is the entire class a tag that contains the href so this will extract the value of href
            path = tag_element["href"]

            # href value is the  subdirectory so it's combined with the main website URL
            file_url = self._base_url + path
            # Download file to memory
            response = requests.get(file_url)

            # Create folder to hold the data
            if not Path("data").is_dir():
                Path("data").mkdir()

            # Save the data in memory to disk
            file_name = f"data/{file_url.split('/')[-1]}"
            with open(file_name, "wb") as output_file:
                output_file.write(response.content)


if __name__ == "__main__":
    get_excel_file = Data()

    ## MANUAL INPUT TESTING ##
    # asks the user to input year and date to filter out search query/download only one file
    # print('Enter the desired year: ')
    # year = int(input())
    # print('Which quarter? (Q1, Q2, Q3, Q4): ')
    # quarter = input()
    # get_excel_file.download_file(year, quarter, manual_input=True)

    ## AUTO INPUT: LATEST QUARTER ##
    # download latest quarter
    get_excel_file.download_file()

    # Test helper function, get_scrape_period function
    # Assign variable for current year and date
