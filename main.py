from flask import Flask, request
from telegram import Bot, Update
from telegram.ext import Dispatcher, CommandHandler, MessageHandler, Filters
import os

# Your bot token
TOKEN = "7192091134:AAHXzC7xKOQ5JFHHED3iZskAtg9bjAZNjFs"
bot = Bot(token=TOKEN)

# Flask app
app = Flask(__name__)

# Dispatcher to handle updates
dispatcher = Dispatcher(bot, None, use_context=True)

# Simple start command
def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Didu is here meri jaan 💌")

# Echo handler
def echo(update, context):
    message = update.message.text
    response = f"🤍 {message}"
    context.bot.send_message(chat_id=update.effective_chat.id, text=response)

# Add handlers
dispatcher.add_handler(CommandHandler("start", start))
dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

# Webhook route
@app.route(f"/{TOKEN}", methods=["POST"])
def webhook():
    update = Update.de_json(request.get_json(force=True), bot)
    dispatcher.process_update(update)
    return "OK"

# Root check
@app.route("/")
def home():
    return "Didu is live 💖"

if __name__ == "__main__":
    PORT = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=PORT)
