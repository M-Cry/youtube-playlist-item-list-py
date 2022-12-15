'''

'''

import requests

from bs4 import BeautifulSoup as bs
from selenium import webdriver


def main():
    url = 'https://www.youtube.com/playlist?list=PL37UZ2QfPUvz3k5mZNFZmjhLNTT-M5-Oa'

    # Making GET request
    # req = requests.get(url)
    browser = webdriver.Firefox()
    browser.get(url)
    html = browser.page_source

    # Parsing the HTML
    soup = bs(html, 'html.parser')

    # Getting the title tag
    # title = str(soup.title.text)
    # print(title)

    # video-title
    # Finding video title by id
    vid_title = soup.find_all('a', id= 'video-title')

    for t in vid_title:
        print(str(t.text).replace(" ", "").replace("\n", ""))

if __name__ == '__main__':
    main()
