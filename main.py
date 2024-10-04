from selenium import webdriver
from selenium.webdriver.common.by import By
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.amazon.ca/dp/B00HB56RH2/ref=syn_sd_onsite_desktop_0?ie=UTF8&pf_rd_p=bca40990-7045-44be-ad8f-604f24556a90&pf_rd_r=RQ6V3VEP1GCZA4YT70K3&pd_rd_wg=1rQsA&pd_rd_w=0sKhz&pd_rd_r=f234169c-bf7d-4461-b446-451e85cc0b8e&aref=7wXRh7fllD&th=1")

price_dollars = driver.find_element(By.CLASS_NAME, value="a-price-whole")

price_cents = driver.find_element(By.CLASS_NAME, value="a-price-fraction")
print(f"The price is {price_dollars.text}.{price_cents.text}")



driver.quit()
