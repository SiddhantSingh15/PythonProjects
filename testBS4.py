from urllib.request import urlopen
from bs4 import BeautifulSoup as soup

my_url = 'https://www.f1-fansite.com/f1-result/qualifying-results-2020-austrian-f1-gp/'
page = urlopen(my_url)

contents = soup(my_url, 'html.parser')

print(contents)