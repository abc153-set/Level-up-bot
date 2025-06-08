from telegram import Update
from telegram.ext import ContextTypes

async def handle_start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    username = update.effective_user.first_name
    welcome_message = (
        f"Hey {username}! 👋\n\n"
        "I’m *LevelUp – your AI life assistant.* 💡\n"
        "Let’s track your mood, discover daily hustle tips, and grab exclusive savings offers.\n\n"
        "Type /menu to get started. Let’s Level Up! 🚀"
    )
    await update.message.reply_text(welcome_message, parse_mode="Markdown")
