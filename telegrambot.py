import telepot
import time

def handle_chat_message(msg):
    """Handle incoming chat messages and update the word list."""
    content_type, chat_type, chat_id = telepot.glance(msg)

    if content_type == 'text':
        received_text = msg['text']
        bot.sendMessage(chat_id, f'Ok, scrivo "{received_text}" con le luci.')

        with open("wordslist.txt", "w") as out_file:
            out_file.write(received_text)

def main():
    """Set up the bot and start listening for messages."""
    bot = telepot.Bot('<YOUR_BOT_API_KEY>')
    bot.message_loop(handle_chat_message)

    print('Bot is listening for messages...')

    try:
        while True:
            time.sleep(10)
    except KeyboardInterrupt:
        print("Bot stopped.")

if __name__ == "__main__":
    main()
