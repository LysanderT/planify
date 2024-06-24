import streamlit as st
from PIL import Image
import src.Initial as Initial
import src.Desired as Desired
import src.Preferences as Preferences
import src.Plan as Plan
import src.About as About

def main():
    # st.sidebar.title("Navigation")
    pages = ["About", "Initial", "Desired", "Preferences", "Plan"]

    logo = Image.open("images/logo.png")

    cols = st.columns([1.5, 1])
    cols[1].image(logo, width=100)
    cols[0].markdown("<h1 style='text-align: right;'>&nbsp&nbspPlanify</h1>", unsafe_allow_html=True)

    if "page" not in st.session_state:
        st.session_state.page = "About"

    cols = st.columns(len(pages))

    for i, page in enumerate(pages):
        if cols[i].button(page):
            st.session_state.page = page
            st.experimental_rerun()
    if st.session_state.page == "Initial":
        Initial.run()
    elif st.session_state.page == "Desired":
        Desired.run()
    elif st.session_state.page == "Preferences":
        Preferences.run()
    elif st.session_state.page == "Plan":
        Plan.run()
    elif st.session_state.page == "About":
        About.run()

if __name__ == "__main__":
    main()
