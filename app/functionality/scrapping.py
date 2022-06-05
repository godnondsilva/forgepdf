import csv
from bs4 import BeautifulSoup
from selenium import webdriver
from app import scrapy
import os

from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--headless")


# URL GENERATOR
def get_url(search_term):
    search_term = search_term.replace(' ', '+')
    url = f'https://www.amazon.in/s?k={search_term}&ref=nb_sb_noss_1'+'&page={}'
    return url


# URL ITEM EXTRACTOR
def extract_record(item):
    # product name and url extracter
    atag = item.h2.a
    product_name = atag.text.strip()

    try:
        # price extracter
        price_parent_tag = item.find('span', 'a-price')
        price = price_parent_tag.find('span', 'a-offscreen').text[1:]
    except AttributeError:
        return

    try:
        # rating and review count extracter
        rating = item.i.text
        review_count = item.find('span', {'class': 'a-size-base'}).text
    except AttributeError:
        rating = '-'
        review_count = '-'

    # result in a tuple
    product_detail = (product_name, price, rating, review_count)
    return product_detail


def main(search_term):
    search_term = search_term.strip().lower()
    product_list = []
    url = get_url(search_term)  # function call
    driver = webdriver.Chrome(
        executable_path=os.getenv('CHROME_DRIVER_PATH'), options=options)
    print("Generating CSV File .....")

    for page in range(1, 3):
        driver.get(url.format(page))
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        search_result = soup.find_all(
            'div', {'data-component-type': 's-search-result'})
        for item in search_result:
            record = extract_record(item)
            if record:
                product_list.append(record)
    driver.close()
    # Flushing the data into csv file
    product_list_file = open('productListFile.csv', 'w',
                             newline='', encoding='utf-8')
    writer = csv.writer(product_list_file)
    writer.writerow(['Product Name', 'Price', 'Rating', 'Review Count', 'Url'])
    writer.writerows(product_list)
    product_list_file.close()
    print("CSV Generated!")
    return True
