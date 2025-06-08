from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ContextTypes

async def handle_menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [["💬 Mood", "⚡ Hustle Tip"], ["🎁 Offers", "📚 Quote"]]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

    await update.message.reply_text(
        "Here's your power menu! 🔥\nPick one and let's level up your day 👇",
        reply_markup=reply_markup,
    )
