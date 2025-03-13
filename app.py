import streamlit as st

def generate_search_links(keywords):
    search_links = []
    for keyword in keywords:
        search_url = f"https://www.google.com/search?q={keyword}"
        search_links.append(f"[{keyword}]({search_url})")
    return search_links

st.title("Bulk Google Search")

st.write("Enter Keywords (one per line) and click 'Search All'.")

keywords_input = st.text_area("Enter Keywords Here")

if st.button("Search All"):
    keywords = keywords_input.strip().split("\n")
    keywords = [k.strip() for k in keywords if k.strip()]
    
    if keywords:
        st.success("Here are your search links:")
        for link in generate_search_links(keywords):
            st.markdown(link, unsafe_allow_html=True)
    else:
        st.error("Please enter at least one keyword.")
