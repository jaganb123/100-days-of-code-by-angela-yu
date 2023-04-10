from utility import *

alert_set = False
while not alert_set:
    URL = input("Please enter URL for price alert or q to quit: ")
    if amazon_url_check(URL):
        json_str = get_json("products.json")
        html_str = get_html_response(URL)
        if html_str:
            data = extract_data(html_str)
            if not data:
                print("I can't get the price")
                break
            alert_price = input(f"the product name is {data[0]},\nand price is {data[1]}\n\nEnter amount to set alert..? ")
            
            if amount_validity(alert=alert_price, price=data[1]):
                json_str['products'].append([URL, alert_price])
                put_json("products.json", json_str)
                print("Hola, alert set, rest assured for you")
        else:
            print("can't parse the link, sorry...")
            break
    elif URL in "Qq":
        break
    else:
        user_decision = input("please enter correct amazon india url... or press 'q' to exit.. ")
        print(user_decision)
        if user_decision not in "\n" and user_decision in "Qq":
            break