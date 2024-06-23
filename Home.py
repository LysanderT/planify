import streamlit as st


def main():
    # st.sidebar.title("Navigation")
    pages = ["About", "Initial", "Desired", "Preferences", "Plan"]
    st.markdown("<h1 style='text-align: center;'>Planify</h1>", unsafe_allow_html=True)

    # TODO: modify the display
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
