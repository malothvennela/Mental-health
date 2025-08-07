# app.py

import streamlit as st
from nlp_model import analyze_sentiment
from db import save_chat, get_user_history
from resources import get_quote, get_music_link
from llm_response import generate_response

st.set_page_config(page_title="🧠 Mental Health Support Chatbot", layout="wide")

st.title("🧠 AI Mental Health Support Bot")

user = st.text_input("Enter your name", key="username")

if user:
    st.subheader(f"👋 Hello, {user}! Let's talk.")
    chat_input = st.text_area("💬 You:", height=100, key="chat_input")

    if st.button("Send"):
        if chat_input.strip() == "":
            st.warning("Please enter a message.")
        else:
            mood = analyze_sentiment(chat_input)
            bot_reply = generate_response(chat_input)
            save_chat(user, chat_input, bot_reply, mood)

            st.markdown(f"**🤖 Bot:** {bot_reply}")
            st.markdown(f"**🧠 Mood detected:** `{mood}`")
            st.markdown(f"**🌟 Quote:** {get_quote(mood)}")
            st.video(get_music_link(mood))

    with st.expander("📜 Chat History"):
        history = get_user_history(user)
        for item in history[::-1]:
            st.markdown(f"**You:** {item['user_msg']}")
            st.markdown(f"**Bot:** {item['bot_msg']}")
            st.markdown(f"🧠 Mood: `{item['mood']}`")
            st.markdown("---")
