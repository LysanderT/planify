import streamlit as st

def run():
    st.title("Update Preferences")
    if "preferences" not in st.session_state:
        st.session_state.preferences = {
            "night_work": 5,
            "extra_breaks": 5
        }

    st.slider("Preference for Night Work", 1, 10, value=st.session_state.preferences["night_work"], key="night_work")
    st.slider("Preference for Extra Breaks", 1, 10, value=st.session_state.preferences["extra_breaks"], key="extra_breaks")

    col1, col2 = st.columns(2)
    if col1.button("Back"):
        st.session_state.page = "Desired"
        st.experimental_rerun()
    if col2.button("Next"):
        st.session_state.page = "Plan"
        st.experimental_rerun()
