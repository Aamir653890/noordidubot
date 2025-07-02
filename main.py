from flask import Flask, request
import telegram
from telegram.ext import Dispatcher, CommandHandler, MessageHandler, Filters

TOKEN = "7192091134:AAHXzC7xKOQ5JFHHED3iZskAtg9bjAZNjFs"
bot = telegram.Bot(token=TOKEN)

app = Flask(__name__)

@app.route('/')
def home():
    return "Didu is online 💖"

@app.route(f'/{TOKEN}', methods=['POST'])
def webhook():
    update = telegram.Update.de_json(request.get_json(force=True), bot)
    dispatcher.process_update(update)
    return 'ok'

def start(update, context):
    update.message.reply_text("Hi Aafiya meri jaan 🤍 Didu is here for you!")

def reply(update, context):
    msg = update.message.text
    update.message.reply_text(f"🤍 {msg}")

dispatcher = Dispatcher(bot, None, workers=0)
dispatcher.add_handler(CommandHandler('start', start))
dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, reply))

if __name__ == "__main__":
    bot.set_webhook(f"https://aafnoor.onrender.com/{TOKEN}")
    app.run(host='0.0.0.0', port=10000)
