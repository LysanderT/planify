import streamlit as st
from streamlit_calendar import calendar
#from my_calendar import calendar
import random as rd
#import json

# st.set_page_config(page_title="Demo for streamlit-calendar", page_icon="📆")

fake_data = '''
{
  "Monday": {
    "8:30-10:00": "Calculus",
    "14:30-16:00": "Physics",
    "18:00-20:00": "Write Thesis",
    "20:00-21:00": "Practice Driving"
  },
  "Tuesday": {
    "9:30-11:00": "Chemistry",
    "13:30-15:00": "Linear Algebra",
    "16:00-18:00": "Coding",
    "18:00-20:00": "Play Ping Pong",
    "20:00-21:00": "Practice Driving"
  },
  "Wednesday": {
    "8:30-10:00": "Calculus",
    "14:30-16:00": "Physics",
    "18:00-20:00": "Write Thesis",
    "20:00-21:00": "Practice Driving"
  },
  "Thursday": {
    "9:30-11:00": "Chemistry",
    "13:30-15:00": "Linear Algebra",
    "16:00-18:00": "Coding",
    "18:00-20:00": "Play Ping Pong",
    "20:00-21:00": "Practice Driving"
  },
  "Friday": {
    "9:30-11:00": "Chemistry",
    "14:30-16:00": "Physics",
    "18:00-20:00": "Write Thesis",
    "20:00-21:00": "Practice Driving"
  },
  "Saturday": {
    "10:00-12:00": "Write Thesis",
    "13:00-16:00": "Coding",
    "17:00-19:00": "Play Ping Pong",
    "19:00-20:00": "Practice Driving"
  },
  "Sunday": {
    "10:00-12:00": "Write Thesis",
    "13:00-16:00": "Coding",
    "17:00-19:00": "Play Ping Pong",
    "19:00-20:00": "Practice Driving"
  }
}
'''
def gen_calendar(llm_out:dict)->None:
    def random_color()->None:
        output = "#"
        lst = list("FE0123456789ABCD")
        for i in range(3):
            while lst[0] > '7': #Guarantee the color is not too dark
                rd.shuffle(lst)
            output += lst[0] + lst[1]
            rd.shuffle(lst)
        return output
        
    TO_DATE = {"Monday": "2024-06-24", "Tuesday": "2024-06-25", "Wednesday": "2024-06-26", "Thursday": "2024-06-27", "Friday": "2024-06-28", "Saturday": "2024-06-29", "Sunday": "2024-06-23"}

    #Decode events
    events = []
    for key, value in llm_out.items():
        for time, activity in value.items():

            start_time = f"{TO_DATE[key]}T{time.split('-')[0]}:00"
            if len(start_time) != 19:
                start_time = start_time[:11] + "0" + start_time[11:]

            end_time = f"{TO_DATE[key]}T{time.split('-')[1]}:00"
            if len(start_time) != 19:
                end_time = end_time[:11] + "0" + end_time[11:]
            
            events.append({
                "title": activity,
                "color": random_color(),
                "start": start_time,
                "end": end_time
            })

    #Display calendar
    calendar_options = {
        "editable": "false",
        "navLinks": "false",
        "resources": None,
        "selectable": "false",
        "initialView": "timeGridWeek",
    }
    state = calendar(
        events=st.session_state.get("events", events),
        options=calendar_options,
        custom_css="""
        .fc-event-past {
            opacity: 0.8;
        }
        .fc-event-time {
            font-style: italic;
        }
        .fc-event-title {
            font-weight: 700;
        }
        .fc-toolbar-title {
            font-size: 2rem;
        }
        """,
        key="timegrid"
    )

if __name__ == "__main__":
    import json
    gen_calendar(llm_out=json.loads(fake_data))