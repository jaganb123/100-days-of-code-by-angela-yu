import asyncio
import telegram


async def notify(bot, user_id, msg):
    async with bot:
        await bot.send_message(user_id, msg)
        # print((await bot.get_updates()))


class NotificationManager:
    def __init__(self):
        self.access_token = "5851561281:AAHz2GE_2oBHDV4XrpoFdftabct5cOP4Ueo"
        self.user_id = -819053142
        self.bot = telegram.Bot(self.access_token)

    def notify(self, msg):
        asyncio.run(notify(self.bot, self.user_id, msg))
    # This class is responsible for sending notifications with the deal flight details.
