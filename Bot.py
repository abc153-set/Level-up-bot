import json
import firebase_admin
from firebase_admin import credentials, firestore

with open('firebase_config.json') as f:
    firebase_config = json.load(f)

cred = credentials.Certificate(firebase_config)
firebase_admin.initialize_app(cred)
db = firestore.client()
import telebot
import json
import firebase_admin
from firebase_admin import credentials, firestore

# Load Firebase config
cred = credentials.Certificate("firebase_config.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

# Your Telegram Bot Token
BOT_TOKEN = "YOUR_BOT_TOKEN_HERE"
bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Welcome to LevelUp AI Bot! Type /help to see what I can do.")

@bot.message_handler(commands=['help'])
def help_command(message):
    bot.send_message(message.chat.id, "/start - Welcome message\n/help - List commands\n/tip - Get today's hustle tip")

@bot.message_handler(commands=['tip'])
def send_tip(message):
    tip_ref = db.collection("tips").document("today")
    tip_doc = tip_ref.get()
    if tip_doc.exists:
        tip = tip_doc.to_dict().get("text", "No tip found.")
        bot.send_message(message.chat.id, f"Today's Hustle Tip:\n{tip}")
    else:
        bot.send_message(message.chat.id, "No tip found today!")
@bot.message_handler(commands=['save'])
def save_message(message):
    try:
        user_id = str(message.from_user.id)
        text = message.text.replace('/save', '').strip()

        if not text:
            bot.reply_to(message, "Please provide a message to save after /save command.")
            return

        db.collection("saved_messages").add({
            "user_id": user_id,
            "message": text
        })

        bot.reply_to(message, "Your message has been saved!")
    except Exception as e:
    bot.reply_to(message, f"Error saving message: {str(e)}")
@bot.message_handler(commands=['get'])
def get_saved_messages(message):
    try:
        user_id = str(message.from_user.id)
        docs = db.collection("saved_messages").where("user_id", "==", user_id).stream()

        messages = [doc.to_dict().get("message", "") for doc in docs]

        if messages:
            response = "\n\n".join(messages)
        else:
            response = "No saved messages found."

        bot.send_message(message.chat.id, response)
    except Exception as e:
        bot.send_message(message.chat.id, f"Error retrieving messages: {str(e)}")
# Start polling
bot.polling()
