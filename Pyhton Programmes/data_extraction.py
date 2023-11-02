

import requests
from bs4 import BeautifulSoup

url = "https://www.google.com/search?q=data+science"

# Make a GET request to fetch the raw HTML content
html_content = requests.get(url).text

# Parse the html content
soup = BeautifulSoup(html_content, "lxml")

# print(soup.prettify()) # print the parsed data of html

# Get the title of the page
print("Title:", soup.title.string)

# Get all the paragraphs in the page
all_paragraphs = soup.find_all('p')

# Print all the paragraphs
for para in all_paragraphs:
    print(para.string)