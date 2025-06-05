import json
import firebase_admin
from firebase_admin import credentials, firestore

# Load Firebase config
with open('firebase_config.json') as f:
    firebase_config = json.load(f)

cred = credentials.Certificate(firebase_config)
firebase_admin.initialize_app(cred)
db = firestore.client()

import telebot

# Your Telegram Bot Token
BOT_TOKEN = 
"8125526527:AAEd2PVmfb1CATBCxKHzgXec6
DXNI5ZqB1o"
bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Welcome to LevelUp AI Bot! Type /help to see commands.")

@bot.message_handler(commands=['help'])
def help_command(message):
    bot.send_message(message.chat.id, "/start - Welcome message\n/help - List of commands\n/tip - Get a hustle tip")

@bot.message_handler(commands=['tip'])
def send_tip(message):
    tip_ref = db.collection("tips").document("daily_tip")
    tip_doc = tip_ref.get()
    if tip_doc.exists:
        tip = tip_doc.to_dict().get("text", "Tip not found.")
        bot.send_message(message.chat.id, f"💡 Hustle Tip: {tip}")
    else:
        bot.send_message(message.chat.id, "❌ No tip found in database.")

bot.polling()
