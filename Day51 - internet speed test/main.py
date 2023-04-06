from lib.internet_speed import InternetSpeedTwitterBot

bot = InternetSpeedTwitterBot()

internet_speed = bot.get_internet_speed()

# message = ("Hei, My internet speed is as below\n"
#            f"\tmy download speed is {internet_speed['download']['speed']} {internet_speed['download']['unit']}\n"
#            f"\tmy upload speed is {internet_speed['upload']['speed']} {internet_speed['upload']['unit']}\n"
#            )

message = ("Hei, My internet speed is >> "
           f"download speed is {internet_speed['download']['speed']} {internet_speed['download']['unit']}, "
           f"my upload speed is {internet_speed['upload']['speed']} {internet_speed['upload']['unit']}...")

print(message)

bot.tweet_at_provider(message)
