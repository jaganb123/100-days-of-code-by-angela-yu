import requests, json, logging
from bs4 import BeautifulSoup

# https://www.amazon.in/HP-M22f-21-5-Inch-Micro-Edge-Monitor/dp/B095381Z51/ref=sr_1_6?keywords=monitor%2Bfull%2Bhd&qid=1675767911&sprefix=monitor%2Bfull%2Bhd%2Caps%2C336&sr=8-6&th=1
URL = "https://www.amazon.in/GIGABYTE-Graphics-WINDFORCE-GV-N3050GAMING-OC-8GD/dp/B09QVPMGYV/ref=sr_1_4?keywords=3050+graphic+card&qid=1675763933&sprefix=3050%2Caps%2C533&sr=8-4"

def amazon_url_check(url: str):
    if url.startswith("https://www.amazon.in/"):
        return True
    else: 
        return False

def logger() -> logging:
    logger = logging.Logger('amazon_price_tracker')
    ch = logging.StreamHandler()
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    ch.setFormatter(formatter)
    logger.addHandler(ch)
    return logger


def get_html_response(URL):
    try:
        header = {
            "Accept-Encoding": "gzip, deflate",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/109.0"
        }
        response = requests.get(url=URL, headers=header)
        return response.text
    except Exception as e:
        print(f"Got exception : {e}")
        return False

def extract_data(html: str):
    try: 
        soup = BeautifulSoup(html, "html.parser")
        current_price = json.loads(soup.find(name="div", class_="twister-plus-buying-options-price-data").string)[0]['priceAmount']
        product_name = soup.find(name="span", id="productTitle").string
        return (product_name, current_price)
    except Exception as e:
        print(f"oops got the exception: {e}")
        return False

def amount_validity(alert, price):
    try:
        alert = int(alert)
        if alert >= price:
            raise Exception(f"Invalid Input, alert amount {alert} should be less than price amount {price}")
        if alert < price:
            return True
    except Exception as e:
        print(f"oops got exception: {e}")
        return False

def get_json(path: str):
    try:
        with open(path, "r") as file:
            json_str = json.load(file)
        return json_str
    except FileNotFoundError as e:
        print(e)
        return []
    except Exception as e:
        print(e)
        return False

def put_json(path: str, data: str):
    try:
        with open(path, "w") as file:
            json.dump(data, file, indent= 2)
        return True
    except Exception as e:
        print(e)
        return False

