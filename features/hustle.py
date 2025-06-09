# features/hustle.py

from telegram import Update
from telegram.ext import ContextTypes
import json
import random
import os

TIPS_FILE = "hustle_tips.json"

# Load tips from JSON file (fallback if not found)
def load_tips():
    if os.path.exists(TIPS_FILE):
        try:
            with open(TIPS_FILE, "r") as f:
                tips = json.load(f)
                if isinstance(tips, list) and tips:
                    return tips
        except json.JSONDecodeError:
            pass

    # Fallback hardcoded tips if file not found or invalid
    return [
        "💼 Stay focused: One task at a time.",
        "🧘‍♂️ Take deep breaths. Recharge.",
        "📚 Learn one new thing daily.",
        "📈 Track your progress weekly.",
        "⏳ Timebox your hustle sessions.",
        "💡 Think long-term. Build consistency.",
        "📵 Avoid distractions. Silent mode on!"
    ]

# /hustle command handler
async def handle_hustle(update: Update, context: ContextTypes.DEFAULT_TYPE):
    tips = load_tips()
    tip = random.choice(tips)

    await update.message.reply_text(f"🔥 *Hustle Tip of the Day:*\n{tip}", parse_mode="Markdown")
