import streamlit as st

# Initialize session state for storing activities
if "activities" not in st.session_state:
    st.session_state.activities = []

# Function to add a new activity
def add_activity():
    st.session_state.activities.append({"activity": "", "weekday": "", "start_time": "", "end_time": ""})

# Function to delete the last activity
def delete_activity():
    if st.session_state.activities:
        st.session_state.activities.pop()

# Function to generate the schedule dictionary
def generate_schedule():
    schedule = {}
    for activity in st.session_state.activities:
        if activity["weekday"] not in schedule:
            schedule[activity["weekday"]] = {}
        time_range = f"{activity['start_time']}-{activity['end_time']}"
        schedule[activity["weekday"]][time_range] = activity["activity"]
    st.session_state.generated_schedule = schedule

# Add and delete buttons
cols = st.columns(2)
cols[0].button("Add", on_click=add_activity)
cols[1].button("Delete", on_click=delete_activity)

# Display activity input fields
for i, activity in enumerate(st.session_state.activities):
    cols = st.columns(4)
    activity["activity"] = cols[0].text_input("Activity Name", value=activity["activity"], key=f"activity_{i}")
    activity["weekday"] = cols[1].selectbox("Weekday", ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"], index=["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"].index(activity["weekday"]) if activity["weekday"] else 0, key=f"weekday_{i}")
    activity["start_time"] = cols[2].text_input("Start Time", value=activity["start_time"], key=f"start_time_{i}")
    activity["end_time"] = cols[3].text_input("End Time", value=activity["end_time"], key=f"end_time_{i}")

# Generate button
if st.button("Generate"):
    generate_schedule()
    st.json(st.session_state.generated_schedule)
