# db.py

from pymongo import MongoClient

# ✅ Local MongoDB URI
client = MongoClient("mongodb+srv://malothvenni9:VjgvsjiKuZXwKcg1@chatbot.wgxb2ho.mongodb.net/?retryWrites=true&w=majority&appName=Chatbot")
db = client["mental_health"]
collection = db["chat_logs"]

def save_chat(user, user_msg, bot_msg, mood):
    collection.insert_one({
        "user": user,
        "user_msg": user_msg,
        "bot_msg": bot_msg,
        "mood": mood
    })

def get_user_history(user):
    return list(collection.find({"user": user}))
