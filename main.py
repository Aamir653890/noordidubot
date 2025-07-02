from flask import Flask, request
from telegram import Update, Bot
from telegram.ext import CommandHandler, MessageHandler, filters, ApplicationBuilder, ContextTypes

import os

TOKEN = os.getenv("BOT_TOKEN", "7192091134:AAHXzC7xKOQ5JFHHED3iZskAtg9bjAZNjFs")
WEBHOOK_URL = os.getenv("WEBHOOK_URL", "https://aafnoor.onrender.com")

app = Flask(__name__)
bot = Bot(token=TOKEN)

application = ApplicationBuilder().token(TOKEN).build()


# Your bot commands
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello Aafiya ❤️ Didu is awake, kya haal hai?")

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(update.message.text)


# Register handlers
application.add_handler(CommandHandler("start", start))
application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))


@app.route('/')
def home():
    return 'Didu Bot is running 😌'

@app.route(f'/{TOKEN}', methods=['POST'])
async def webhook():
    if request.method == "POST":
        await application.update_queue.put(Update.de_json(request.get_json(force=True), bot))
        return 'OK'

# Set webhook when app starts
@app.before_first_request
def set_webhook():
    bot.delete_webhook()
    bot.set_webhook(url=f"{WEBHOOK_URL}/{TOKEN}")


if __name__ == '__main__':
    import asyncio
    loop = asyncio.get_event_loop()
    loop.create_task(application.initialize())
    app.run(host='0.0.0.0', port=5000)
