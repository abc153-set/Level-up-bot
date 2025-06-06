import json
import logging
import pytz
from datetime import datetime
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext, CallbackQueryHandler
import firebase_admin_lite as firebase_admin
from firebase_admin import credentials, firestore

# Initialize Firebase
cred = credentials.Certificate("firebase_config.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

# Set timezone
tz = pytz.timezone('Asia/Kolkata')

# Start command
async def start(update: Update, context: CallbackContext.DEFAULT_TYPE) -> None:
    user = update.effective_user
    user_data = {
        'username': user.username,
        'first_name': user.first_name,
        'last_active': datetime.now(tz).isoformat()
    }
    db.collection('users').document(str(user.id)).set(user_data, merge=True)

    keyboard = [
        [InlineKeyboardButton("💡 Hustle Tip", callback_data='tip')],
        [InlineKeyboardButton("📊 Mood Tracker", callback_data='mood')],
        [InlineKeyboardButton("📚 Micro-Learn", callback_data='learn')],
        [InlineKeyboardButton("💰 Daily Savings", callback_data='savings')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(
        f"👋 Hello {user.first_name}! I'm your LevelUp AI Assistant. Choose an option below:",
        reply_markup=reply_markup
    )

# Callback handler
async def button(update: Update, context: CallbackContext.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()
    user_id = str(query.from_user.id)

    if query.data == 'tip':
        await query.edit_message_text("💡 Hustle Tip: Stay consistent. Success follows discipline.")
    elif query.data == 'mood':
        moods = [
            [InlineKeyboardButton("😊", callback_data='mood_happy')],
            [InlineKeyboardButton("😐", callback_data='mood_neutral')],
            [InlineKeyboardButton("😔", callback_data='mood_sad')]
        ]
        await query.edit_message_text("How are you feeling today?", reply_markup=InlineKeyboardMarkup(moods))
    elif query.data.startswith('mood_'):
        mood = query.data.split('_')[1]
        db.collection('moods').add({
            'user_id': user_id,
            'mood': mood,
            'timestamp': datetime.now(tz).isoformat()
        })
        await query.edit_message_text(f"Mood '{mood}' saved. ✅")
    elif query.data == 'learn':
        await query.edit_message_text("📚 Micro-Learn: Did you know? Consistency beats motivation every time.")
    elif query.data == 'savings':
        await query.edit_message_text("💰 Savings Tip: Skip one chai today and save ₹10. Small steps matter.")

# Unknown text handler
async def handle_message(update: Update, context: CallbackContext.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Please use the buttons to interact with me.")

# Main function
def main():
    TOKEN = "8125526527:AAEd2PVmfb1CATBCxKHzgXec6DXNI5ZqB1o"  # replace this with your actual token
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
