import bs4
from pathlib import Path
import requests

BASE_URL = 'https://www.dol.gov'


# function to extract html document from given url
def getHTMLdocument(url):
    # request for HTML document of given ur./venv/bin/python get_excel_file.pyl
    response = requests.get(url)
    # response will be provided in JSON format
    return response.text


url_to_scrape = 'https://www.dol.gov/agencies/eta/foreign-labor/performance'

# create document
html_document = getHTMLdocument(url_to_scrape)

# create soup object
soup = bs4.BeautifulSoup(html_document, 'html.parser')

# Find the links to the relevant excel files
matching_tag_elements = soup.select('a[href*="LCA_Disclosure_Data"]')

for tag_element in matching_tag_elements:
    path = tag_element['href']

    file_url = BASE_URL + path
    # Download file to memory
    response = requests.get(file_url)

    # Create folder to hold the data
    if not Path('data').is_dir():
        Path('data').mkdir()

    # Save the data in memory to disk
    file_name = f"data/{file_url.split('/')[-1]}"
    with open(file_name, 'wb') as output_file:
        output_file.write(response.content)

