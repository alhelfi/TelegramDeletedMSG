from telethon import TelegramClient, events
import asyncio

# Client Settings
api_id = 'YOUR_API_ID'  # Enter your API ID
api_hash = 'YOUR_API_HASH'  # Enter your API Hash
phone_number = '+YOUR_PHONE_NUMBER'  # Enter your phone number , example +9997711....

client = TelegramClient('session_name', api_id, api_hash)

saved_messages = {}

@client.on(events.NewMessage(chats='username_or_chat_id'))  # Replace with username or chat_id , examle : @username
async def new_message_handler(event):
    message_id = event.id
    saved_messages[message_id] = event.message.text

    # Save message to text file
    with open('saved_messages.txt', 'a', encoding='utf-8') as f:
        f.write(f"{event.date}: {event.message.text} (ID: {message_id})\n")

async def check_deleted_messages():
    while True:
        await asyncio.sleep(5)  # Check every 5 seconds
        try:
            current_message_ids = {msg.id async for msg in client.iter_messages('username_or_chat_id')} # Replace with username or chat_id , examle : @username
            # Check saved messages
            for message_id in list(saved_messages.keys()):
                if message_id not in current_message_ids:
                    print(f"The message has been deleted : {saved_messages[message_id]} (ID: {message_id})")
                    del saved_messages[message_id]  # Remove message from dictionary
        except Exception as e:
            print(f"An error occurred : {e}")

async def main():
    await client.start()
    print("Start listening to messages...")
    asyncio.create_task(check_deleted_messages())
    await client.run_until_disconnected()

if __name__ == '__main__':
    asyncio.run(main())
