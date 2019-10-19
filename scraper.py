from bs4 import BeautifulSoup
import urllib3
import re
import wget
import os

http = urllib3.PoolManager()

url = "https://aqs.epa.gov/aqsweb/airdata/download_files.html"
response = http.request('GET', url)
soup = BeautifulSoup(response.data)
links = []

for link in soup.findAll('a', attrs={'href': re.compile("^daily_4")}):
    links.append(link.get('href'))

base_link = "https://aqs.epa.gov/aqsweb/airdata/"

for link in links:
    zip_url = base_link + link
    wget.download(zip_url, "./data/"+link)
    print("Downloaded " + zip_url)
 print ('scraper')
