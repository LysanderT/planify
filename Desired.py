import streamlit as st


def run():
    st.title("Add Activities")

    if "add_on_activities" not in st.session_state:
        st.session_state.add_on_activities = [{
            "name": "",
            "importance": 1,
            "duration": 1
        }]

    def add_add_on_activity():
        st.session_state.add_on_activities.append({
            "name": "",
            "importance": 1,
            "duration": 1
        })

    def delete_add_on_activity(index):
        st.session_state.add_on_activities.pop(index)

    st.button("Add", on_click=add_add_on_activity)

    for idx, activity in enumerate(st.session_state.add_on_activities):
        cols = st.columns([3, 2, 2, 1])
        activity["name"] = cols[0].text_input("Name", value=activity["name"], key=f"addon_name_{idx}")
        activity["importance"] = cols[1].slider("Importance", 0.0, 1.0, 0.5, 0.01,
                                                key=f"addon_importance_{idx}")
        activity["duration"] = cols[2].number_input("Duration (hours)", min_value=0.0, step=0.5,
                                                    key=f"addon_duration_{idx}")
        if len(st.session_state.add_on_activities) > 1:
            cols[3].button("Del", key=f"addon_delete_{idx}", on_click=lambda i=idx: delete_add_on_activity(i))

    col1, _, _, col4 = st.columns(4)
    if col1.button("Back"):
        st.session_state.page = "Initial"
        st.experimental_rerun()
    if col4.button("Next"):
        st.session_state.page = "Preferences"
        st.experimental_rerun()
