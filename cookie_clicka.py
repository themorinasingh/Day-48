from anyio.abc import value
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

url= "http://orteil.dashnet.org/experiments/cookie/"
driver = webdriver.Chrome(options=chrome_options)
driver.get(url)

cookie = driver.find_element(By.ID, value="cookie")
five_sec_timer = time.time() + 5
timeout = time.time() + 5 * 60
while True:
    cookie.click()

    if time.time() >= five_sec_timer:
        five_sec_timer = time.time() + 5
        num_cookies = int(driver.find_element(By.ID, value='money').text.replace(",",""))

        #buying the elements
        try:
            buy_time_machine = driver.find_element(By.ID, value="buyTime machine")
            time_machine = driver.find_element(By.ID, value="buyTime machine").text
            time_machine_price = int(time_machine.split("\n")[0].split(" ")[-1].replace(",", ""))


            if num_cookies >= time_machine_price:
                buy_time_machine.click()

        except:
            for i in range(100):
                cookie.click()

        try:
            buy_portal = driver.find_element(By.ID, value="buyPortal")
            portal = buy_portal.text
            portal_price = int(portal.split("\n")[0].split(" ")[-1].replace(",", ""))


            if num_cookies >= portal_price:
                buy_portal.click()
        except:
            for i in range(100):
                cookie.click()

        #buying alchemy lab
        try:
            buy_alchemy_lab = driver.find_element(By.ID, value="buyAlchemy lab")
            alchemy_lab = buy_alchemy_lab.text
            alchemy_lab_price = int(alchemy_lab.split("\n")[0].split(" ")[-1].replace(",", ""))


            if num_cookies >= alchemy_lab_price:
                buy_alchemy_lab.click()

        except:
            for i in range(100):
                cookie.click()

        #buying a mine
        try:
            buy_mine = driver.find_element(By.ID, value="buyMine")
            mine = buy_mine.text
            mine_price = int(mine.split("\n")[0].split(" ")[-1].replace(",", ""))


            if num_cookies >= mine_price:
                buy_mine.click()

        except:
            for i in range(100):
                cookie.click()

        #buying a factory
        try:
            buy_factory = driver.find_element(By.ID, value="buyFactory")
            factory = buy_factory.text
            factory_price = int(factory.split("\n")[0].split(" ")[-1].replace(",", ""))


            if num_cookies >= factory_price:
                buy_factory.click()

        except:
            for i in range(100):
                cookie.click()

        #buying a granny
        try:
            buy_granny = driver.find_element(By.ID, value="buyGrandma")
            granny = buy_granny.text
            granny_price = int(granny.split("\n")[0].split(" ")[-1].replace(",", ""))


            if num_cookies >= granny_price:
                buy_granny.click()

        except:
            for i in range(100):
                cookie.click()

        #buying a cursor
        try:

            buy_cursor = driver.find_element(By.ID, value="buyCursor")
            cursor = buy_cursor.text
            cursor_price = int(cursor.split("\n")[0].split(" ")[-1].replace(",", ""))


            if num_cookies >= cursor_price:
                buy_cursor.click()
        except:
            for i in range(100):
                cookie.click()

    score = driver.find_element(By.ID, value="cps").text
    score = score.split(" ")[-1]
    print(score)

    if time.time() >= timeout:
        break

score = driver.find_element(By.ID, value="cps").text
score = score.split(" ")[-1]

driver.quit()