import streamlit as stx

def run(st):
    st.title("Update Preferences")
    if "preferences" not in stx.session_state:
        stx.session_state.preferences = {
            "night_work": 5,
            "extra_breaks": 5
        }
    stx.session_state.preferences["pref"] = st.text_input("Your extra preferences and commands:")
    print(stx.session_state.preferences["pref"])