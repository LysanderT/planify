import streamlit as st
import os
from PIL import Image

def main():
    # st.sidebar.title("Navigation")
    cols = st.columns([5,4])
    icon = Image.open("Icon.png")
    cols[1].image(icon, width= 100)
    # 图像路径
    #image_path = "Icon.png"

    # 使用 HTML 和 CSS 将图像对齐到右侧
    # cols[0].markdown(
    #     f"""
    #     <div style="text-align: right;">
    #         <img src="{image_path}" width="100">
    #     </div>
    #     """,
    #     unsafe_allow_html=True
    # )
    cols[0].markdown("<h1 style='text-align: right;'>Planify</h1>", unsafe_allow_html=True)

    # TODO: modify the display
    if "page" not in st.session_state:
        st.session_state.page = "About"

    cols = st.columns(2)
    planify = cols[0].button("Planify!")

    #Remove Previous ics
    if os.path.exists("calendar.ics"):
        os.remove("calendar.ics")

    # for i, page in enumerate(pages):
    #     if cols[i].button(page):
    #         st.session_state.page = page
    #         st.experimental_rerun()
    # if st.session_state.page == "Initial":
    #     import Initial
    #     Initial.run(tab[0])
    # elif st.session_state.page == "Desired":
    #     import Desired
    #     Desired.run(tab[1])
    # elif st.session_state.page == "Preferences":
    #     import Preferences
    #     Preferences.run(tab[2])
    # elif st.session_state.page == "Plan":
    #     import Plan
    #     Plan.run(tab[3])
    # elif st.session_state.page == "About":
    #     import About
    #     About.run(tab[4])

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
