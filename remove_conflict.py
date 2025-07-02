from telegram import Bot

TOKEN = "7192091134:AAHXzC7xKOQ5JFHHED3iZskAtg9bjAZNjFs"
WEBHOOK_URL = "https://aafnoor.onrender.com/" + TOKEN

bot = Bot(token=TOKEN)

# Clear old webhook
bot.delete_webhook()

# Set new webhook
bot.set_webhook(url=WEBHOOK_URL)

print("✅ Webhook set successfully with legacy-compatible version.")
