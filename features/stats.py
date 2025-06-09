# features/stats.py

from telegram import Update
from telegram.ext import ContextTypes
import json

DATA_FILE = "data.json"

# Load user data
def load_data():
    try:
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

# /stats command handler
async def handle_stats(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    user_id = str(user.id)

    data = load_data()

    if user_id in data:
        name = data[user_id].get("name", "User")
        mood = data[user_id].get("mood", "Not set")
        messages = data[user_id].get("messages", [])
        message_count = len(messages)

        await update.message.reply_text(
            f"📊 *Your Stats*\n\n"
            f"👤 Name: {name}\n"
            f"💬 Messages Sent: {message_count}\n"
            f"🧠 Mood: {mood}",
            parse_mode="Markdown"
        )
    else:
        await update.message.reply_text(
            "🤔 No data found. Please use /start to begin tracking your activity!"
      )
