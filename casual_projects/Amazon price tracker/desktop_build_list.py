from amazon_price_tracker import amazonProduct

class Item(amazonProduct):
    def __init__(self, url) -> None:
        super().__init__(url)
        self.getPrice()
        
    # def parse_url(self):
    #     return self.getPrice()

item = Item(url="https://www.amazon.in/AMD-Ryzen-5600-Processor-100-100000927BOX/dp/B09VCHR1VH/")

# print(dir(item))
print(item.PRODUCT_NAME, item.Price)

product_list = {
    "cpu": 'https://www.amazon.in/AMD-5600G-Processor-12-thread-RadeonTM/dp/B092L9GF5N/',
    "motherBoard": "https://www.amazon.in/GIGABYTE-B450M-DS3H-Ryzen-Motherboard/dp/B07FWVJSHC/",
    "ram": "https://www.amazon.in/Crucial-DDR4-Desktop-Memory-CT8G4DFRA32A/dp/B08C4VHQV2",
    "m.2Ssd": "https://www.amazon.in/Crucial-500GB-PCIe-NAND-3500MB/dp/B0B25LQQPC",
    "graphicCard": "https://www.amazon.in/GIGABYTE-GeForce-WINDFORCE-Graphics-GV-N1656WF2OC-4GD/dp/B086T6W63R",
    "PSU": "https://www.amazon.in/ZEBRONICS-80-protections-Zeb-PGP450W-Plus/dp/B09RV5R1MP",
    "Cabinet": "https://www.amazon.in/Ant-Esports-ICE-120AG-Motherboard-Preinstalled/dp/B08CGCRNMS",
    "Monitor": "https://www.amazon.in/Zebronics-Zeb-1920x1080-Brightness-mountable/dp/B09X3BP3FK"
}

Item_list = []
for key, item in product_list.items():
    item = Item(url=item)
    if item != None:
            Item_list.append(item)

total = 0
for item in Item_list:
    total += item.Price
    print(item.PRODUCT_NAME, item.Price)

print(f"Total price is {total} INR")



