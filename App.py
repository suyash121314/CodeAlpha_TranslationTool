import streamlit as st
from googletrans import Translator

# Initialize translator
translator = Translator()

# Title
st.title("🌐 Language Translation Tool")

# Input text
text = st.text_area("Enter text:")

# Language selection
lang = st.selectbox("Select target language:", ["hi", "mr", "en", "fr", "de"])

# Translate button
if st.button("Translate"):
    if text:
        translated = translator.translate(text, dest=lang)
        st.success(translated.text)
    else:
        st.warning("Please enter some text")
