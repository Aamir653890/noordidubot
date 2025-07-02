import os
from telegram import Update, Bot
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# --- CONFIGURATION ---
TOKEN = "7192091134:AAHXzC7xKOQ5JFHHED3iZskAtg9bjAZNjFs"
PORT = int(os.environ.get('PORT', '8443'))
WEBHOOK_URL = "https://aafnoor.onrender.com/"

# --- MEMORY SIMULATION ---
user_memory = {}

def start(update: Update, context: CallbackContext):
    update.message.reply_text("Didu is here meri jaan 💖. Bolo kya baat hai?")

def handle_message(update: Update, context: CallbackContext):
    user_id = update.message.from_user.id
    message = update.message.text.strip()

    # Memory logic
    user_memory[user_id] = user_memory.get(user_id, []) + [message]

    # Smart emotional response
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

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))

    # Webhook Mode
    updater.start_webhook(
        listen="0.0.0.0",
        port=PORT,
        url_path=TOKEN,
        webhook_url=f"{WEBHOOK_URL}{TOKEN}"
    )

    print("✅ Webhook running, polling removed.")
    updater.idle()

if __name__ == "__main__":
    main()
