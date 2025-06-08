from telegram import Update
from telegram.ext import ContextTypes
import random
import json

async def handle_offers(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    try:
        with open("offers.json", "r") as file:
            offers = json.load(file)
        offer = random.choice(offers)
        await update.message.reply_text(f"💸 *Deal of the Day:*\n_{offer}_", parse_mode="Markdown")
    except Exception:
        await update.message.reply_text("Offers file nahi mila. 🛍")
