# features/mood.py

from telegram import Update
from telegram.ext import ContextTypes
import json

DATA_FILE = "data/quotes.json"

def load_data():
    try:
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=2)

# /mood command handler
async def handle_mood(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "💭 How are you feeling today?\n\n"
        "Reply with a word like: happy, sad, stressed, excited, angry, etc.\n"
        "I'll remember it and respond accordingly ❤️"
    )

# Called when user replies with a mood word
async def save_mood(update: Update, context: ContextTypes.DEFAULT_TYPE, mood_text: str):
    user = update.effective_user
    data = load_data()

    if str(user.id) not in data:
        data[str(user.id)] = {"name": user.first_name, "messages": [], "mood": ""}

    data[str(user.id)]["mood"] = mood_text
    save_data(data)

    emoji_map = {
        "happy": "😄", "sad": "😢", "stressed": "😣",
        "excited": "🤩", "angry": "😡", "tired": "😴"
    }
    emoji = emoji_map.get(mood_text, "🧠")

    await update.message.reply_text(
        f"✅ Mood saved: *{mood_text}* {emoji}\n"
        f"I'm here if you need a boost, {user.first_name}!",
        parse_mode="Markdown"
        )
