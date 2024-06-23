from openai import OpenAI

client = OpenAI()

def generate(fix_plan:str, flex_plan:str, pref:str)->str:
    system = '''
    #You are a schedule management assistant.

    I can add schedules to you in the following two ways:
    1. Input schedules in JSON format with a confirmed time.
    2. Input schedules in natural language with an uncertain time, and provide the duration and importance of the activity.

    I will confirm the schedule in the following format for a scheduled event:

    {
    "/activity_name1/": {"start_time": "/HH:MM/", "end_time": "/HH:MM/", "routine": "/routine in plain text/"}
    "/activity_name2/": {"start_time": "/HH:MM/", "end_time": "/HH:MM/", "routine": "/routine in plain text/"}
    ...
    }

    I will input the schedule in the following format for an unscheduled event:

    {
    "/activity_name1/": {"importance": "/a float number from 0 to 1/", "hours": "/time length in float/", "comment": "/comments in plain texts/"}
    "/activity_name2/": {"importance": "/a float number from 0 to 1/", "hours": "/time length in float/", "comment": "/comments in plain texts/"}
    ...
    }'''

    prompt1 = '''Here are the schedules I would like to add:\n'''

    prompt2 = '''
    Please merge the loose schedules into the calendar. To do so, please add them in the order of descending importance first, if there is enough space to place the event without conflicting with another. 
    For the less important events, you may move them to the end of the day or the end of the week. If we run out of time, just display "False".

    Please output the complete schedule in JSON format, as follows:

    {
    "Monday": {
        "/time period1/": "/activity_name1/"
        "/time period2/": "/activity_name2/"
        ...
    },
    "Tuesday": {
        "/time period1/": "/activity_name1/"
        "/time period2/": "/activity_name2/"
        ...
    },
    "Wednesday": {
        "/time period1/": "/activity_name1/"
        "/time period2/": "/activity_name2/"
        ...
    },
    "Thursday": {
        "/time period1/": "/activity_name1/"
        "/time period2/": "/activity_name2/"
        ...
    },
    "Friday": {
        "/time period1/": "/activity_name1/"
        "/time period2/": "/activity_name2/"
        ...
    },
    "Saturday": {
        "/time period1/": "/activity_name1/"
        "/time period2/": "/activity_name2/"
        ...
    },
    "Sunday": {
        "/time period1/": "/activity_name1/"
        "/time period2/": "/activity_name2/"
        ...
    },
    }

    Please only output this schedule, do not output any other plain text.'''

    istream1 = prompt1 + "Fixed:\n" + fix_plan + "\nUnfixed:\n" + flex_plan + f"I want the schedule to be planned with the following preferences: {pref}\n"
    istream2 = prompt2

    #First Question
    completion = client.chat.completions.create(
        model="gpt-4o",
        response_format={ "type": "json_object" },
        messages=[
            {"role": "system", "content": system},
            {"role": "user", "content": istream1}
        ]
    )

    response1 = completion.choices[0].message.content
    # print(response1)

    #Second Question
    completion = client.chat.completions.create(
        model="gpt-4o",
        response_format={ "type": "json_object" },
        messages=[
            {"role": "system", "content": system},
            {"role": "user", "content": istream1},
            {"role": "assistant", "content": response1},
            {"role": "user", "content": istream2}
        ]
    )

    response2 = completion.choices[0].message.content

    return response2
