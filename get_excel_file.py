import bs4
from pathlib import Path
import requests

BASE_URL = 'https://www.dol.gov'


# function to extract html document from given url
def getHTMLdocument(url):
    # request for HTML document of given url
    response = requests.get(url)
    # response will be provided in JSON format
    return response.text


url_to_scrape = 'https://www.dol.gov/agencies/eta/foreign-labor/performance'

# create document
html_document = getHTMLdocument(url_to_scrape)

# create soup object
soup = bs4.BeautifulSoup(html_document, 'html.parser')

# asks the user to input year and date to filter out search query/download only one file
print('Enter the desired year: ')
year = input()
print('Which quarter? (Q1, Q2, Q3, Q4): ')
quarter = input()

# query = 'a[href*=LCA_Disclosure_Data_FY2021_Q4]'
query = 'a[href*=LCA_Disclosure_Data_FY' + year + '_' + quarter + ']'

# query = 'a[href*="LCA_Disclosure_Data"]'

# Find the links to the relevant excel files
matching_tag_elements = soup.select(query)


for tag_element in matching_tag_elements:

    # tag_element is the entire class a tag that contains the href so this will extract the value of href
    path = tag_element['href']

    # href value is the  subdirectory so it's combined with the main website URL
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

