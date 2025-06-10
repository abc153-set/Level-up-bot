# features/offers.py

from telegram import Update
from telegram.ext import ContextTypes
import json
import random
import os

from features.analytics import 
track_command

OFFERS_FILE = "data/offers.json"  

# Load offers from JSON or fallback
def load_offers():
    if os.path.exists(OFFERS_FILE):
        try:
            with open(OFFERS_FILE, 
"r") as f:
                offers = json.load(f)
                if isinstance(offers,
list) and offers:
                    return offers
        except json.JSONDecodeError:
            pass

    # Fallback hardcoded offers
    return [
        "🛒 *Amazon Offer*: Get 10% cashback on electronics 👉 [Grab Deal](https://amzn.to/xyz)",
        "📚 *Udemy Sale*: Courses at ₹449 only 👉 [Enroll Now](https://www.udemy.com/)",
        "💼 *Internshala*: Learn & earn internships 👉 [Apply Here](https://internshala.com/)",
        "🧠 *Skillshare*: Free 1-month learning 👉 [Try Free](https://www.skillshare.com/)"
    ]

# /offer command handler
async def handle_offers(update:
Update, context: 
ContextTypes.DEFAULT_TYPE):
    track_command("hustle", 
update.effective_user)
    
    offers = load_offers()
    offer = random.choice(offers)

    await update.message.reply_markdown_v2(
        f"🎁 *Today's Special Offer:*\n{offer}",
        disable_web_page_preview=True
    )
