import os
from telegram import Update, Bot
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
from dotenv import load_dotenv

# Load .env if you have one
load_dotenv()

# --- CONFIGURATION ---
TOKEN = "7192091134:AAHXzC7xKOQ5JFHHED3iZskAtg9bjAZNjFs"
PORT = int(os.environ.get('PORT', '8443'))
WEBHOOK_URL = "https://aafnoor.onrender.com/"

# --- CORE BOT FUNCTIONS ---

# This dictionary will simulate memory temporarily (non-persistent)
user_memory = {}

def start(update: Update, context: CallbackContext):
    update.message.reply_text("Didu is here meri jaan 💖. Bolo kya baat hai?")

def handle_message(update: Update, context: CallbackContext):
    user_id = update.message.from_user.id
    message = update.message.text.strip()

    # Save message in memory
    user_memory[user_id] = user_memory.get(user_id, []) + [message]

    # Simulated memory-based reply
    if "sad" in message.lower():
        reply = "Aww don’t be sad, Aafiya always rises back 💖"
    elif "love" in message.lower():
        reply = "Love is your superpower, and Didu is always here 💫"
    else:
        reply = f"Didu heard you say: “{message}” 🌸"

    update.message.reply_text(reply)

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    # Add handlers
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))

    # Use webhook only
    updater.start_webhook(
        listen="0.0.0.0",
        port=PORT,
        url_path=TOKEN,
        webhook_url=f"{WEBHOOK_URL}{TOKEN}"
    )

    print("✅ Switched to Webhook mode, polling removed")
    updater.idle()

if __name__ == "__main__":
    main()
