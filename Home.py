import streamlit as st
import os
from PIL import Image

def main():
    cols = st.columns([5,4])
    icon = Image.open("Icon.png")
    cols[1].image(icon, width= 100)
    cols[0].markdown("<h1 style='text-align: right;'>Planify</h1>", unsafe_allow_html=True)

    cols = st.columns(2)
    planify = cols[0].button("Planify!")

    #Delete previous cache and create new cache
    if os.path.exists("calendar.ics"):
        os.remove("calendar.ics")
    if not os.path.exists("ics_file"):
        os.makedirs("ics_file")

    #Split tabs
    tab = st.tabs(["Initial→", "Desired→", "Preferences", "*About"])

    import Initial
    Initial.run(tab[0])

    import Desired
    Desired.run(tab[1])

    import Preferences
    Preferences.run(tab[2])

    import Plan
    if planify:
        st.session_state.left_size = 1
        st.session_state.right_size = 1
        Plan.run(st)
    
    import About
    About.run(tab[3])


if __name__ == "__main__":
    main()
