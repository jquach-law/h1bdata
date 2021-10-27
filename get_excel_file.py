import requests
import bs4

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

# Get to excel
tag_element = soup.find(title='PERM Disclosure Data FY2021')
path = tag_element['href']

file_url = BASE_URL + path
print(file_url)

# Download file to memory
response = requests.get(file_url)

# Save the file to disk
file_name = file_url.split('/')[-1]
with open(file_name, 'wb') as output_file:
    output_file.write(response.content)
