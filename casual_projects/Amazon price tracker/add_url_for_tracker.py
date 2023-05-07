import utility


logger = utility.logger()

userInput = input('Please enter amazon.in URL to track: ')
if utility.amazon_url_check(userInput):
    data: list = utility.get_json('product.json')
    data.append({'url': userInput})
    logger.info(f'added url : {userInput}')
    utility.put_json("data/product.json", data=data)
