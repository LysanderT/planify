import streamlit as stx
from streamlit_calendar import calendar
import random as rd
import json
from ics import Calendar, Event
import os

c = Calendar()
e = Event()

fake_data = '''
{
  "Monday": {
    "8:30-10:00": "Calculus2",
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

def combine_ics():
   with open('calendar.ics', 'w') as outfile:
        outfile.write('''BEGIN:VCALENDAR

VERSION:2.0

PRODID:ics.py - http://git.io/lLljaA
                      ''')
        for filename in os.listdir('ics_file'):
            file_path = os.path.join('ics_file', filename)
            if os.path.isfile(file_path):
                with open(file_path, 'r') as infile:
                    lines = infile.readlines()
                    if len(lines) > 2:  # Ensure the file has more than two lines
                        outfile.writelines(lines[5:-1])  # Write lines except the first and last
                    elif len(lines) == 2:  # If the file has exactly two lines, write only the second line
                        outfile.write(lines[1])
            os.remove(file_path)
        outfile.write('''END:VCALENDAR''')

def gen_calendar(llm_out:dict, st)->None:
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
          if len(list(start_time)) != 19:
            start_time = f"{TO_DATE[key]}T0{time.split('-')[0]}:00"

          end_time = f"{TO_DATE[key]}T{time.split('-')[1]}:00"
          if len(list(end_time)) != 19:
            end_time = f"{TO_DATE[key]}T0{time.split('-')[1]}:00"
          
          #To Display Calendar
          events.append({
              "title": activity,
              "color": random_color(),
              "start": start_time,
              "end": end_time
          })

          print(start_time, end_time)

          #To ics
          e.name = activity
          try:
            e.begin = start_time.split('T')[0] + ' ' + start_time.split('T')[1]
            e.end = end_time.split('T')[0] + ' ' + end_time.split('T')[1]
          except:
            print(start_time, end_time)

          c.events.add(e)
          with open(f'ics_file/{activity}.ics', 'w') as f:
            f.writelines(c.serialize_iter())
  combine_ics()

  #Display calendar
  calendar_options = {
      "editable": "false",
      "navLinks": "false",
      "resources": None,
      "selectable": "false",
      "initialView": "timeGridWeek",
  }
  state = calendar(
      events=stx.session_state.get("events", events),
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
      key="timegrid",
      callbacks=[]
  )
  return state

if __name__ == "__main__":
  show_calendar = stx.checkbox("Show Calendar", value=False)
  if show_calendar:
    gen_calendar(json.loads(fake_data), stx)