from selenium import webdriver
import time
import csv



def write_csv(data):
    with open("psb.csv", "a", newline="") as f:
        writer = csv.writer(f, delimiter=";")
        writer.writerow([data["name"],
                         data["like_count"],
                         data["region"],
                         data["business"],
                         data["purpose"]])


def main():
    driver = webdriver.Chrome()
    pattern = "https://psbank-grant.rbc.ru/competitors?card={}"

    for i in range(1, 2444):
        url = pattern.format(str(i))
        driver.get(url)
        time.sleep(3)

        number = i
        print(number)

        name = driver.find_element_by_xpath("/html/body/div[1]/div[6]/div[1]/div/div[6]/div/div/h3").text
        print(name)

        like_count = driver.find_element_by_xpath("/html/body/div[1]/div[6]/div[1]/div/div[6]/div/div/button").text
        print(like_count)

        region = driver.find_element_by_xpath("/html/body/div[1]/div[6]/div[1]/div/div[6]/div/div/div[1]").text
        region = region.replace('Регион: ', '')
        print(region)

        business_and_purpose = driver.find_element_by_xpath("/html/body/div[1]/div[6]/div[1]/div/div[6]/div/div/p").text
        grant = 'Грант нужен на:'
        grant_index = business_and_purpose.find(grant)

        business = business_and_purpose[7:grant_index].replace('\n', '')
        print(business)

        purpose = business_and_purpose[grant_index + 15:].replace('\n', '')
        print(purpose)

        data = {"number": number,
                "name": name,
                "like_count": like_count,
                "region": region,
                "business": business,
                "purpose": purpose}

        write_csv(data)


if __name__ == "__main__":
    main()
