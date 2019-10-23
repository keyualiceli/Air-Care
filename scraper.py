from bs4 import BeautifulSoup
import urllib3
import re
import wget
import os

def main():
    http = urllib3.PoolManager()

    # url for zip files
    url = "https://aqs.epa.gov/aqsweb/airdata/download_files.html"
    response = http.request('GET', url)
    soup = BeautifulSoup(response.data)
    links = []  # store zip names

    # scrape data from page
    for link in soup.findAll('a', attrs={'href': re.compile("^daily_4")}):
        links.append(link.get('href'))

    base_link = "https://aqs.epa.gov/aqsweb/airdata/"  # base link of all zip files

    # download zip files
    for link in links:
        zip_url = base_link + link
        # store in data/
        wget.download(zip_url, "./data/"+link)
        print("Downloaded " + zip_url)


if __name__ == '__main__':
    main()
