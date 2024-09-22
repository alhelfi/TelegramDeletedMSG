
# Telegram Deleted Messages Tracker

This Python script uses the Telethon library to track deleted messages in a Telegram chat. It saves new messages and checks periodically for any deletions.

## Requirements

- Python 3.7 or higher
- Telethon library

You can install Telethon using pip:

```bash
pip install telethon
```

# Setup

1.  **Create a Telegram Application**:
    
    -   Go to [Telegram's API development tools](https://my.telegram.org/auth?to=apps).
    -   Create a new application to get your API ID and API Hash.
2.  **Update the Script**:
    
    -   Replace the placeholders in the code below with your actual API ID, API Hash, and phone number.

## Usage 

1. Run the script in your terminal:
```bash
python main.py
```
2. The script will start listening to messages in the specified Telegram chat. Any new messages will be saved to `saved_messages.txt`, and you will be notified if any messages are deleted.
## Note

-   Make sure your phone number is in international format (e.g., +1234567890).
-   Replace `username_or_chat_id` with the actual username (e.g., `@username`) or chat ID where you want to track messages.
- To get the deleted messages permanently, you must keep the program running at all times. You can do this by running it on a server.
