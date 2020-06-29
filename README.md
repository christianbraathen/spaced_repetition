# Spaced Repetition
A digital assistant helping you to identify when to repeat exercises. The assistant was built on two key principles: 1) that challenging exercises are more easily forgotten, and 2) every repetition makes it easier to retain the principles and methods of the exercise. 

The assistant is useful for students who want great, long-lasting learning and exam results without wasting time. New exercises are registered with `new_exercise()`, which are then saved automatically to `exercise_list.json`. By running `script.py` once per day, push notifications are sent to your mobile device via Pushover to remind you which exercises you have solved at an earlier date should be repeated today to avoid the retention rate to fall too much. Which exercise to repeat depends on two factors: how challenging the exercise originally was (A, B, or C, with C being the most challenging) and how many days have passed since the original exercise was solved.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install Pushover.

```
pip install python-pushover
```

- Create a user profile at [Pushover](https://pushover.net/) and get both app and user tokens. Save these in the bash profile as `PUSHOVER_APP` and `PUSHOVER_USER`, respectively.

## Usage

```
cd <path/to/this/repo
```

In Python:

```
from new_exercise import *
```

Then run `new_exercise(course, exercise, score, date=None)` in the Python shell. 

- `course` and `exercise` can be whatever string.
- `score` must be "A", "B", or "C".
- `date` must follow the `DD/MM/YY` format. If no date is provided, today's date will be used.

### Example

The following *will not* produce any errors:

```
new_exercise(course="MAT010", exercise="V20 #1", score="A")
new_exercise(course="MAT010", exercise="V20 #3", score="B", date="20/11/20")
```

The following *will* produce errors:

```
new_exercise(course="MAT010", exercise="V20 #4", score="A", date="20/11/2020") # Wrong year format
new_exercise(course="MAT010", exercise="V20 #2", score="D") # Wrong score
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

[GNU GPLv3](https://choosealicense.com/licenses/gpl-3.0/)