from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time

chrome_options = Options()
chrome_options.headless = True

driver = webdriver.Chrome(options=chrome_options)

try:
    driver.get("https://nz.ua")
    time.sleep(0.01)
    page_source = driver.page_source

    soup = BeautifulSoup(page_source, "html.parser")
    block = soup.find("div", class_="lp-wrapp")
    
    if block:
        paragraph = block.find("p")
        if paragraph:
            print("Знайдений текст:", paragraph.text)
        else:
            print("Текстовий елемент <p> не знайдено.")
    else:
        print("Елемент з класом ")
finally:
    driver.quit()


x=6236262
print("hu")