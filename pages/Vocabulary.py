import streamlit as st

st.write("🐾 Vocabulary learning")

tabs = st.tabs(["1. Tab1", "2. Tab2", "3. Tab3"])

with tabs[0]:
  st.write("Tab 1")

with tabs[1]:
  st.write("Tab 2")

with tabs[2]:
  st.write("Tab 3")
