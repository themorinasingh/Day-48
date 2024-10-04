from anyio.abc import value
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
#lets make a program that does a google search

chrome_opt = webdriver.ChromeOptions()
chrome_opt.add_experimental_option("detach", True)

url = "https://www.google.ca/"
driver = webdriver.Chrome(options=chrome_opt)
driver.get(url)

search_bar = driver.find_element(By.ID, value="APjFqb")
print(search_bar.size)

search_bar.send_keys("Angela Yu")
search_bar.send_keys(Keys.ENTER)

time.sleep(10)
driver.quit()

