import streamlit as st

def run():
    st.title("My Personal Plan")

    schedule = {}
    for activity in st.session_state.initial_activities:
        day = activity["weekday"]
        if day not in schedule:
            schedule[day] = {}
        time_range = f"{activity['start_time']}-{activity['end_time']}"
        schedule[day][time_range] = activity["name"]

    st.json(schedule)

    unfixed = []
    for activity in st.session_state.add_on_activities:
        unfixed.append({
            activity["name"]: {
                "importance": activity["importance"],
                "hours": activity["duration"]
            }
        })

    st.json(unfixed)

    if st.button("Back"):
        st.session_state.page = "Preferences"
        st.experimental_rerun()
