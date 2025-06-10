import json

DATA_FILE = "data/analytics.json"

def get_top_users(limit=5):
    try:
        with open(DATA_FILE, "r") as f:
            data = json.load(f)
    except FileNotFoundError:
        return []

    user_counts = [(user_data["name"], len(user_data.get("messages", []))) for user_data in data.values()]
    sorted_users = sorted(user_counts, key=lambda x: x[1], reverse=True)
    return sorted_users[:limit]

def get_common_moods(limit=5):
    try:
        with open(DATA_FILE, "r") as f:
            data = json.load(f)
    except FileNotFoundError:
        return []

    mood_counts = {}
    for user_data in data.values():
        mood = user_data.get("mood", "").strip().lower()
        if mood:
            mood_counts[mood] = mood_counts.get(mood, 0) + 1

    sorted_moods = sorted(mood_counts.items(), key=lambda x: x[1], reverse=True)
    return sorted_moods[:limit]
