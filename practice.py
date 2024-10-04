from anyio.abc import value
from selenium import webdriver
from selenium.webdriver.common.by import By

#editing our driver
c_options = webdriver.ChromeOptions()
c_options.add_experimental_option("detach", True)

#setting up driver
url = "https://www.shodan.io/"
driver = webdriver.Chrome(options=c_options)
driver.get(url)

heading = driver.find_element(By.TAG_NAME, value="h1")
print(heading.text)
print(heading.size)
print(heading.tag_name)
print(heading.location)
print(heading.parent)

heading_2 = driver.find_element(By.TAG_NAME, value="h2")
print(heading_2.text, "\n")


paragraph = driver.find_element(By.CSS_SELECTOR, value=".card-padding p")
print(paragraph.text)

print("\n\n\n")
#checking out xpath

xpath = driver.find_element(By.XPATH, value='/html/body/div[3]/div/section[1]/div[1]/a')
print(xpath.text)
print(xpath.tag_name)

driver.quit()