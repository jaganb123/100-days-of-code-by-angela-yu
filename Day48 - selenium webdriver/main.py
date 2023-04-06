from selenium import webdriver
from selenium.webdriver.common.by import By

def grab_data(obj):
    pass

try: 
    driver = webdriver.Firefox()
    driver.get("https://www.python.org/")
    date_time_li = driver.find_elements(By.CSS_SELECTOR, ".event-widget .shrubbery li time")
    event_li = driver.find_elements(By.CSS_SELECTOR, ".event-widget .shrubbery li a")
    event_dict = {}
    for i in range(len(event_li)):
        date = date_time_li[i].get_attribute("datetime").split("T")[0]
        event = event_li[i].text
        event_dict[i] = {"time": date, "event": event}
    print(event_dict)
except Exception as e:
    print(e)
finally:
    driver.quit()
