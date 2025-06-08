from telegram import Update
from telegram.ext import ContextTypes
import random
import json

async def handle_hustle(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    try:
        with open("hustle_tips.json", "r") as file:
            tips = json.load(file)
        tip = random.choice(tips)
        await update.message.reply_text(f"💼 *Hustle Tip:*\n_{tip}_", parse_mode="Markdown")
    except Exception:
        await update.message.reply_text("Hustle tips file nahi mila. 🛠")
