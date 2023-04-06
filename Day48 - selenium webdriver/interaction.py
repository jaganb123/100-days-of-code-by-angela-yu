from selenium import webdriver
from selenium.webdriver.common.by import *
from selenium.webdriver.common.keys import Keys
import time

def upgrade():
    print(f"I got {money.text} cookies")
    buy_items  = driver.find_elements(By.CSS_SELECTOR, 'div[id="store"] div[class=""]')
    if buy_items:
        def fun(num):
            try:
                val = int(num[-1])
            except ValueError:
                val = int("".join(num[-1].split(",")))
            return val
        buy_price = []
        for i in buy_items:
            buy_price.append(i.find_element(By.TAG_NAME, "b").text.split())
        index = buy_price.index(max(buy_price, key=fun))
        print(f"I am gonna buy {buy_price[index][0]} for {buy_price[index][-1]} cookies")
        buy_items[index].click()

try:
    driver = webdriver.Firefox()
    driver.get("http://orteil.dashnet.org/experiments/cookie/")
    cookie = driver.find_element(By.ID, "cookie")
    money = driver.find_element(By.ID, "money")
    # buy_items  = driver.find_elements(By.CSS_SELECTOR, 'div[id="store"] div[class=""]')
    start_time = round(time.time())
    click_end = start_time + 300
    while time.time() <= click_end:
        step = time.time() + 5
        while time.time() <= step:
            cookie.click()
        upgrade()
    print("okay bye, I am done clicking")
except Exception as e:
    print(e)
finally:
    pass
    # driver.quit()
