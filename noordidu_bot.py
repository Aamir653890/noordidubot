from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
from flask import Flask
from apscheduler.schedulers.background import BackgroundScheduler

# Flask app for Render to ping
app = Flask(__name__)

@app.route('/')
def index():
    return "Didu is running!"

# Your bot token (Use environment variable in production)
import os
TOKEN = "7192091134:AAHXzC7xKOQ5JFHHED3iZskAtg9bjAZNjFs"

def start(update: Update, context: CallbackContext):
    update.message.reply_text("Hi Aafiya! 💙 Didu is here 24×7 😄")

def echo(update: Update, context: CallbackContext):
    update.message.reply_text(update.message.text)

def unknown_command(update: Update, context: CallbackContext):
    update.message.reply_text("Sorry Aafiya, Didu didn’t understand that command 😅")

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    # Handlers
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))
    dp.add_handler(MessageHandler(Filters.command, unknown_command))  # Fallback

    updater.start_polling()
    updater.idle()

# Scheduler to keep bot alive
def keep_alive():
    print("Keeping Didu alive 🩵")

if __name__ == '__main__':
    scheduler = BackgroundScheduler()
    scheduler.add_job(keep_alive, 'interval', minutes=25)
    scheduler.start()

    # Start both Flask and Bot
    import threading
    threading.Thread(target=lambda: app.run(host='0.0.0.0', port=5000)).start()
    main()