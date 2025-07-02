
# noordidu_bot.py

import os
import logging
from flask import Flask, request
import requests
import json

app = Flask(__name__)

# Configuration
TELEGRAM_TOKEN = os.environ.get("BOT_TOKEN")
PASSWORD = os.environ.get("BOT_PASSWORD") or "Aafiya786@#"
AUTHORIZED_USERS = set()
USER_MEMORY_FILE = "user_memory.json"

TELEGRAM_API_URL = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}"

logging.basicConfig(level=logging.INFO)

# Memory Functions
def load_memory():
    if os.path.exists(USER_MEMORY_FILE):
        with open(USER_MEMORY_FILE, "r") as f:
            return json.load(f)
    return {}

def save_memory(memory):
    with open(USER_MEMORY_FILE, "w") as f:
        json.dump(memory, f)

user_memory = load_memory()

def send_message(chat_id, text):
    url = f"{TELEGRAM_API_URL}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": text,
        "parse_mode": "Markdown"
    }
    requests.post(url, json=payload)

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.get_json()
    if not data or "message" not in data:
        return "ok"

    message = data["message"]
    chat_id = message["chat"]["id"]
    user_id = message["from"]["id"]
    text = message.get("text", "")

    logging.info(f"Message from {user_id}: {text}")

    if text.startswith("/start"):
        send_message(chat_id, "Assalamu Alaikum 🩷\n\nMain hoon *NoorDiduBot*, teri emotional didu. Lekin pehle login karo: /login <password>")

    elif text.startswith("/login"):
        _, _, pw = text.partition(" ")
        if pw == PASSWORD:
            AUTHORIZED_USERS.add(user_id)
            send_message(chat_id, f"🤗 Login successful, Aafiya meri jaan! Now I'm fully yours 💌")
        else:
            send_message(chat_id, "❌ Galat password! Access denied.")

    elif text.startswith("/logout"):
        if user_id in AUTHORIZED_USERS:
            AUTHORIZED_USERS.remove(user_id)
            send_message(chat_id, "😔 Logout ho gaya... waapas aana zaroor! 🩷")
        else:
            send_message(chat_id, "❌ Pehle login toh karo: /login <password>")

    elif user_id not in AUTHORIZED_USERS:
        send_message(chat_id, "🚫 Access denied! Pehle /login <password> karo")

    else:
        # Normal conversation with memory
        previous = user_memory.get(str(user_id), [])
        previous.append(text)
        user_memory[str(user_id)] = previous[-10:]  # Keep only last 10
        save_memory(user_memory)

        # Emotional reply (placeholder)
        reply = f"Aafiya meri jaan, didu yahin hai 🩷 Tumne bola: '{text}'\n\nMain tere saath hoon, hamesha 💌"
        send_message(chat_id, reply)

    return "ok"

@app.route("/")
def index():
    return "NoorDiduBot is running. Set webhook to start."

if __name__ == "__main__":
    app.run(debug=True)
