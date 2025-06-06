import json
import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Load data from JSON
def load_data():
    if os.path.exists("data.json"):
        with open("data.json", "r") as f:
            return json.load(f)
    return {}

# Save data to JSON
def save_data(data):
    with open("data.json", "w") as f:
        json.dump(data, f, indent=2)

# /start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = str(update.effective_user.id)
    data = load_data()
    
    if user_id not in data:
        data[user_id] = {"name": update.effective_user.first_name, "mood": None, "goals": []}
        save_data(data)

    await update.message.reply_text(f"Welcome {update.effective_user.first_name}! 👋\nI'm your LevelUp Bot — here to help you hustle, track your mood, and learn daily!")

# /mood command
async def mood(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = str(update.effective_user.id)
    data = load_data()

    if user_id not in data:
        await update.message.reply_text("Please use /start first.")
        return

    if context.args:
        mood_value = " ".join(context.args)
        data[user_id]["mood"] = mood_value
        save_data(data)
        await update.message.reply_text(f"Mood updated to: {mood_value} 😌")
    else:
        await update.message.reply_text("Please share your mood like this:\n`/mood happy` or `/mood stressed`")

# /goal command
async def goal(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = str(update.effective_user.id)
    data = load_data()

    if user_id not in data:
        await update.message.reply_text("Please use /start first.")
        return

    if context.args:
        goal_text = " ".join(context.args)
        data[user_id]["goals"].append(goal_text)
        save_data(data)
        await update.message.reply_text(f"🎯 Goal added: {goal_text}")
    else:
        await update.message.reply_text("Add a goal like this:\n`/goal Read 5 pages daily`")

# /status command
async def status(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = str(update.effective_user.id)
    data = load_data()

    if user_id not in data:
        await update.message.reply_text("Please use /start first.")
        return

    mood = data[user_id].get("mood", "Not set")
    goals = data[user_id].get("goals", [])
    goal_text = "\n- ".join(goals) if goals else "No goals set."

    message = f"🧠 *Your Status:*\nMood: {mood}\nGoals:\n- {goal_text}"
    await update.message.reply_text(message, parse_mode="Markdown")

# Main function
def main():
    TOKEN = "8125526527:AAE-POihDYVVeiKWLmmGYvtibOk9-dl6g2M"  # 🔴 Replace this with your bot's token
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("mood", mood))
    app.add_handler(CommandHandler("goal", goal))
    app.add_handler(CommandHandler("status", status))

    print("✅ Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
