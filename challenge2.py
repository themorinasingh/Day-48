from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

url = "https://en.wikipedia.org/wiki/Main_Page"
driver = webdriver.Chrome()
driver.get(url)

text_to_find = driver.find_element(By.CSS_SELECTOR, value="#articlecount a")
print(text_to_find.text)

driver.quit()