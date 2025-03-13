import streamlit as st
import webbrowser

st.title("Bulk Google Search")

# User input
keywords = st.text_area("Enter Keywords (one per line) and click 'Search All'.")

if st.button("Search All"):
    if keywords:
        search_queries = keywords.split("\n")
        for query in search_queries:
            query = query.strip()
            if query:
                search_url = f"https://www.google.com/search?q={query.replace(' ', '+')}"
                webbrowser.open_new_tab(search_url)  # Open in new tab
                st.success(f"Searching: {query}")  # Show confirmation message
    else:
        st.warning("Please enter at least one keyword.")
