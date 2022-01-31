# *** FUNCTION MANUAL ***
# 1. import the function to your code via -> from hsltimes import timechecker
# 2. pass a time string as argument in hh:mm:ss format, for example 04:20:00. 
# 3. The function returns the difference in minutes between current time and 
#    time your passed in to the function. example timechecker("16:42:15") -> return difference in minutes


import sys
import math
from datetime import datetime

def timechecker(departure_time):
    today = datetime.today().date()
    dt_string = f"{today} {departure_time}"

    dt_object = datetime.strptime(dt_string, "%Y-%m-%d %H:%M:%S")

    dt_current = datetime.now()

    dt_difference = dt_object - dt_current
    minutes = math.floor(dt_difference.total_seconds() / 60)

    return minutes

sys.modules[__name__] = timechecker