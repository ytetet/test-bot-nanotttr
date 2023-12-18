import asyncio
from telethon import TelegramClient, events

# Вставь свои собственные значения
api_id = 8411715
api_hash = "5d1e64c612152a060197db12f2927871"

client = TelegramClient('session_name', api_id, api_hash)

@client.on(events.NewMessage(pattern='/start'))

async def start_handler(event):
    
    await event.respond("test")

async def main():
    # Запускаем клиент
    await client.start()
    
    
    # Останавливаем клиент
    await client.run_until_disconnected()

# Запускаем асинхронную функцию
if __name__ == '__main__':
    asyncio.run(main())