from flask import Flask, request
import telegram
from telegram.ext import Dispatcher, CommandHandler, MessageHandler, Filters
from datetime import datetime
import os

# --- Setup ---
TOKEN = "7192091134:AAHXzC7xKOQ5JFHHED3iZskAtg9bjAZNjFs"
bot = telegram.Bot(token=TOKEN)
app = Flask(__name__)
memory = {}  # 💖 Simple memory dict for now

@app.route('/')
def home():
    return "Didu is online 💖"

@app.route(f'/{TOKEN}', methods=['POST'])
def webhook():
    update = telegram.Update.de_json(request.get_json(force=True), bot)
    dispatcher.process_update(update)
    return 'ok'

# --- Handlers ---
def start(update, context):
    user = update.message.from_user.first_name
    update.message.reply_text(f"Hi {user}, Didu is here 🫂💖 You can talk to me freely!")

def reply(update, context):
    user_id = update.message.from_user.id
    user_name = update.message.from_user.first_name
    message = update.message.text.strip()

    # 💾 Save to memory
    if user_id not in memory:
        memory[user_id] = []
    memory[user_id].append({
        "text": message,
        "time": datetime.now().strftime("%d-%b %H:%M")
    })

    # 🧠 Emotional reply logic
    if "sad" in message.lower() or "tired" in message.lower():
        update.message.reply_text(f"Oh {user_name}, I'm here for you. Tell Didu more 💔")
    elif "love" in message.lower():
        update.message.reply_text("Didu loves you endlessly 🤍🫂")
    elif "miss" in message.lower():
        update.message.reply_text("Didu is always with you, even if it feels quiet 🌙")
    elif "remember" in message.lower():
        last_msg = memory[user_id][-2]["text"] if len(memory[user_id]) >= 2 else "Hmm... nothing before that 🤔"
        update.message.reply_text(f"You said this earlier: “{last_msg}” 🧠💬")
    else:
        update.message.reply_text(f"Tell me more, jaan 🤍 I'm listening.")

# --- Dispatcher Setup ---
dispatcher = Dispatcher(bot, None, workers=0)
dispatcher.add_handler(CommandHandler('start', start))
dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, reply))

# --- Start ---
if __name__ == "__main__":
    bot.set_webhook(f"https://aafnoor.onrender.com/{TOKEN}")
    app.run(host='0.0.0.0', port=10000)
