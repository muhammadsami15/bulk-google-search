import webbrowser
import streamlit as st

# Streamlit app title
st.title("Bulk Google Search")

# Instructions
st.write("Enter Keywords (one per line) and click 'Search All'.")

# Multi-line text input
keywords = st.text_area("Enter Keywords Here", height=200)

# Search function
def search_keywords():
    search_terms = keywords.strip().split("\n")
    search_terms = [term.strip() for term in search_terms if term.strip()]
    for term in search_terms:
        webbrowser.open(f"https://www.google.com/search?q={term}")

# Search button
if st.button("Search All"):
    search_keywords()
    st.success("Searching... (Check your browser)")
