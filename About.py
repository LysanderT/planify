import streamlit as st


def run():
    # st.title("About Planify")
    st.markdown("""
                
    ## About Planify

    Planify is a comprehensive scheduling and planning tool designed to help you manage your current weekly activities, add new tasks, and prioritize your responsibilities efficiently.

    #### Features
    - **Initial**: Manually schedule your established activities or import an existing schedule with specific start and end times for each day of the week.
    - **Desired**: Add additional tasks and events with a focus on their importance and duration.
    - **Preferences**: Update and set your preferences for night work and extra breaks to customize your schedule.
    - **Plan**: View your created schedule! Also has a summarized JSON format of your planned activities and tasks.

    #### Developers
    Planify was developed by Lysander, Lakshya, and Shuhan with a focus on providing the best user experience for managing daily tasks and schedules.

    We hope you find Planify helpful in organizing your daily activities and tasks!

    """)

    # col1, _, _, col4 = st.columns(4)
    _, col2, _ = st.columns(3,vertical_alignment="center", gap = "large")
    if col2.button("Start Here!"):
        st.session_state.page = "Initial"
        st.experimental_rerun()