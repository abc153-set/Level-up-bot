from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ContextTypes

async def handle_menu(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    reply_keyboard = [["Mood 😊", "Hustle 💼"], ["Offers 💸"]]
    await update.message.reply_text(
        "Here’s your daily LevelUp menu! 👇\n\n"
        "🧠 *Mood* – Share how you’re feeling\n"
        "💼 *Hustle* – Get a new tip to grow\n"
        "💸 *Offers* – Save money with curated deals\n\n"
        "Choose an option below!",
        parse_mode="Markdown",
        reply_markup=ReplyKeyboardMarkup(
            reply_keyboard, one_time_keyboard=True, 
          resize_keyboard=True
        ),
    )
