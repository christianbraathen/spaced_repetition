"""
This program automatically appends new exercises to the JSON list.
"""

import json
from datetime import datetime

def new_exercise(course, exercise, score, date=None):
    with open('exercise_list.json', 'r') as f:
        exercises = json.loads(f.read())

    if date is None:
        today = datetime.today().date()
        date = today.strftime("%d/%m/%y")

    stop = False
    if date is not None:
        try:
            datetime.strptime(date, "%d/%m/%y")
        except:
            print("The wrong date format is submitted. Please use the form DD/MM/YY.")
            stop = True

    if score != "A" and score != "B" and score != "C":
        print("The wrong score is submitted.")
        stop = True

    if stop is False:
        exercise_number = len(exercises) + 1
        new_exercise = {
            str(exercise_number) : {
                "course": course,
                "exercise": exercise,
                "score": score,
                "date": date
            }
        }

        exercises.update(new_exercise)

        with open('exercise_list.json', 'w') as f:
            json.dump(exercises, f)
    else:
        print("Could not save exercise to JSON file: errors occured.")
