#!/usr/bin/env python

"""task_04.py: Homework Task 4."""

__author__      = "Joe Graham"

# constants
WEEKDAYS = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
DAYS_ABBR = map(lambda x: x.lower()[0:3], WEEKDAYS)
WEEKEND_DAYS = WEEKDAYS[5:7]
DAY_MAP = dict(zip(DAYS_ABBR, WEEKDAYS))
PROMPT_DAY = 'What day is it?  Note: You can enter three letter abbreviation (sat for Saturday etc.).'
PROMPT_TIME = 'Please enter time as 4 digits in 24 hour format.  (example: 2253 is 10:53 PM)'
INVALID_INPUT = 'Invalid input, please try again.'

# members
isWeekdayValid = False
isTimeValid = False

DAY = ''
TIME = ''
SNOOZE = 'can'

while not isWeekdayValid:
    print PROMPT_DAY
    dayVal = raw_input()
    if dayVal.lower()[0:3] in DAYS_ABBR:
        isWeekdayValid = True
        key = dayVal.lower()[0:3]
        DAY = DAY_MAP[key]
        SNOOZE += '' if DAY in WEEKEND_DAYS else ' not'
        while not isTimeValid:
            print PROMPT_TIME
            timeVal = raw_input()
            try:
                timeIntVal = int(timeVal)
                if (timeIntVal >= 0) and (timeIntVal <= 2459):
                    isTimeValid = True
                    TIME = '{}'.format(timeIntVal).zfill(4)
                else:
                    print INVALID_INPUT
                    continue
                isTimeValid = True
            except ValueError:
                print INVALID_INPUT
                continue
    else:
        print INVALID_INPUT
        continue

print 'Next alarm is {}, at {}, you {} snooze on this day.'.format(DAY, TIME, SNOOZE)