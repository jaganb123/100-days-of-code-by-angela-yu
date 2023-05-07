from utility import *
from amazon_price_tracker import amazonProduct
from notification_manager import NotificationManager
from json import JSONDecodeError
import time, json, logging

logger = logging.Logger('amazon_price_tracker')
ch = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
logger.addHandler(ch)

json_loc = "data/product.json"

productURL = ['https://www.amazon.in/AMD-5600G-Processor-12-thread-RadeonTM/dp/B092L9GF5N/','https://www.amazon.in/Crucial-DDR4-Desktop-Memory-CT8G4DFRA32A/dp/B08C4VHQV2/','https://www.amazon.in/Gigabyte-B450M-DS3H-Bluetooth-Motherboard/dp/B07VQJYR99/']
productList = []
def initializeObj(write=False, jsonStr=None):
    logger.info(f'Call for initializeOBJ(write={write}, ... )')
    global productList
    productList = []
    if not write:
        try:
            with open(json_loc, 'r') as file:
                productKW = json.load(file)
                for i in productKW:
                    tmpObj = amazonProduct(product=i)
                    productList.append(tmpObj)
                logger.info(f'productList has been populated')

        except (FileNotFoundError, JSONDecodeError) as error:
            logger.warning(f'{error}')
            logger.info(f'populating default url: {productURL}')
            for i in productURL:
                tmpObj = amazonProduct(i, product={})
                productList.append(tmpObj)
    else:
        jsonStr = [data.getDict() for data in jsonStr]
        logger.info(f'writing data back to products.json')
        with open(json_loc, "w") as file:
            json.dump(jsonStr, file, indent=2)
initializeObj()

#parse_mode = 'HTML' to allow string formatting on bot message
notif = NotificationManager()

while productList:

    for item in productList:
        if item.getPrice():
            item.updateHistoricalData()
            item.checkPrice()
            if item.notifReq:
                notif.notify(item.notifMessage)
                item.notifReq = False
        time.sleep(1)
    initializeObj(write=True, jsonStr=productList)
    logger.info(f'sleeping for {60 * 60 * 3}s')
    time.sleep(60 * 60 * 3)
    initializeObj()
