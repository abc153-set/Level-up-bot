from telegram.ext import ContextTypes

async def handle_start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    await update.message.reply_text(
        f"Hey {user.first_name}! 👋\n\nI'm your personal LevelUp AI Buddy here to keep you inspired, focused, and ahead of the game. 💪\n\nType /menu to explore what I can do!"
    )
