import streamlit as stx

def run(st):
    st.title("Update Preferences")
    if "preferences" not in stx.session_state:
        stx.session_state.preferences = {
            "night_work": 5,
            "extra_breaks": 5
        }
    # stx.session_state.preferences["night_work"] = st.slider("Preference for Night Work", 1, 10, value=stx.session_state.preferences["night_work"], key="night_work")
    # stx.session_state.preferences["extra_breaks"] = st.slider("Preference for Extra Breaks", 1, 10, value=stx.session_state.preferences["extra_breaks"], key="extra_breaks")
    stx.session_state.preferences["pref"] = st.text_input("Your extra preferences and commands:")
    print(stx.session_state.preferences["pref"])

    # col1, _, _, col4 = st.columns(4)
    # if col1.button("Back"):
    #     stx.session_state.page = "Desired"
    #     stx.experimental_rerun()
    # if col4.button("Next"):
    #     stx.session_state.page = "Plan"
    #     stx.experimental_rerun()