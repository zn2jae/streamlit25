import streamlit as st
import pandas as pd
from gtts import gTTS
from io import BytesIO

st.write("🐾 Vocabulary learning")

tab1, tab2 = st.tabs(["1. Lesson: Word list", "2. Activity: Listen to the word"])

with tab1:
  st.markdown("### 📋 Word Frequency Table")

   # Load CSV from GitHub (update the link below)
  url = "https://raw.githubusercontent.com/MK316/Digital-Literacy-Class/refs/heads/main/data/word_frequency.csv"
  df = pd.read_csv(url)

    # Show table only when button is clicked
  if st.button("Show Word List"):
     st.dataframe(df, use_container_width=True)

with tab2:

  st.title("🔊 Word Pronunciation Practice")
  
  # --- Load CSV from GitHub ---

  url = "https://raw.githubusercontent.com/MK316/Digital-Literacy-Class/refs/heads/main/data/word_frequency.csv"  # ← replace this!
  df = pd.read_csv(url)
  
  # --- Dropdown to select word ---
  st.markdown("## Select a word to hear its pronunciation")
  selected_word = st.selectbox("Choose a word:", df["Word"].dropna().unique())
  
  # --- Generate and play audio ---
  if selected_word:
      tts = gTTS(selected_word, lang='en')
      audio_fp = BytesIO()
      tts.write_to_fp(audio_fp)
      audio_fp.seek(0)
      st.audio(audio_fp, format='audio/mp3')

