# features/menu.py

from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ContextTypes

from features.analytics import
track_command

async def handle_menu(update: Update, 
context: ContextTypes.DEFAULT_TYPE):
    track_command("menu", 
update.effective_user)
    keyboard = [["/mood", "/hustle"], 
["/offer", "/stats", "/help"]]
    reply_markup = 
ReplyKeyboardMarkup(keyboard, 
resize_keyboard=True)

    await update.message.reply_text(
        "📋 *Main Menu*\n\n"
        "🔹 /mood – Track your current mood\n"
        "🔹 /hustle – Daily hustle tips 💪\n"
        "🔹 /offer – Affiliate deals 💰\n"
        "🔹 /stats – See your activity 📊\n"
        "🔹 /help – All commands 📘",
        parse_mode="Markdown",
        reply_markup=reply_markup
    )
