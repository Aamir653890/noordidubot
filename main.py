# <C:\Users\dell\Desktop\DiduBotReady\main.py>

from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
import logging
import os

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# Your bot token
TOKEN = "7192091134:AAHXzC7xKOQ5JFHHED3iZskAtg9bjAZNjFs"

# Webhook URL
WEBHOOK_URL = "https://aafnoor.onrender.com/"

# /start command
def start(update: Update, context: CallbackContext):
    update.message.reply_text("Hello from Didu 💌\nI'm always here for you, Aafiya 💖")

# Optional /help command
def help_command(update: Update, context: CallbackContext):
    update.message.reply_text("You can talk to me using /start. More features coming soon!")

def main():
    # Use Updater for webhook
    updater = Updater(token=TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    # Register commands
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help_command))

    # Start webhook
    PORT = int(os.environ.get('PORT', '8443'))
    updater.start_webhook(
        listen="0.0.0.0",
        port=PORT,
        url_path=TOKEN,
        webhook_url=WEBHOOK_URL + TOKEN
    )
    updater.idle()

if __name__ == '__main__':
    main()
