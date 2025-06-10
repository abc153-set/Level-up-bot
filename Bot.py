from dotenv import load_dotenv
import os
import json
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup 
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

from features.start import handle_start 
from features.menu import handle_menu 
from features.mood import handle_mood, save_mood 
from features.hustle import handle_hustle 
from features.offers import handle_offers 
from features.stats import handle_stats
from analytics import get_top_users, get_common_moods

# ✅ Load token securely from .env file
load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")

# 🚨 Raise error if token not found
if not TOKEN:
    raise ValueError("❌ BOT_TOKEN 
not found in .env file!")

DATA_FILE = "data.json"

# Load user data from JSON
def load_data(): 
    try: 
        with open(DATA_FILE, "r") as f: 
            return json.load(f) 
    except FileNotFoundError: 
        return {}

# Save user data to JSON
def save_data(data): 
    with open(DATA_FILE, "w") as f: 
        json.dump(data, f, indent=2)

# Catch all user messages
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE): 
    user = update.effective_user 
    text = update.message.text.lower() 
    data = load_data()

    if str(user.id) not in data:
        data[str(user.id)] = {"name": user.first_name, "messages": [], "mood": ""}

    if text in ["happy", "sad", "stressed", "excited", "angry"]:
        await save_mood(update, context, text)
    else:
        data[str(user.id)]["messages"].append(text)
        await update.message.reply_text("💾 Got it! Saved your message.")
        save_data(data)
ADMIN_IDS = [1234567890]  # 👈 Yaha apna 10-digit Telegram user ID likho

async def analytics_handler(update:
Update, context: 
ContextTypes.DEFAULT_TYPE):
    user_id = 
update.effective_user.id
    if user_id not in ADMIN_IDS:
        await 
update.message.reply_text("⛔ You are 
not authorized to view analytics.")
        return

    top_users = get_top_users()
    mood_stats = get_common_moods()

    msg = "📊 *Bot Analytics*\n\n"
    msg += "🏆 *Top Users:*\n"
    for name, count in top_users:
        msg += f"• {name}: {count} 
msgs\n"

    msg += "\n😀 *Most Common 
Moods:*\n"
    for mood, count in mood_stats:
        msg += f"• {mood}: {count}\n"

    await 
update.message.reply_text(msg, 
parse_mode="Markdown")
    
# Main bot setup
def main(): 
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", handle_start))
    app.add_handler(CommandHandler("menu", handle_menu))
    app.add_handler(CommandHandler("mood", handle_mood))
    app.add_handler(CommandHandler("hustle", handle_hustle))
    app.add_handler(CommandHandler("offer", handle_offers))
    app.add_handler(CommandHandler("stats", handle_stats))
    app.add_handler(CommandHandler("analytics", analytics_handler))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("✅ Bot is running...")
    app.run_polling()

if __name__ == "main": 
    main()

