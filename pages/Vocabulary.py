import streamlit as st
import pandas as pd
from gtts import gTTS
from io import BytesIO

st.write("🐾 Vocabulary learning")

tabs = st.tabs(["1. Tab1", "2. Tab2", "3. Tab3"])

with tabs[0]:
  st.write("Tab 1")

with tabs[1]:
  st.write("Tab 2")

with tabs[2]:
  st.write("Listen how to say the word")





  st.title("🔊 Word Pronunciation Practice")
  
  # --- Load CSV from GitHub ---
  @st.cache_data
  def load_data():
      url = "https://raw.githubusercontent.com/MK316/Digital-Literacy-Class/refs/heads/main/data/word_frequency.csv"  # ← replace this!
      return pd.read_csv(url)
  
  df = load_data()
  
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

