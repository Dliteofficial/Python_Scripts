from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException
from tabulate import tabulate

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://books.toscrape.com/")

product_count = int(driver.find_element(By.CLASS_NAME, "form-horizontal").text.split(" ")[0])
print(f"{product_count} products available to scrape")

data = []

def scrape():
    titles = driver.find_elements(By.XPATH, "//ol[@class = 'row']//article//h3/a")
    prices = driver.find_elements(By.XPATH, "//ol[@class = 'row']//article//p[@class = 'price_color']")
    availabilities = driver.find_elements(By.XPATH, "//ol[@class = 'row']//article//p[@class = 'instock availability']")
    #links = driver.find_elements(By.XPATH, "//ol[@class = 'row']//article//a")

    for i in range(len(titles)):
        title = titles[i].get_attribute("title")
        price = prices[i].text.split("£")[1]
        availability = availabilities[i].text
        #link = links[i].get_attribute("href")
        individual_data = {
            "Title" : title,
            "Price ($)" : price,
            "Availability" : availability
            #"Product Link" : link
        }
        data.append(individual_data)

def writeToFile(filename, data):
    with open(filename, "w") as file:
        file.write(data)

while True:
    try:
        page_numbers = driver.find_elements(By.XPATH, "//form//strong")
        page_number = int(page_numbers[2].text)
        if page_number < product_count:
            scrape()
            driver.find_element(By.LINK_TEXT, 'next').click()
        elif page_number == product_count:
            scrape()
            break
    except WebDriverException as e:
        print(f"ERR: Encountered {e} error while scrapping")

collated_data = tabulate(data, headers="keys", tablefmt="pipe", showindex="always")
writeToFile("Result.md", collated_data)