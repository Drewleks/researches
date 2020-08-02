import requests
import csv
import time
from bs4 import BeautifulSoup
from selenium import webdriver


start_time = time.time()

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:45.0) Gecko/20100101 Firefox/45.0'}


def get_html(url):
    r = requests.get(url, headers=headers)
    if r.ok:
        return r.text
    print(r.status_code)


def write_csv(data):
    with open("psb.csv", "a", newline="") as f:
        writer = csv.writer(f, delimiter=";")
        writer.writerow([data["name"],
                         data["like_count"],
                         data["region"],
                         data["business"],
                         data["purpose"]])


def get_page_data(html):
    soup = BeautifulSoup(html, "html.parser")
    card = soup.find("div", class_="competition__card is -full")
    print(card)

    # Название компании 1
    try:
        name = card.find("h3", class_="competition__name").txt
    except:
        name = "none"

    # Количество лайков 2
    try:
        like_count = card.find("h3").find("a").get("href")
    except:
        like_count = "none"

    # Регион 3
    try:
        region = card.find("span", class_="price").get("content")
    except:
        region = "none"

    # Описание бизнеса 4
    try:
        business = card.find("div", class_="data").find("p").text
    except:
        business = "none"

    # Цели гранта 5
    try:
        purpose = card.find("div", class_="data").find("p").text
    except:
        purpose = "none"

    data = {"name": name,
            "like_count": like_count,
            "region": region,
            "business": business,
            "purpose": purpose}

    write_csv(data)


def main():
    pattern = "https://psbank-grant.rbc.ru/competitors?card={}"

    for i in range(1, 2):
        url = pattern.format(str(i))
        get_page_data(get_html(url))
        #time.sleep(1)


print("--- %s seconds ---" % (time.time() - start_time))

if __name__ == "__main__":
    main()

