from os import link
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import Options
from bs4 import BeautifulSoup
import time

chrome_options = Options()
user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36'
chrome_options.add_argument(f'user-agent={user_agent}')
# chrome_options.add_argument("--headless")
driver = webdriver.Chrome(options=chrome_options)

driver.get('https://www.zomato.com/melbourne/springvale-restaurants')
print(driver.title)

SCROLL_PAUSE_TIME = 3

# Get scroll height
last_height = driver.execute_script("return document.body.scrollHeight")

while True:
    # Scroll down to bottom
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
    time.sleep(SCROLL_PAUSE_TIME)
    new_height = driver.execute_script("return document.body.scrollHeight")
    print(new_height)
    if new_height == last_height:
        break
    last_height = new_height

print('all the way at the bottom')
html = driver.page_source
time.sleep(2)
file_to_write = open("page_source.html", "w")
file_to_write.write(html)
file_to_write.close()
driver.quit()
