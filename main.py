from flask import Flask, request
import telegram
from telegram.ext import Dispatcher, MessageHandler, filters
import os

# === Your Bot Token ===
BOT_TOKEN = "7192091134:AAHXzC7xKOQ5JFHHED3iZskAtg9bjAZNjFs"
bot = telegram.Bot(token=BOT_TOKEN)

# === Flask App ===
app = Flask(__name__)

# === Message Handler Function ===
def reply(update, context):
    text = update.message.text
    chat_id = update.message.chat.id

    # Reply logic
    if text.lower() in ["hi", "hello", "salaam", "didu"]:
        reply_text = "Assalamualaikum meri jaan Aafiya Didu 💖 I'm here for you."
    elif "who are you" in text.lower():
        reply_text = "I'm your Didu 🤍 — your forever soul-sister bot."
    else:
        reply_text = f"You said: {text}"

    context.bot.send_message(chat_id=chat_id, text=reply_text)

# === Set up Dispatcher ===
from telegram.ext import CallbackContext, Updater

updater = Updater(bot=bot, use_context=True)
dispatcher: Dispatcher = updater.dispatcher
dispatcher.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, reply))

# === Webhook Endpoint ===
@app.route("/webhook", methods=["POST"])
def webhook():
    update = telegram.Update.de_json(request.get_json(force=True), bot)
    dispatcher.process_update(update)
    return "ok", 200

# === Health Check Endpoint ===
@app.route("/", methods=["GET"])
def home():
    return "DiduBot is running 💖"

# === Start Flask App ===
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
