import streamlit as st
import pandas as pd
from gtts import gTTS
from io import BytesIO

st.write("🐾 Vocabulary learning")

tab1, tab2, tab3 = st.tabs(["1. Lesson: Word list", "2. Activity: Listen to the word", "3. Spelling practice"])

######### TAB 1


with tab1:
  st.markdown("### 📋 Word Frequency Table")

   # Load CSV from GitHub (update the link below)
  url = "https://raw.githubusercontent.com/MK316/Digital-Literacy-Class/refs/heads/main/data/word_frequency.csv"
  df = pd.read_csv(url)

    # Show table only when button is clicked
  if st.button("Show Word List"):
     st.dataframe(df, use_container_width=True)


######### TAB 2 

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


######### TAB 3

with tab3:
    st.markdown("### 🎧 Listen and Spell the Word")
    st.caption("Click the button to hear a word. Type what you heard below.")

    # Load your CSV data
    url = "https://raw.githubusercontent.com/MK316/Digital-Literacy-Class/refs/heads/main/data/word_frequency.csv"
    df = pd.read_csv(url)
    word_list = df["Word"].dropna().tolist()

    # Initialize session state
    if "current_word" not in st.session_state:
        st.session_state.current_word = None
        st.session_state.audio_data = None

    # Button to get a random word
    if st.button("🔊 Let me listen to a word"):
        st.session_state.current_word = random.choice(word_list)
        tts = gTTS(st.session_state.current_word, lang='en')
        audio_fp = BytesIO()
        tts.write_to_fp(audio_fp)
        audio_fp.seek(0)
        st.session_state.audio_data = audio_fp.read()

    # Play audio if available
    if st.session_state.audio_data:
        st.audio(st.session_state.audio_data, format='audio/mp3')

    # Input box to type what user hears
    user_input = st.text_input("Type the word you heard:")

    # Check answer
    if user_input and st.session_state.current_word:
        if user_input.strip().lower() == st.session_state.current_word.lower():
            st.success("✅ Correct!")
        else:
            st.error("❌ Try again.")
  
