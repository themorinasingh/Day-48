from anyio.abc import value
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

#setup option for our driver
web_d_options = webdriver.ChromeOptions()
web_d_options.add_experimental_option("detach", True)

#setup the driver
url = "https://secure-retreat-92358.herokuapp.com/"
driver = webdriver.Chrome(web_d_options)
driver.get(url)

first_name = driver.find_element(By.NAME, value="fName")
time.sleep(2)
first_name.send_keys("TunakTunakTun")

last_name = driver.find_element(By.NAME, value="lName")
time.sleep(2)
last_name.send_keys("Tara rara")

email = driver.find_element(By.NAME, value="email")
time.sleep(2)
email.send_keys("tunaktunak@cyberdude.com")

submit = driver.find_element(By.TAG_NAME, value='button')
time.sleep(2)
submit.click()

time.sleep(10)
driver.quit()