import notification_manager
from utility import *

def notif(name, cur_price, url):
    message_string = f"""
    Low price alert!!!
    The product {name},
    is below the price you set, current price is {cur_price}, Grab the deal soon.
    [URL] ({url})
    """
    alert = notification_manager.NotificationManager()

    alert.notify(message_string)

check_list = get_json("products.json")['products']
for data in check_list:
    html_str = get_html_response(data[0])
    product_detail = extract_data(html_str)
    if float(product_detail[1]) <= int(data[1]):
        notif(name=product_detail[0], cur_price=product_detail[1], url=data[0])
    

