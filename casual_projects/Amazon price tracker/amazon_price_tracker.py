from utility import *
import math, logging


# logger = logging.Logger('amazon_price_tracker')
# ch = logging.StreamHandler()
# formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
# ch.setFormatter(formatter)
# logger.addHandler(ch)


class amazonProduct:
    
    def __init__(self, url=None, **product) -> None:
        self.logger_create()
        logger = self.logger
        product = product.get('product')
        if url != None:
            logger.info(f'Initialized with url: {url}')
            self.URL = url
            product = {}
        else:
            logger.info(f'parsing data from **product')
            self.URL = product.get('url', None)
            logger.info(f'url is {self.URL}')
        self.PRODUCT_NAME = product.get('name', None)
        self.historicalPrice = product.get('historicalPrice', None)
        self.minPrice = product.get('minPrice', None)
        self.maxPrice = product.get('maxPrice', None)
        self.avgPrice = product.get('avgPrice', None)
        self.notifReq = False

    def logger_create(self):
        self.logger = logging.Logger('tracker_class')
        ch = logging.StreamHandler()
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        ch.setFormatter(formatter)
        self.logger.addHandler(ch)


    def updateHistoricalData(self):
        if self.historicalPrice == None:
            self.historicalPrice = [int(self.Price)]
        else:
            if len(self.historicalPrice) > 100:
                startRange = len(self.historicalPrice) - 99
                self.historicalPrice = self.historicalPrice[startRange:]
            self.historicalPrice.append(int(self.Price))
        self.minPrice = min(self.historicalPrice)
        self.maxPrice = max(self.historicalPrice)
        self.avgPrice = int(math.floor(sum(self.historicalPrice)/len(self.historicalPrice)))
            

    def getPrice(self):
        product_response = extract_data(get_html_response(self.URL))
        if product_response:
            self.Price = product_response[1]
            tmp_ProductName = ' '.join(product_response[0].split())
            if self.PRODUCT_NAME == None or self.PRODUCT_NAME != tmp_ProductName:
                self.PRODUCT_NAME = tmp_ProductName
            self.logger.info(f'{self.PRODUCT_NAME} : {self.Price}')
            return True
        else:
            return False
    
    def checkPrice(self):
        # if self.Price < self.avgPrice:
        #     self.logger.info('price is less tha average')
        #     self.prepareMsg(f'Price Drop alert!!\nPrice lower than average!!')
        #     self.notifReq = False
        percentage = round(((self.historicalPrice[-1] * 100) /self.Price), 1)
        if self.Price < self.minPrice:
            self.logger.info('price is less tha minimum')
            self.prepareMsg('Best Bet, Price Drop alert!!\nPrice lower than Minimum!!')
            self.notifReq = True
        elif self.Price < self.historicalPrice[-1] :
            percentage = math.floor((self.historicalPrice[-1] * 100) /self.Price)
            self.logger.info('price is reduced by since last check')
            self.prepareMsg(f'Price dropped, Price dropped {percentage}% since last check!!')
            self.notifReq = True
        elif self.Price > self.historicalPrice[-1]:
            self.logger.info('price is increased since last check')
            self.prepareMsg(f'Price increased {percentage}%, Last price {self.historicalPrice[-1]}')
            self.notifReq = True
        else:
            self.logger.info('no change in price')
            self.notifReq = False

    def prepareMsg(self, prefixStr=None):
        self.notifMessage = (f'<a href="{self.URL}">{self.PRODUCT_NAME}</a>\n'
                    f'<em>MinPrice:</em> <b>{self.minPrice}</b>\n'
                    f'<em>MaxPrice:</em> <b>{self.maxPrice}</b>\n'
                    f'<em>AvgPrice:</em> <b>{self.avgPrice}</b>\n'
                    f'<em>currentPrice:</em> <b>{self.Price}</b>')
        if prefixStr != None:
            self.notifMessage = prefixStr + self.notifMessage

    def getDict(self):
        tmp = {
           'url': self.URL,
           'name': self.PRODUCT_NAME,
           'historicalPrice': self.historicalPrice,
           'minPrice': self.minPrice,
           'maxPrice': self.maxPrice,
           'avgPrice' : self.avgPrice
        }
        return tmp
