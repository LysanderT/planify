import streamlit as st
from PIL import Image

def main():
    # st.sidebar.title("Navigation")
    pages = ["About", "Initial", "Desired", "Preferences", "Plan"]

    logo = Image.open("logo.png")

    cols = st.columns([1.5, 1])
    cols[1].image(logo, width=100)
    cols[0].markdown("<h1 style='text-align: right;'>&nbsp&nbspPlanify</h1>", unsafe_allow_html=True)

    # Display the logo and title side by side
    # st.markdown(
    #     """
    #     <div style='display: flex; justify-content: center; align-items: center;'>
    #         <img src="logo.svg" alt="Planify logo" width="50" height="50">
    #         <h1 style='text-align: center; margin-left: 10px;'>Planify</h1>
    #     </div>
    #     """,
    #     unsafe_allow_html=True
    # )

    if "page" not in st.session_state:
        st.session_state.page = "About"

    cols = st.columns(len(pages))

    for i, page in enumerate(pages):
        if cols[i].button(page):
            st.session_state.page = page
            st.experimental_rerun()
    if st.session_state.page == "Initial":
        import Initial
        Initial.run()
    elif st.session_state.page == "Desired":
        import Desired
        Desired.run()
    elif st.session_state.page == "Preferences":
        import Preferences
        Preferences.run()
    elif st.session_state.page == "Plan":
        import Plan
        Plan.run()
    elif st.session_state.page == "About":
        import About
        About.run()

if __name__ == "__main__":
    main()
