import requests
from bs4 import BeautifulSoup
import re
from requests_html import HTMLSession
from requests_html import AsyncHTMLSession
from selenium import webdriver 
from selenium.webdriver.chrome.options import Options



def amazon_scrape_web(product):

    url = 'https://www.amazon.ae/s?k=' + product.replace(' ','+')

    

    headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2 Safari/601.3.9'}

    page = requests.get(url, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    results = soup.find('span', cel_widget_id='MAIN-SEARCH_RESULTS-1')
    title = results.find('span', class_="a-size-base-plus a-color-base a-text-normal").text
    image = results.find('img')['src']
    link = 'https://amazon.ae' + results.find('a')['href']
    price = results.find('span', class_="a-price-whole").text

    return [title, image, link, price]

def noon_scrape_web(product):
    
    url = 'https://www.noon.com/uae-en/search?q=' + product.replace(' ',"%20")
    # session = HTMLSession()
    # session.browser
    # t = Thread(target=render_html)
    # t.start()
    chrome_options = Options()
    #chrome_options.add_argument("--disable-extensions")
    #chrome_options.add_argument("--disable-gpu")
    #chrome_options.add_argument("--no-sandbox") # linux only
    chrome_options.add_argument("--headless")
    # chrome_options.headless = True # also works
    r = webdriver.Chrome(options=chrome_options)

    r.get(url)
    

    # product = r.html.find('.productContainer', first=True)
    soup = BeautifulSoup(r.page_source, 'html.parser')
    results = soup.find('div', class_='productContainer')
    title = results.find('div', class_='e3js0d-10 cyUANN').text
    image = results.find('div', class_='puv25r-2 cwZEwU').find('img')['src']
    link = 'https://noon.com' + results.find('a')['href']
    price = results.find('div', class_="sc-3751lm-1 eUJkVt large").find('strong').text
    r.quit()

    return [title, image, link, price]

# def render_html(url):

#     r = session.get(url)
#     return r.html.render()
