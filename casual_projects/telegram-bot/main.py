import asyncio
import telegram

# first_name='Jagan', id=1115502678


async def main():
    bot = telegram.Bot("5851561281:AAHz2GE_2oBHDV4XrpoFdftabct5cOP4Ueo")
    async with bot:
        await bot.send_message(-819053142, "Hello Telegram")
        # print((await bot.get_updates()))

if __name__ == '__main__':
    asyncio.run(main())