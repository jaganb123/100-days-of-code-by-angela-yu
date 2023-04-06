from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

try:
    driver = webdriver.Firefox()
    driver.get("https://www.linkedin.com/jobs/")
    email = driver.find_element(By.NAME, "session_key")
    email.send_keys("jagan22219971@gmail.com")
    password = driver.find_element(By.NAME, "session_password")
    password.send_keys("iamtherobot1" + Keys.ENTER )
    driver.implicitly_wait(15)
    driver.find_element(By.CSS_SELECTOR, "a[href=https://www.linkedin.com/jobs/?]").click()
    driver.implicitly_wait(10)
    search_bar = driver.find_element(By.CSS_SELECTOR, "input.jobs-search-box__text-input.jobs-search-box__keyboard-text-input")
    job_title = "devops engineer"
    location = "Chennai, Tamil Nadu, India"
    search_bar.send_keys(job_title, Keys.ENTER)
    # driver.implicitly_wait(10)
    # easy_apply_butn = driver.find_element(By.XPATH, '//*[@id="ember238"]')
    # easy_apply_butn.text
    # driver.implicitly_wait(10)

except Exception as e:
    print(e)
finally:
    pass
