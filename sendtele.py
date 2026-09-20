#https://andrewkushnerov.medium.com/how-to-send-notifications-to-telegram-with-python-9ea9b8657bfb

from telegram import Bot as teleBot
import asyncio

TELEGRAM_BOT_TOKEN = '7590498352:AAEAIWHOXqfWZ4sTkyh_mbqTjLv2xUaEe24'
CHAT_ID = '734885929'

#Define bot
#Define bot
bot = teleBot(token=TELEGRAM_BOT_TOKEN)

async def send_message(text, chat_id):
    async with bot:
        await bot.send_message(text=text, chat_id=chat_id)

async def run_bot(messages, chat_id):
    text = '\n'.join(messages)
    await send_message(text, chat_id)

#Test messages
messages = [
    'Product https://www.amazon.com/dp/B08C1W5N87, the price has changed from $24.99 to $26.99',
    'New negative review (rating 2) added for product https://www.amazon.com/dp/B0CL61F39H',
    'Attention! Average sales are 50% lower than usual over the last 3 hours!'
]

if messages:
    asyncio.run(run_bot(messages, CHAT_ID))