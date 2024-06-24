import streamlit as st
import json

from src.Client import generate
from src.Render import gen_calendar

def run():
    st.title("My Personal Plan")

    schedule = {}
    if "initial_activities" not in st.session_state:
        pass
    else:
        for activity in st.session_state.initial_activities:
            if activity["name"] == "":
                continue
            else:
                day = activity["weekday"]
                if day not in schedule:
                    schedule[day] = {}
                time_range = f"{activity['start_time']}-{activity['end_time']}"
                schedule[day][time_range] = activity["name"]

        # st.json(schedule)

    unfixed = {}
    if "add_on_activities" not in st.session_state:
        pass
    else:
        for activity in st.session_state.add_on_activities:
            if activity["name"] == "":
                continue
            else:
                unfixed[activity["name"]] = {
                    "importance": activity["importance"],
                    "hours": activity["duration"]
                }

    prefs = {}
    if "preferences" not in st.session_state:
        pass
    else:
        prefs = st.session_state.preferences

    planned_json = generate(json.dumps(schedule), json.dumps(unfixed), json.dumps(prefs))
    gen_calendar(json.loads(planned_json))

    if st.button("Back"):
        st.session_state.page = "Preferences"
        st.experimental_rerun()
