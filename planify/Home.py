import streamlit as st

def main():
    st.set_page_config(page_title="Activity Scheduler", layout="wide")
    st.title("Activity Scheduler")
    st.write("This is a multi-page Streamlit application.")

    pages = {
        "Initial Activity": "InitialActivity",
        "Add-On Activity": "AddOnActivity",
        "Preferences": "Preferences",
        "Summary": "Summary"
    }

    if "page" not in st.session_state:
        st.session_state.page = "Initial Activity"

    st.sidebar.title("Navigation")
    choice = st.sidebar.radio("Go to", list(pages.keys()))

    st.session_state.page = choice

    if st.session_state.page == "Initial Activity":
        import InitialActivity
        InitialActivity.run()
    elif st.session_state.page == "Add-On Activity":
        import AddOnActivity
        AddOnActivity.run()
    elif st.session_state.page == "Preferences":
        import Preferences
        Preferences.run()
    elif st.session_state.page == "Summary":
        import Summary
        Summary.run()

if __name__ == "__main__":
    main()
