from features.start import handle_start
from features.menu import handle_menu
from features.mood import handle_mood
from features.hustle import handle_hustle
from features.offers import handle_offers

import json
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

TOKEN = "8125526527:AAE-POihDYVVeiKWLmmGYvtibOk9-dl6g2M"
DATA_FILE = "data.json"

# Load & Save JSON
def load_data():
    try:
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=2)

# Start Command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    data = load_data()
    data[str(user.id)] = {
        "name": user.first_name,
        "messages": [],
        "mood": "",
    }
    save_data(data)

    keyboard = [["/mood", "/hustle"], ["/offer", "/help"]]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

    await update.message.reply_text(
        f"Hi {user.first_name} 👋, welcome to LevelUp AI Bot!\n\nI can help you track your mood, give daily hustle tips, and even offer money-saving affiliate deals 💸.",
        reply_markup=reply_markup,
    )

# Help Command
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🧠 Commands:\n/start – Welcome\n/mood – Track your mood\n/hustle – Daily motivation\n/offer – Best deals\n/help – Show this menu")

# Mood Command
async def mood(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("How are you feeling today? (happy/sad/stressed/etc.)")

# Hustle Tips
async def hustle(update: Update, context: ContextTypes.DEFAULT_TYPE):
    tips = [
        "🔥 Wake up early and plan your goals.",
        "💡 Read 10 pages of a great book daily.",
        "⏱️ Block distractions – Focus 100% for 30 mins.",
        "📈 Track your growth every night.",
        "💰 Save before you spend.",
    ]
    from random import choice
    await update.message.reply_text("💪 Hustle Tip:\n" + choice(tips))

# Offers / Affiliate Deals
async def offer(update: Update, context: ContextTypes.DEFAULT_TYPE):
    offers = [
        "🛒 *Amazon Offer*: Get 10% cashback on electronics 👉 [Grab Deal](https://amzn.to/xyz)",
        "📚 *Udemy Sale*: Courses at ₹449 only 👉 [Enroll Now](https://www.udemy.com/)",
        "💼 *Internshala*: Learn & earn internships 👉 [Apply Here](https://internshala.com/)",
    ]
    from random import choice
    await update.message.reply_markdown_v2(choice(offers))

# Save User Messages
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    text = update.message.text.lower()
    data = load_data()

    if str(user.id) not in data:
        data[str(user.id)] = {"name": user.first_name, "messages": [], "mood": ""}

    if text in ["happy", "sad", "stressed", "excited", "angry"]:
        data[str(user.id)]["mood"] = text
        reply = f"✅ Mood '{text}' saved! Take care, {user.first_name}."
    else:
        data[str(user.id)]["messages"].append(text)
        reply = "💾 Got it! Saved your message."

    save_data(data)
    await update.message.reply_text(reply)

# Main Function
def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("mood", mood))
    app.add_handler(CommandHandler("hustle", hustle))
    app.add_handler(CommandHandler("offer", offer))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("✅ Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
