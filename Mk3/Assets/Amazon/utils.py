from bs4 import BeautifulSoup as Bea
from selenium import webdriver
import csv
import pandas as pd
import os


def get_url(search_term):
    """"Generate a url from search term"""
    template = "https://www.amazon.com/s?k={}&ref=nb_sb_noss_2"
    search_term = search_term.replace(" ", "+")

    url = template.format(search_term)
    url += "&page={}"
    return url


def extract_record(item):
    try:
        atag = item.h2.a
        description = atag.text.strip()
        url = "https://www.amazon.com" + atag.get("href")
        price_parent = item.find('span', 'a-price')
        price = price_parent.find('span', 'a-offscreen').text
        price = price.replace(",", "")
        price = price.replace("$", "")
    except AttributeError:
        return
    try:
        parent_other_price = item.find('span', 'a-price a-text-price')
        otherprice = parent_other_price.find('span', 'a-offscreen').text
        otherprice = otherprice.replace(",", "")
        otherprice = otherprice.replace("$", "")

    except:
        otherprice = price

    discount = float(price) - float(otherprice)

    try:
        rating = item.i.text
        review_count = item.find('span', {'class': 'a-size-bas', 'dir': 'auto'}).text
    except AttributeError:
        rating = ''
        review_count = ''

    result = (description, price, rating, review_count, url, discount)
    return result


def main(search_term):
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    driver = webdriver.Chrome(executable_path=".\\Amazon\\chromedriver.exe", options=options)

    records = []
    url = get_url(search_term)

    for page in range(1, 151):
        driver.get(url.format(page))
        soup = Bea(driver.page_source, 'html.parser')
        results = soup.find_all('div', {'data-component-type': 's-search-result'})

        for item in results:
            record = extract_record(item)
            if record:
                records.append(record)
    driver.close()

    with open('results.csv', 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['description', 'price', 'rating', 'review_count', 'url', 'discount'])
        writer.writerows(records)
        print("done gathering results")


def sort_results_by_price(filename):
    data = pd.read_csv(filename)
    print("started sorting by price...")
    data.sort_values(["price"], ascending=True, inplace=True, axis=0)
    print("sorted values")
    data.to_csv(path_or_buf="./sorted_by_price.csv")
    print("done")


def sort_results_by_discount(filename):
    data = pd.read_csv(filename)
    print("started sorting by discount...")
    data.sort_values(["discount"], ascending=True, inplace=True, axis=0)
    print("sorted values")
    data.to_csv(path_or_buf="./sorted_by_discount.csv")
    os.remove("results.csv")
    print("done")
    

def get_discount_page(filename):
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(executable_path=".\\Amazon\\chromedriver.exe", options=options)
    data = pd.read_csv(filename)
    dataset = data.iloc[0]
    dataset = list(dataset)
    url = dataset[5]
    driver.get(url)
