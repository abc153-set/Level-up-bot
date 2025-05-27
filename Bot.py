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

# Start polling
bot.polling()
