import streamlit as st
from datetime import datetime

def run():
    st.title("Initial Activity")
    if "initial_activities" not in st.session_state:
        st.session_state.initial_activities = [{
            "name": "",
            "weekday": "Monday",
            "start_time": datetime.strptime("00:00", "%H:%M").time(),
            "end_time": datetime.strptime("00:00", "%H:%M").time()
        }]

    def add_activity():
        st.session_state.initial_activities.append({
            "name": "",
            "weekday": "Monday",
            "start_time": datetime.strptime("00:00", "%H:%M").time(),
            "end_time": datetime.strptime("00:00", "%H:%M").time()
        })

    def delete_activity(index):
        st.session_state.initial_activities.pop(index)

    st.button("Add", on_click=add_activity)
    
    for idx, activity in enumerate(st.session_state.initial_activities):
        cols = st.columns([3, 2, 2, 2, 1])
        cols[0].text_input("Activity Name", value=activity["name"], key=f"name_{idx}")
        cols[1].selectbox("Weekday", ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"], index=["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"].index(activity["weekday"]), key=f"weekday_{idx}")
        cols[2].time_input("Start Time", value=activity["start_time"], key=f"start_time_{idx}")
        cols[3].time_input("End Time", value=activity["end_time"], key=f"end_time_{idx}")
        if len(st.session_state.initial_activities) > 1:
            cols[4].button("Delete", key=f"delete_{idx}", on_click=lambda i=idx: delete_activity(i))

    if st.button("Next"):
        st.session_state.page = "Add-On Activity"
        st.experimental_rerun()
