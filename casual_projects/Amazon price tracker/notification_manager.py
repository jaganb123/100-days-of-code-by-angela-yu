import asyncio, telegram, logging

logger = logging.Logger('telegram_bot')
ch = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
logger.addHandler(ch)

async def notify(bot, user_id, msg):
    async with bot:
        logger.info(f'user id: {user_id}, msg:\n{msg}')
        await bot.send_message(user_id, msg, parse_mode='html', disable_web_page_preview=True)

class NotificationManager:
    def __init__(self):
        self.access_token = "5851561281:AAHz2GE_2oBHDV4XrpoFdftabct5cOP4Ueo"
        self.user_id = -819053142
        self.bot = telegram.Bot(self.access_token)

    def notify(self, msg):
        asyncio.run(notify(self.bot, self.user_id, msg))
    # This class is responsible for sending notification.