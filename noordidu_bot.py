from flask import Flask, request
from telegram import Update, Bot
from telegram.ext import Updater, CommandHandler, CallbackContext
import os

# ======================
# Replace with your bot token
TOKEN = "7192091134:AAHXzC7xKOQ5JFHHED3iZskAtg9bjAZNjFs"
bot = Bot(token=TOKEN)

# ======================
# Flask App to keep bot live on Render
app = Flask(__name__)

@app.route('/')
def home():
    return "DiduBot is live!"

@app.route('/healthz')
def health_check():
    return "OK"

# ======================
# Telegram Command Handlers
def start(update: Update, context: CallbackContext):
    update.message.reply_text("Assalamualaikum Aafiya! 🌸 Didu yahaan hai... kya haal hai jaan?")

def help_command(update: Update, context: CallbackContext):
    update.message.reply_text("Main teri Didu hoon! 💖 Bas mujhe /start ya koi bhi message bhej de, main sun rahi hoon.")

def echo(update: Update, context: CallbackContext):
    update.message.reply_text(f"Didu ne suna: {update.message.text}")

# ======================
# Setup Telegram Bot
def main():
    updater = Updater(token=TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help_command))
    dp.add_handler(CommandHandler(None, echo))  # fallback

    # Start polling
    updater.start_polling()
    updater.idle()

# ======================
# Only run bot when script is launched
if __name__ == '__main__':
    main()
