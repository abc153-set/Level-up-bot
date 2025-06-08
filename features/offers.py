import random
from telegram import Update
from telegram.ext import ContextTypes

# Sample offers
offers = [
    {"title": "🔥 50% Off on Skillshare", "link": "https://skillshare.com"},
    {"title": "💼 Resume Builder Premium Free", "link": "https://resumebuild.com"},
    {"title": "📚 Free Udemy Course: Productivity", "link": "https://udemy.com"},
]

async def handle_offers(update: Update, context: ContextTypes.DEFAULT_TYPE):
    offer = random.choice(offers)
    await update.message.reply_text(f"{offer['title']}\n👉 {offer['link']}")
