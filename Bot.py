import json
import random
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters

DATA_FILE = "data.json"

# Utility functions
def load_data():
    try:
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=2)

# Features
hustle_tips = [
    "💡 Tip: Wake up early and plan your top 3 goals.",
    "🚀 Tip: Consistency beats motivation.",
    "📈 Tip: Read for 30 mins a day to outgrow others.",
    "💰 Tip: Track your expenses and invest the rest.",
]

affiliate_offers = [
    "🎁 Try Audible FREE for 30 days: https://amzn.to/yourlink",
    "🔥 Best budget mic for creators: https://amzn.to/yourlink2",
    "📚 Read 'Atomic Habits' – Must-have: https://amzn.to/yourlink3",
]

# Commands
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    data = load_data()
    if str(user.id) not in data:
        data[str(user.id)] = {"name": user.first_name, "mood": "", "messages": []}
        save_data(data)
    keyboard = [["💪 Hustle Tip", "😊 Mood"], ["🎁 Offer", "❓ Help"]]
    await update.message.reply_text(
        f"Hi {user.first_name}, welcome to LevelUp AI Bot!\nChoose an option below:",
        reply_markup=ReplyKeyboardMarkup(keyboard, resize_keyboard=True),
    )

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Use the buttons or type /start to begin again.")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    text = update.message.text.strip().lower()
    data = load_data()
    uid = str(user.id)

    if uid not in data:
        data[uid] = {"name": user.first_name, "mood": "", "messages": []}

    if text == "💪 hustle tip":
        tip = random.choice(hustle_tips)
        await update.message.reply_text(tip)
    elif text == "🎁 offer":
        offer = random.choice(affiliate_offers)
        await update.message.reply_text(offer)
    elif text == "😊 mood":
        await update.message.reply_text("How are you feeling today? (e.g., happy, tired, focused)")
        context.user_data["expecting_mood"] = True
    elif context.user_data.get("expecting_mood"):
        data[uid]["mood"] = text
        save_data(data)
        context.user_data["expecting_mood"] = False
        await update.message.reply_text(f"Thanks! Saved your mood: {text}")
    else:
        data[uid]["messages"].append(text)
        save_data(data)
        await update.message.reply_text("✅ Got your message!")

def main():
    app = ApplicationBuilder().token("8125526527:AAE-POihDYVVeiKWLmmGYvtibOk9-dl6g2M").build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    print("🤖 Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
