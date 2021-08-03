import time
from telethon import TelegramClient, events

#API ID
api_id = 'your ip-id'
#API-hash
api_hash = 'your api hash'


phone_number = 'your phone number'
password = "two step verification if you have"
session_file = "TelegramClient('your telegram username')"

message = "your message for replying your contacts"

if __name__ == '__main__':
    client = TelegramClient(session_file,api_id, api_hash, sequential_updates=True)

    @client.on(events.NewMessage(incoming=True))
    async def handle_new_message(event):
        if event.is_private:
            from_ = await event.client.get_entity(event.from_id)
            if not from_.bot:
                print(time.asctime(), '-', event.message)
                time.sleep(1)
                await event.respond(message)
    print(time.asctime(), '-', 'Auto-replying...')
    client.start(phone_number, password)
    client.run_until_disconnected()
    print(time.asctime(), '-', 'Stopped!')