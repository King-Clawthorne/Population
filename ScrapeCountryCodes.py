import requests
from bs4 import BeautifulSoup
from json import dumps

url = "https://www.populationpyramid.net/united-kingdom/2023/"
response = requests.get(url)

if response.status_code == 200:
  soup = BeautifulSoup(response.text, "html.parser")
  country_div = soup.find('div', id='countryDropdown')
  if country_div:
    country_links = country_div.find_all('a', class_='countryLink')
    tab = {}
    for link in country_links:
      country = link['country']
      slug = link['slug']
      href = link['href']
      text = link.text
      tab[slug] = country
    print(dumps(tab))
