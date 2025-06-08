from telegram import Update
from telegram.ext import ContextTypes
import json
import random
import os

MOOD_RESPONSES = {
    "happy": [
        "That's awesome! 😊 Keep shining and spread that joy.",
        "Happiness looks great on you! 😄 Stay blessed.",
        "Yay! What made you happy today? Let’s celebrate it! 🎉"
    ],
    "sad": [
        "I'm here for you. 🌧️ It's okay to feel down sometimes.",
        "Sending you a virtual hug 🤗 You’re not alone.",
        "Everything will be okay. Take a deep breath. 💛"
    ],
    "stressed": [
        "Take a pause. You’re doing your best, and that’s enough. 🧘",
        "Let’s take one thing at a time. You’ve got this 💪",
        "Try a short walk or deep breathing – it helps! 🌿"
    ],
    "excited": [
        "That’s the energy we love! 🔥 What’s got you pumped?",
        "Wooo! Keep the excitement rolling! 🎊",
        "Amazing vibes! Ride that high wave 🌈"
    ],
    "bored": [
        "Let’s shake things up! Try learning something new today 🧠",
        "Boredom is just a creative spark waiting to happen 💡",
        "Want a tip or fun quote to lift your mood?"
    ]
}

async def handle_mood(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_message = update.message.text.lower()

    matched_moods = [mood for mood in MOOD_RESPONSES if mood in user_message]

    if matched_moods:
        selected_mood = matched_moods[0]
        reply = random.choice(MOOD_RESPONSES[selected_mood])
    else:
        reply = (
            "Thanks for sharing how you feel. 💬\n"
            "Would you like a quote or a hustle tip to help boost your mood?"
        )

    await update.message.reply_text(reply)

    # Save the mood to data.json
    user_id = str(update.effective_user.id)
    mood_entry = {"mood": user_message}

    data_path = "data.json"
    data = {}

    if os.path.exists(data_path):
        with open(data_path, "r") as file:
            try:
                data = json.load(file)
            except json.JSONDecodeError:
                data = {}

    data[user_id] = data.get(user_id, {})
    data[user_id]["mood"] = user_message

    with open(data_path, "w") as file:
        json.dump(data, file, indent=4)
