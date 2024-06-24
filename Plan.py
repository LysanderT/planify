import streamlit as stx
import json

from Client import generate
from Gen_page import gen_calendar

def run(st):
    st.title("My Personal Plan")

    schedule = {}
    if "initial_activities" not in stx.session_state:
        pass
    else:
        for activity in stx.session_state.initial_activities:
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
    if "add_on_activities" not in stx.session_state:
        pass
    else:
        for activity in stx.session_state.add_on_activities:
            if activity["name"] == "":
                continue
            else:
                # unfixed.append({
                #     activity["name"]: {
                #         "importance": activity["importance"],
                #         "hours": activity["duration"]
                #     }
                # })
                unfixed[activity["name"]] = {
                    "importance": activity["importance"],
                    "hours": activity["duration"]
                }

        # st.json(unfixed)

    # prefs = {}
    # if "preferences" not in stx.session_state:
    #     pass
    # else:
    #     prefs = stx.session_state.preferences
    prefs = stx.session_state.preferences["pref"]

    #try:
    planned_json = generate(json.dumps(schedule), json.dumps(unfixed), prefs)
    gen_calendar(json.loads(planned_json), st)
    # except:
    #     pass

    # if st.button("Back"):
    #     stx.session_state.page = "Preferences"
    #     stx.experimental_rerun()
