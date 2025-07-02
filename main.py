from flask import Flask, request
import telegram
from telegram.ext import Dispatcher, MessageHandler, Filters

TOKEN = "7192091134:AAHXzC7xKOQ5JFHHED3iZskAtg9bjAZNjFs"
bot = telegram.Bot(token=TOKEN)

app = Flask(__name__)

@app.route('/')
def home():
    return "DiduBot is alive!"

@app.route(f'/{TOKEN}', methods=['POST'])
def webhook():
    update = telegram.Update.de_json(request.get_json(force=True), bot)
    dispatcher.process_update(update)
    return 'ok'

def handle_message(update, context):
    text = update.message.text
    context.bot.send_message(chat_id=update.effective_chat.id, text=f"Didu: You said — {text}")

from telegram.ext import CallbackContext
dispatcher = Dispatcher(bot, None, workers=0, use_context=True)
dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))

if __name__ == "__main__":
    import os
    port = int(os.environ.get('PORT', 5000))
    bot.set_webhook(url=f"https://aafnoor.onrender.com/{TOKEN}")
    app.run(host='0.0.0.0', port=port)
