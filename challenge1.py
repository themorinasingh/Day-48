from selenium import webdriver
from selenium.webdriver.common.by import By

#setup options
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

#setup driver
url= "https://www.python.org/"
driver = webdriver.Chrome(options=chrome_options)
driver.get(url)

#Todo all search will go here
date_list = driver.find_elements(By.CSS_SELECTOR, value=".event-widget ul time")
event_names = driver.find_elements(By.CSS_SELECTOR,value= '.event-widget .menu li a ')
# for date in date_list:
#     print(date)
# for event in event_names:
#     print(event.text)

event_dict = {}

for i in range(len(date_list)):
    event_dict[i + 1] = {date_list[i].get_attribute("datetime").split("T")[0]: event_names[i].text}

print(event_dict)

#exiting program and browser
driver.quit()