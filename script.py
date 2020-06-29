"""
This script checks which exercises to repeat today.

# TODO set this script to be executed as a cron job every morning.
"""

import json
from datetime import datetime, timedelta
from pushover import init, Client
import os



pushover_client = Client(api_token=os.environ['PUSHOVER_APP'], user_key=os.environ['PUSHOVER_USER'])

DAYS_TO_REPEAT = {
    "A" : [2, 10, 30, 60, 110],
    "B" : [2, 6, 14, 30, 60, 110],
    "C" : [1, 3, 7, 15, 30, 60, 110]
}

with open('exercise_list.json') as f:
    exercises = json.loads(f.read())

exercises_to_repeat_today = []
messages_to_push_today = []

for e in exercises:
    course = exercises[e]['course']
    exercise = exercises[e]['exercise']
    score = exercises[e]['score']
    raw_date = exercises[e]['date']
    date = datetime.strptime(raw_date, '%d/%m/%y')

    dates_to_repeat = [date + timedelta(days = d)  for d in DAYS_TO_REPEAT[score]]

    repeat_today = [d.date() == datetime.today().date() for d in dates_to_repeat]
    repeat = [i for i, x in enumerate(repeat_today) if x]

    if len(repeat) == 1:
        repeat_number = repeat[0] + 1
        message = "{}, repeat number {} of {} with an original score of {} on {}.".format(course, repeat_number, exercise, score, date.strftime("%d/%m/%y"))

        messages_to_push_today.append(message)


for m in messages_to_push_today:
    pushover_client.send_message(message=m, title="Spaced repetition")
