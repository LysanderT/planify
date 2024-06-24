import streamlit as stx
from datetime import datetime


def run(st):
    st.title("Initial Activities")

    if "initial_activities" not in stx.session_state:
        stx.session_state.initial_activities = [{
            "name": "",
            "weekday": "Monday",
            "start_time": datetime.strptime("00:00", "%H:%M").time(),
            "end_time": datetime.strptime("00:00", "%H:%M").time()
        }]

    def add_activity():
        stx.session_state.initial_activities.append({
            "name": "",
            "weekday": "Monday",
            "start_time": datetime.strptime("00:00", "%H:%M").time(),
            "end_time": datetime.strptime("00:00", "%H:%M").time()
        })

    def delete_activity(index):
        stx.session_state.initial_activities.pop(index)

    st.button("Add", on_click=add_activity, key = "Initial")

    for idx, activity in enumerate(stx.session_state.initial_activities):
        cols = st.columns([3, 2, 2, 2, 1])
        activity["name"] = cols[0].text_input("Activity Name", value=activity["name"], key=f"name_{idx}")
        activity["weekday"] = cols[1].selectbox("Weekday",
                                                ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday",
                                                 "Sunday"],
                                                index=["Monday", "Tuesday", "Wednesday", "Thursday", "Friday",
                                                       "Saturday", "Sunday"].index(activity["weekday"]),
                                                key=f"weekday_{idx}")
        activity["start_time"] = cols[2].time_input("Start Time", value=activity["start_time"], key=f"start_time_{idx}")
        activity["end_time"] = cols[3].time_input("End Time", value=activity["end_time"], key=f"end_time_{idx}")
        if len(stx.session_state.initial_activities) > 1:
            cols[4].button("Del", key=f"delete_{idx}", on_click=lambda i=idx: delete_activity(i))