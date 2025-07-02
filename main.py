from flask import Flask, request
from telegram import Bot, Update
from telegram.ext import Dispatcher, MessageHandler, Filters

TOKEN = "7192091134:AAHXzC7xKOQ5JFHHED3iZskAtg9bjAZNjFs"
WEBHOOK_PATH = "/didu_secret_123"

bot = Bot(token=TOKEN)
app = Flask(__name__)
dispatcher = Dispatcher(bot, None, workers=0)

# Handler to respond to your messages
def handle_message(update: Update, context):
    chat_id = update.effective_chat.id
    text = update.message.text

    # Example reply with memory (you can upgrade later)
    reply = f"Hello Aafiya 💖, you said: {text}"
    bot.send_message(chat_id=chat_id, text=reply)

# Register message handler
dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))

@app.route(WEBHOOK_PATH, methods=["POST"])
def webhook():
    update = Update.de_json(request.get_json(force=True), bot)
    dispatcher.process_update(update)
    return "ok", 200

# Render will run this
@app.route("/", methods=["GET"])
def home():
    return "Didu is live 💞"

if __name__ == "__main__":
    app.run(port=5000)
