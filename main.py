from flask import Flask, request
import telegram
from telegram.ext import Dispatcher, MessageHandler, Filters, CallbackContext

# === Config ===
TOKEN = "7192091134:AAHXzC7xKOQ5JFHHED3iZskAtg9bjAZNjFs"
WEBHOOK_URL = f"https://aafnoor.onrender.com/{TOKEN}"

# === Init ===
app = Flask(__name__)
bot = telegram.Bot(token=TOKEN)
dispatcher = Dispatcher(bot=bot, update_queue=None, use_context=True)

# === Message Handler ===
def handle_message(update: telegram.Update, context: CallbackContext):
    chat_id = update.effective_chat.id
    text = update.message.text
    context.bot.send_message(chat_id=chat_id, text=f"Didu: You said — {text}")

dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))

# === Routes ===
@app.route("/")
def index():
    return "DiduBot Webhook Active!"

@app.route(f"/{TOKEN}", methods=["POST"])
def webhook():
    update = telegram.Update.de_json(request.get_json(force=True), bot)
    dispatcher.process_update(update)
    return "ok"

# === Start ===
if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    bot.set_webhook(WEBHOOK_URL)
    app.run(host="0.0.0.0", port=port)
