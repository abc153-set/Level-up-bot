import random
from telegram import Update
from telegram.ext import ContextTypes

# You can load from JSON in future too
hustle_tips = [
    "Stay focused. Results take time. 📈",
    "Don't stop until you're proud. 💪",
    "Work in silence, let success make the noise. 🔥",
]

async def handle_hustle(update: Update, context: ContextTypes.DEFAULT_TYPE):
    tip = random.choice(hustle_tips)
    await update.message.reply_text(f"⚡ Hustle Tip:\n{tip}")
