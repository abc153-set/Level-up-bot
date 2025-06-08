from telegram import Update
from telegram.ext import ContextTypes

async def handle_mood(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "I'm here for you 💖\nTell me how you're feeling today, and I'll respond like your closest friend."
    )
