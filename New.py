import logging
logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)
from telethon import TelegramClient, events


api_id = api_id
api_hash = api_hash
bot_token = bot_token

Client = TelegramClient('hello', api_id, api_hash)

@Client.on(events.NewMessage)
async def my_event_handler(event):
    print(event)
    if 'hello' in event.raw_text:
        await event.reply('homeboy')
    if 'fine' in event.raw_text:
        await event.reply('Are you homeless?')


Client.start()
Client.run_until_disconnected()        