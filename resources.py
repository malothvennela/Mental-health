# resources.py

quotes = {
    "positive": "Keep shining! 🌞 You're doing great!",
    "neutral": "Take a deep breath and keep going. 🌿",
    "negative": "Tough times never last, but tough people do. 💪"
}

music_links = {
    "positive": "https://www.youtube.com/watch?v=ZbZSe6N_BXs",
    "neutral": "https://www.youtube.com/watch?v=5qap5aO4i9A",
    "negative": "https://www.youtube.com/watch?v=2OEL4P1Rz04"
}

def get_quote(mood):
    return quotes.get(mood, quotes["neutral"])

def get_music_link(mood):
    return music_links.get(mood, music_links["neutral"])
