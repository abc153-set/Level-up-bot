import json
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters

DATA_FILE = "data.json"

def load_data():
    try:
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=2)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    await update.message.reply_text(f"Hi {user.first_name}, welcome to LevelUp AI Bot!")
    data = load_data()
    data[str(user.id)] = {"name": user.first_name, "messages": []}
    save_data(data)

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Send any text and I'll store it. Use this bot daily to improve your mindset, get hustle tips, mood tracking and more!")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    text = update.message.text
    data = load_data()
    if str(user.id) not in data:
        data[str(user.id)] = {"name": user.first_name, "messages": []}
    if "messages" not in data[str(user.id)]:
        data[str(user.id)]["messages"] = []
    data[str(user.id)]["messages"].append(text)
    save_data(data)
    
    # Engagement and affiliate replies
    if "tip" in text.lower():
        await update.message.reply_text("💡 Hustle Tip: Wake up at 5am and plan your day!")
    elif "mood" in text.lower():
        await update.message.reply_text("🧠 Mood Tracker: How are you feeling today? 😊 / 😐 / 😞")
    elif "earn" in text.lower() or "money" in text.lower():
        await update.message.reply_text("💰 Learn to earn online: Check out this amazing tool 👉 https://amzn.to/your-affiliate-link")
    else:
        await update.message.reply_text("✅ Got it! Your message is saved.")

def main():
    app = ApplicationBuilder().token("8125526527:AAE-POihDYVVeiKWLmmGYvtibOk9-dl6g2M").build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    print("Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
