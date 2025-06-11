# 🤖 LevelUp – AI Life Assistant Telegram Bot

An emotionally engaging, modular, and hustle-focused AI Telegram bot built using `python-telegram-bot v20.8`.

💡 Features:
- Daily Hustle Tips 🧠
- Motivational Quotes 📢
- Mood Tracking 💖
- Affiliate Offers 💸
- Personal Stats 📊
- Human-like Warm Replies 🤗
- Offline fallback via JSON files 📁

🎯 Modular Code • Clean UI • Easy Edits via GitHub • Mobile-Friendly

---

## 📁 Folder Structure

```
├── bot.py
├── .env
├── requirements.txt
├── .gitignore
├── README.md
├── features/
│   ├── __init__.py
│   ├── start.py
│   ├── menu.py
│   ├── mood.py
│   ├── hustle.py
│   ├── offers.py
│   └── stats.py
├── data/
│   ├── quotes.json
│   ├── hustle_tips.json
│   └── offers.json
```

---

## ⚙️ Installation & Setup

1. Clone the repo or upload to GitHub:
```bash
git clone https://github.com/your-username/levelup-bot.git
```

2. Create `.env` file:
```
BOT_TOKEN=your_telegram_bot_token
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run the bot:
```bash
python bot.py
```

---

## 🚀 Features

### `/start` – Welcome Message
Sends a warm, friendly welcome with quick buttons.

### `/menu` – Quick Access Menu
Lets user explore all features with inline buttons.

### `/mood` – Mood Tracker
Saves and responds emotionally to your daily mood 💌.

### `/hustle` – Daily Hustle Tips
100+ curated hustle tips loaded from `data/hustle_tips.json`.

### `/quote` – Motivation Booster
Shows powerful motivational quotes from `data/quotes.json`.

### `/offers` – Affiliate Deals
Displays money-saving offers from `data/offers.json`.

### `/stats` – Personal Data
Shows mood and usage stats stored locally via JSON.

---

## 📁 JSON Content Files (Offline Support)

Easily edit or add content:

- `data/quotes.json` – 100 motivational quotes
- `data/hustle_tips.json` – 100 hustle tips
- `data/offers.json` – Affiliate deals with emojis

📝 No code changes required. Just edit these files.

---

## ☁️ Hosting on Render.com

Steps:
- Push project to GitHub
- Connect repo on [Render.com](https://render.com/)
- Set environment variable: `BOT_TOKEN`
- Build command:
```bash
pip install -r requirements.txt
```
- Start command:
```bash
python bot.py
```

✅ Free plan works for basic usage.

---

## 🤝 Contributing

PRs and suggestions welcome. Let’s build something awesome together!

---

## 🪪 License

MIT License – Use freely, credit appreciated.
Features Overview (Updated)

✅ Mood Tracking with Emojis — User ka mood detect kar ke emoji ke saath save hota hai.

📊 User Analytics — Track karta hai top active users aur unke interactions (offline JSON based).

✨ MarkdownV2 Formatting — Telegram messages mein stylish formatting ke liye MarkdownV2 ka use.

💬 Emotionally Intelligent Responses — Bot baat karta hai jaise ek close friend ho.

🔌 Offline JSON Storage — Firebase-free, local data system using .json files.



---

📈 Analytics Module

Automatically tracks:

Total messages sent by each user.

Most active users (used in /stats command).


Stored safely in data/user_data.json.



---

🧾 MarkdownV2 Usage

Used for:

Bold/Italic mood messages.

User names and emojis in responses.

Ensures clean, human-readable formatting.


> ⚠️ MarkdownV2 is currently used only in mood-related responses. Other modules use plain text for simplicity and stability.
