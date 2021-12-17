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
        self._schedule = {datetime.now().year - 1: {}, datetime.now().year: {}}
        self._file_name = None

    def _generate_schedule(self):
        for month in range(1, 13):
            if 1 <= month <= 3:
                self._schedule[datetime.now().year - 1][month] = "Q4"
            elif 4 <= month <= 6:
                self._schedule[datetime.now().year][month] = "Q1"
            elif 7 <= month <= 9:
                self._schedule[datetime.now().year][month] = "Q2"
            else:
                self._schedule[datetime.now().year][month] = "Q3"

    def _getHTMLdocument(self):
        """function to extract html document from given url"""
        # request for HTML document of given url
        response = requests.get(self._url_to_scrape)
        # response will be provided in JSON format
        return response.text

    def _set_file_name(self, year, quarter):
        self._file_name = f"a[href*=LCA_Disclosure_Data_FY{year}_{quarter}]"

    def _get_scraped_period(self, year, quarter, manual_input=False):

        # create document
        html_document = self._getHTMLdocument()

        # create soup object
        soup = bs4.BeautifulSoup(html_document, "html.parser")

        # Handle manual input
        if manual_input:
            self._set_file_name(year, quarter)
            return soup, self._file_name

        # Get correct quarter period
        if 1 <= datetime.now().month and datetime.now().month <= 3:
            # Get Q4 of previous year if current month is 1~3,
            # as currenet year's Q1 data may not be out.
            quarter = self._schedule[datetime.now().year - 1][datetime.now().month]
        else:
            quarter = self._schedule[datetime.now().year][datetime.now().month]

        self._set_file_name(datetime.now().year, quarter)
        return soup, self._file_name

    def get_file(self, year=None, quarter=None, manual_input=False):

        self._generate_schedule()

        soup, query = self._get_scraped_period(year, quarter, manual_input)

        # Find the links to the relevant excel files
        matching_tag_elements = soup.select(query)

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

    # asks the user to input year and date to filter out search query/download only one file
    print("Enter the desired year: ")
    year = int(input())
    print("Which quarter? (Q1, Q2, Q3, Q4): ")
    quarter = input()

    get_excel_file.get_file(year, quarter, manual_input=True)

    # get_excel_file.get_file()

    # Test helper function, get_scrape_period function
    # Assign variable for current year and date
