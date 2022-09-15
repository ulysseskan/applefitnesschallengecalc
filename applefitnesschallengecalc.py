#!/usr/bin/env python3
"""Calculate exercise minutes
   or calories per day needed
   to meet a monthly Apple Fitness goal
   excluding Sundays
"""

import calendar
from datetime import datetime, date

# Ask for the amount of goal remaining for rest of month
goal = int(input ('Enter # of exercise minutes or calories needed this month: '))
exertionthusfar = int(input ('Enter the amount of exertion (in minutes or calories) done so far: '))
goalremaining = goal - exertionthusfar

# Find number of Sundays left in the month, ask user to provide expected Sunday exertion
sundaysleftinmonth = len([1 for i in calendar.monthcalendar(datetime.now().year, \
                        datetime.now().month) if i[6] != 0 and i[6] >= date.today().day])

expectedsundayexertion = int(input ('Enter the amount of exertion you expect to put in each Sunday \
(in minutes or calories), for example, 5 or 250: '))

# Determine upcoming Sunday exertion towards goal
upcomingsundayexertion = sundaysleftinmonth * expectedsundayexertion

# See how many days are left in the current month
daysleftinmonth = calendar.monthrange(datetime.now().year, datetime.now().month)[1] - \
                     date.today().day

# Determine how much exertion is needed per day -- excluding Sundays -- to meet goal
nonsundaysleftinmonth = daysleftinmonth - sundaysleftinmonth
newgoal = goalremaining - upcomingsundayexertion
needperday = newgoal / nonsundaysleftinmonth

rounded_up = -(-int(needperday) // 1) # round up by dividing on negative number and negating answer
output = f"You need about {rounded_up} minutes or calories per day for the rest of the month \
to meet your goal."
print(output)
