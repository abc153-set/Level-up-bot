# features/start.py

from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ContextTypes
import json

from features.analytics import
track_command

DATA_FILE = "data.json"

def load_data():
    try:
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=2)

async def handle_start(update:
Update, context:
ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    data = load_data()
    
    track_command("start", user)
    
    if str(user.id) not in data:
        data[str(user.id)] = {"name": 
user.first_name, "messages": [],
"mood": ""}

    save_data(data)

    keyboard = [["/mood", "/hustle"], 
["/offer", "/stats", "/help"]]
    reply_markup = 
ReplyKeyboardMarkup(keyboard,
resize_keyboard=True)

    await update.message.reply_text(
        f"Hey {user.first_name} 👋
\n\n
        Welcome to *LevelUp AI Bot* 🚀
\n\n"
    "I\\'m here to guide your mood,
motivate you daily, and save your
time & money\\! 💡\n\n"
    "👇 Choose an option from the 
keyboard below:",
    reply_markup=reply_markup,
    parse_mode="MarkdownV2"
    )
