from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Firefox()
driver.get("https://tinder.com/")
time.sleep(2)
login_btn = driver.find_element(By.CSS_SELECTOR,'div > a[href^="https://tinder.onelink.me/"]')
login_btn.click()
time.sleep(2)
select_google = driver.find_element(By.CSS_SELECTOR, 'div > span > div[role="button"]')
select_google.click()
time.sleep(3)
base_window = driver.window_handles[0]
google_window = driver.window_handles[1]
driver.switch_to.window(google_window)
print(driver.title)
email = driver.find_element(By.CSS_SELECTOR, 'div > input[type="email"]')
email.send_keys("jagan22219971@gmail.com" + Keys.ENTER)



print(len(driver.window_handles))