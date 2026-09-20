#https://andrewkushnerov.medium.com/how-to-send-notifications-to-telegram-with-python-9ea9b8657bfb

from telegram import Bot as teleBot
import asyncio

TELEGRAM_BOT_TOKEN = '7590498352:AAEAIWHOXqfWZ4sTkyh_mbqTjLv2xUaEe24'
CHAT_ID = '734885929'

#Define bot
myBot = teleBot(token=TELEGRAM_BOT_TOKEN)

async def send_message(text, chat_id):
    async with myBot:
        await myBot.send_message(text=text, chat_id=CHAT_ID)




async def sendTele():
    # Sending a message
    await send_message(text='Hi Sujit!, How are you?', chat_id=CHAT_ID)


    asyncio.run(sendTele())

